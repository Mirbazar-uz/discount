from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from typing import Dict, Optional, List
from zoneinfo import ZoneInfo

from .models import Promotion, PromotionImage, Store, StoreStats, PostLog, PromotionStatus

UZB_TZ = ZoneInfo("Asia/Tashkent")


class StoreCRUD:
    def __init__(self, db: Session):
        self.db = db

    def get_or_create(self, channel_data: Dict) -> Store:
        store = self.db.query(Store).filter(
            Store.slug == channel_data["slug"]
        ).first()

        if not store:
            store = Store(
                name=channel_data["name"],
                slug=channel_data["slug"],
                telegram_channel=channel_data.get("channel", ""),
                website=channel_data.get("website", ""),
                color=channel_data.get("color", "#7c3aed"),
                category=channel_data.get("category", "electronics"),
                logo_path=f"assets/logos/{channel_data['slug']}.png",
            )
            self.db.add(store)
            self.db.commit()
            self.db.refresh(store)

        return store

    def get_all_active(self) -> List[Store]:
        return self.db.query(Store).filter(
            Store.is_active == True
        ).all()

    def get_by_slug(self, slug: str) -> Optional[Store]:
        return self.db.query(Store).filter(Store.slug == slug).first()


class PromotionCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        store_id: int,
        data: Dict,
        source_post_id: str,
        source_url: str,
        image_url: Optional[str] = None,
        image_urls: Optional[List[str]] = None,
    ) -> Optional[Promotion]:
        try:
            deadline = None
            if data.get("deadline"):
                try:
                    deadline = datetime.fromisoformat(data["deadline"])
                except (ValueError, TypeError):
                    deadline = None

            promotion = Promotion(
                store_id=store_id,
                title=data.get("title", "Aksiya"),
                description=data.get("description", ""),
                old_price=data.get("old_price"),
                new_price=data.get("new_price"),
                discount_percent=data.get("discount_percent", 0),
                discount_text=data.get("discount_text", ""),
                category=data.get("category", "other"),
                deadline=deadline,
                deadline_text=data.get("deadline_text", ""),
                source_url=source_url,
                source_post_id=source_post_id,
                image_url=image_url,
                status=PromotionStatus.ACTIVE
                if data.get("is_active", True)
                else PromotionStatus.EXPIRED,
            )
            self.db.add(promotion)
            self.db.commit()
            self.db.refresh(promotion)

            urls = image_urls or ([image_url] if image_url else [])
            for i, url in enumerate(urls):
                img = PromotionImage(
                    promotion_id=promotion.id,
                    image_url=url,
                    position=i,
                )
                self.db.add(img)
            if urls:
                self.db.commit()

            return promotion
        except Exception as e:
            self.db.rollback()
            raise RuntimeError(f"Failed to create promotion: {e}") from e

    def exists_by_source_id(self, source_post_id: str) -> bool:
        return (
            self.db.query(Promotion)
            .filter(Promotion.source_post_id == source_post_id)
            .first()
            is not None
        )

    def update_image_path(self, promo_id: int, image_path: str):
        promo = self.db.query(Promotion).filter(Promotion.id == promo_id).first()
        if promo:
            self.db.query(Promotion).filter(Promotion.id == promo_id).update(
                {"generated_image_path": image_path}
            )
            self.db.commit()

    def update_display_image(self, promo_id: int, image_url: str):
        self.db.query(Promotion).filter(Promotion.id == promo_id).update(
            {"image_url": image_url}
        )
        self.db.commit()

    def mark_posted(self, promo_id: int, platform: str, post_id: str):
        updates: Dict = {}
        if platform == "telegram":
            updates = {"posted_telegram": True, "telegram_post_id": post_id}
        elif platform == "instagram":
            updates = {"posted_instagram": True, "instagram_post_id": post_id}

        if updates:
            self.db.query(Promotion).filter(Promotion.id == promo_id).update(updates)
            self.db.commit()

        log = PostLog(
            promotion_id=promo_id,
            platform=platform,
            post_type="single",
            post_id=post_id,
            success=True,
        )
        self.db.add(log)
        self.db.commit()

    def count_today_instagram_posts(self) -> int:
        today_start = datetime.now(UZB_TZ).replace(hour=0, minute=0, second=0, microsecond=0)
        return (
            self.db.query(Promotion)
            .filter(
                Promotion.posted_instagram == True,
                Promotion.created_at >= today_start,
            )
            .count()
        )

    def get_active_promotions(
        self,
        category: Optional[str] = None,
        store_slugs: Optional[List[str]] = None,
        search: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> tuple:
        query = (
            self.db.query(Promotion)
            .join(Store)
            .filter(Promotion.status == PromotionStatus.ACTIVE)
        )

        if category and category != "all":
            query = query.filter(Promotion.category == category)

        if store_slugs:
            query = query.filter(Store.slug.in_(store_slugs))

        if search:
            query = query.filter(Promotion.title.ilike(f"%{search}%"))

        total = query.count()
        promotions = (
            query.order_by(Promotion.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )

        return promotions, total

    def get_by_id(self, promo_id: int) -> Optional[Promotion]:
        return self.db.query(Promotion).filter(Promotion.id == promo_id).first()

    def mark_expired(self):
        now = datetime.now(UZB_TZ)
        self.db.query(Promotion).filter(
            Promotion.status == PromotionStatus.ACTIVE,
            Promotion.deadline != None,
            Promotion.deadline < now,
        ).update(
            {"status": PromotionStatus.EXPIRED, "expired_at": now},
            synchronize_session=False,
        )
        self.db.commit()

    def delete_old_expired(self, threshold: datetime):
        self.db.query(Promotion).filter(
            Promotion.status == PromotionStatus.EXPIRED,
            Promotion.expired_at != None,
            Promotion.expired_at < threshold,
        ).update(
            {"status": PromotionStatus.DELETED},
            synchronize_session=False,
        )
        self.db.commit()
