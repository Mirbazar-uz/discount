from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from typing import List, Dict
from zoneinfo import ZoneInfo

from ..database.models import Promotion, Store, StoreStats, PromotionStatus

UZB_TZ = ZoneInfo("Asia/Tashkent")


class RatingCalculator:
    def __init__(self, db: Session):
        self.db = db

    def calculate_weekly_rating(self) -> List[Dict]:
        week_ago = datetime.now(UZB_TZ) - timedelta(days=7)

        stats = (
            self.db.query(
                Store.id,
                Store.name,
                Store.slug,
                Store.color,
                func.count(Promotion.id).label("count"),
                func.max(Promotion.discount_percent).label("max_discount"),
                func.avg(Promotion.discount_percent).label("avg_discount"),
            )
            .join(Promotion, Store.id == Promotion.store_id)
            .filter(
                Promotion.created_at >= week_ago,
                Promotion.status == PromotionStatus.ACTIVE,
            )
            .group_by(Store.id)
            .order_by(func.count(Promotion.id).desc())
            .all()
        )

        return [
            {
                "id": s.id,
                "name": s.name,
                "slug": s.slug,
                "color": s.color,
                "count": s.count,
                "max_discount": s.max_discount or 0,
                "avg_discount": round(s.avg_discount or 0, 1),
            }
            for s in stats
        ]

    def calculate_monthly_rating(self) -> List[Dict]:
        month_ago = datetime.now(UZB_TZ) - timedelta(days=30)

        stats = (
            self.db.query(
                Store.id,
                Store.name,
                Store.slug,
                Store.color,
                func.count(Promotion.id).label("count"),
                func.max(Promotion.discount_percent).label("max_discount"),
                func.avg(Promotion.discount_percent).label("avg_discount"),
            )
            .join(Promotion, Store.id == Promotion.store_id)
            .filter(Promotion.created_at >= month_ago)
            .group_by(Store.id)
            .order_by(func.count(Promotion.id).desc())
            .all()
        )

        return [
            {
                "id": s.id,
                "name": s.name,
                "slug": s.slug,
                "color": s.color,
                "count": s.count,
                "max_discount": s.max_discount or 0,
                "avg_discount": round(s.avg_discount or 0, 1),
            }
            for s in stats
        ]

    def get_top_discounts(self, limit: int = 5) -> List[Dict]:
        promotions = (
            self.db.query(Promotion)
            .join(Store)
            .filter(Promotion.status == PromotionStatus.ACTIVE)
            .order_by(Promotion.discount_percent.desc())
            .limit(limit)
            .all()
        )

        return [
            {
                "id": p.id,
                "title": p.title,
                "store": p.store.name,
                "discount_percent": p.discount_percent,
                "discount_text": p.discount_text,
                "new_price": p.new_price,
                "old_price": p.old_price,
            }
            for p in promotions
        ]

    def save_weekly_stats(self):
        stats = self.calculate_weekly_rating()
        now = datetime.now(UZB_TZ)
        week_start = now - timedelta(days=7)

        for s in stats:
            store_stat = StoreStats(
                store_id=s["id"],
                period_type="weekly",
                period_start=week_start,
                period_end=now,
                total_promotions=s["count"],
                max_discount=s["max_discount"],
                avg_discount=s["avg_discount"],
            )
            self.db.add(store_stat)

        self.db.commit()
