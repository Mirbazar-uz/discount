from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


class MirbazarScheduler:
    def __init__(self, app):
        self.app = app
        self.scheduler = AsyncIOScheduler()

    def setup_jobs(self):
        self.scheduler.add_job(
            self.app.run_scraping,
            CronTrigger(hour="*/4"),
            id="scraping",
            name="Telegram kanallardan scraping",
        )

        self.scheduler.add_job(
            self.app.post_daily_digest,
            CronTrigger(hour=9, minute=0),
            id="daily_digest",
            name="Kunlik TOP-5 digest",
        )

        self.scheduler.add_job(
            self.app.post_weekly_rating,
            CronTrigger(day_of_week="mon", hour=10, minute=0),
            id="weekly_rating",
            name="Haftalik reyting",
        )

        self.scheduler.add_job(
            self.app.post_monthly_summary,
            CronTrigger(day=1, hour=11, minute=0),
            id="monthly_summary",
            name="Oylik xulosa",
        )

        self.scheduler.add_job(
            self.app.cleanup_expired_promotions,
            CronTrigger(hour=0, minute=0),
            id="cleanup",
            name="Eskirgan aksiyalarni tozalash",
        )

    def start(self):
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()
