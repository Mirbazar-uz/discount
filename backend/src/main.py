import asyncio
import logging
from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone as tz
from zoneinfo import ZoneInfo

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import Settings
from .scraper.telegram_scraper import TelegramScraper
from .scraper.channels import TELEGRAM_CHANNELS
from .ai.groq_client import GroqClient
from .ai.validator import PromotionValidator
from .database.connection import get_db, init_db
from .database.crud import PromotionCRUD, StoreCRUD
from .image.generator import ImageGenerator
from .poster.telegram_poster import TelegramPoster
from .poster.instagram_poster import InstagramPoster
from .rating.calculator import RatingCalculator
from .scheduler.jobs import MirbazarScheduler
from .api.routes import router
from .api.admin_routes import admin_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


class MirbazarApp:
    def __init__(self):
        self.settings = Settings()

        self.scraper = TelegramScraper()
        self.groq = GroqClient(
            self.settings.GROQ_API_KEY,
            vision_model=self.settings.GROQ_VISION_MODEL,
        )
        self.validator = PromotionValidator()
        self.image_gen = ImageGenerator()
        self.telegram = TelegramPoster(
            self.settings.TELEGRAM_BOT_TOKEN,
            self.settings.TELEGRAM_CHANNEL_ID,
        )
        self.instagram = InstagramPoster(
            self.settings.INSTAGRAM_USERNAME,
            self.settings.INSTAGRAM_PASSWORD,
        )

        init_db()
        self.scheduler = MirbazarScheduler(self)

    def _get_db_session(self):
        return next(get_db())

    async def run_scraping(self):
        logger.info("Scraping boshlandi...")

        for channel in TELEGRAM_CHANNELS:
            try:
                await self._scrape_channel(channel)
            except Exception as e:
                logger.error("Channel scraping error %s: %s", channel["name"], e)
            await asyncio.sleep(5)

        logger.info("Scraping tugadi")

    async def _scrape_channel(self, channel: dict):
        logger.info("  Scraping: %s", channel["name"])

        db = self._get_db_session()
        try:
            store_crud = StoreCRUD(db)
            promo_crud = PromotionCRUD(db)

            store = store_crud.get_or_create(channel)
            posts = self.scraper.fetch_channel_posts(channel["url"], limit=20)

            for post in posts:
                if not self.scraper.is_promotion_post(post["text"]):
                    continue

                if promo_crud.exists_by_source_id(post["post_id"]):
                    continue

                image_urls = post.get("image_urls", [])
                if not image_urls and post.get("image_url"):
                    image_urls = [post["image_url"]]

                if image_urls:
                    parsed = self.groq.parse_promotion_with_image(
                        post["text"], image_urls, channel["name"]
                    )
                else:
                    parsed = self.groq.parse_promotion(post["text"], channel["name"])

                if not parsed or parsed.get("is_promotion") is False:
                    continue

                validated = self.validator.validate(parsed)

                if validated.get("low_confidence"):
                    continue

                promotion = promo_crud.create(
                    store_id=store.id,
                    data=validated,
                    source_post_id=post["post_id"],
                    source_url=post["post_link"],
                    image_url=image_urls[0] if image_urls else None,
                    image_urls=image_urls,
                )

                if promotion and validated.get("is_active"):
                    image_data = {
                        **validated,
                        "store": channel["name"],
                        "id": promotion.id,
                    }
                    image_path = self.image_gen.create_promotion_image(image_data)
                    promo_crud.update_image_path(promotion.id, image_path)

                    if not image_urls:
                        filename = Path(image_path).name
                        promo_crud.update_display_image(
                            promotion.id, f"/images/{filename}"
                        )

                    await self._post_to_telegram(promotion, image_path)
                    await self._post_to_instagram(promotion, image_path, promo_crud)
        finally:
            db.close()

    async def _post_to_telegram(self, promotion, image_path: str):
        data = {
            "store": promotion.store.name,
            "title": promotion.title,
            "old_price": promotion.old_price,
            "new_price": promotion.new_price,
            "discount_text": promotion.discount_text,
            "discount_percent": promotion.discount_percent,
            "deadline_text": promotion.deadline_text,
            "source_url": promotion.source_url,
            "id": promotion.id,
        }

        db = self._get_db_session()
        try:
            promo_crud = PromotionCRUD(db)
            post_id = await self.telegram.post_promotion(data, image_path)
            if post_id:
                promo_crud.mark_posted(promotion.id, "telegram", post_id)
                await asyncio.sleep(self.settings.POST_DELAY_SECONDS)
        finally:
            db.close()

    async def _post_to_instagram(self, promotion, image_path: str, promo_crud):
        today_posts = promo_crud.count_today_instagram_posts()
        if today_posts >= 5:
            return

        data = {
            "store": promotion.store.name,
            "title": promotion.title,
            "old_price": promotion.old_price,
            "new_price": promotion.new_price,
            "discount_text": promotion.discount_text,
            "discount_percent": promotion.discount_percent,
            "deadline_text": promotion.deadline_text,
        }

        post_id = self.instagram.post_promotion(data, image_path)

        if post_id:
            promo_crud.mark_posted(promotion.id, "instagram", post_id)

    async def post_daily_digest(self):
        logger.info("Kunlik digest...")

        db = self._get_db_session()
        try:
            calc = RatingCalculator(db)
            top_promos = calc.get_top_discounts(5)

            if not top_promos:
                return

            image_path = self.image_gen.create_digest_image(top_promos)
            await self.telegram.post_digest(top_promos, image_path)
        finally:
            db.close()

    async def post_weekly_rating(self):
        logger.info("Haftalik reyting...")

        db = self._get_db_session()
        try:
            calc = RatingCalculator(db)
            stores_data = calc.calculate_weekly_rating()

            if not stores_data:
                return

            image_path = self.image_gen.create_rating_image(stores_data, "Haftalik")
            await self.telegram.post_rating(stores_data, image_path, "Haftalik")

            calc.save_weekly_stats()
        finally:
            db.close()

    async def post_monthly_summary(self):
        logger.info("Oylik xulosa...")

        db = self._get_db_session()
        try:
            calc = RatingCalculator(db)
            stores_data = calc.calculate_monthly_rating()

            if not stores_data:
                return

            image_path = self.image_gen.create_rating_image(stores_data, "Oylik")
            await self.telegram.post_rating(stores_data, image_path, "Oylik")
        finally:
            db.close()

    async def cleanup_expired_promotions(self):
        logger.info("Tozalash...")

        db = self._get_db_session()
        try:
            promo_crud = PromotionCRUD(db)
            threshold = datetime.now(ZoneInfo("Asia/Tashkent")) - timedelta(days=30)
            promo_crud.delete_old_expired(threshold)
            promo_crud.mark_expired()
        finally:
            db.close()

    def start_scheduler(self):
        self.scheduler.setup_jobs()
        self.scheduler.start()

    def stop(self):
        self.scheduler.stop()
        self.scraper.close()


mirbazar_app = MirbazarApp()


@asynccontextmanager
async def lifespan(application: FastAPI):
    mirbazar_app.start_scheduler()
    logger.info("Mirbazar ishga tushdi!")
    yield
    mirbazar_app.stop()
    logger.info("Mirbazar to'xtatildi")


app = FastAPI(
    title="Mirbazar.uz API",
    description="Barcha chegirmalar bir joyda",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generated_images_dir = Path("generated_images")
generated_images_dir.mkdir(exist_ok=True)
app.mount("/images", StaticFiles(directory=str(generated_images_dir)), name="images")

app.include_router(router)
app.include_router(admin_router)
