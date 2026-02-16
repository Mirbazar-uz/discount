from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from datetime import datetime
from typing import Optional, List, Dict
from zoneinfo import ZoneInfo

from .models import Promotion, Store, PostLog, PromotionStatus

UZB_TZ = ZoneInfo("Asia/Tashkent")


class AdminPromotionCRUD:
    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        status: Optional[str] = None,
        store_slug: Optional[str] = None,
        search: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> tuple:
        query = self.db.query(Promotion).join(Store)

        if status and status != "all":
            try:
                status_enum = PromotionStatus(status)
                query = query.filter(Promotion.status == status_enum)
            except ValueError:
                pass

        if store_slug:
            query = query.filter(Store.slug == store_slug)

        if search:
            sanitized = search.replace("%", "\\%").replace("_", "\\_")
            query = query.filter(Promotion.title.ilike(f"%{sanitized}%"))

        total = query.count()
        promotions = (
            query.order_by(Promotion.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )

        return promotions, total

    def update(self, promo_id: int, data: Dict) -> Optional[Promotion]:
        promo = self.db.query(Promotion).filter(
            Promotion.id == promo_id
        ).first()

        if not promo:
            return None

        update_data = {k: v for k, v in data.items() if v is not None}

        if update_data:
            self.db.query(Promotion).filter(
                Promotion.id == promo_id
            ).update(update_data)
            self.db.commit()
            self.db.refresh(promo)

        return promo

    def delete(self, promo_id: int) -> bool:
        promo = self.db.query(Promotion).filter(
            Promotion.id == promo_id
        ).first()

        if not promo:
            return False

        self.db.delete(promo)
        self.db.commit()
        return True

    def update_status(self, promo_id: int, status: str) -> Optional[Promotion]:
        promo = self.db.query(Promotion).filter(
            Promotion.id == promo_id
        ).first()

        if not promo:
            return None

        try:
            status_enum = PromotionStatus(status)
        except ValueError:
            return None

        update_fields = {"status": status_enum}
        if status_enum == PromotionStatus.EXPIRED:
            update_fields["expired_at"] = datetime.now(UZB_TZ)

        self.db.query(Promotion).filter(
            Promotion.id == promo_id
        ).update(update_fields)
        self.db.commit()
        self.db.refresh(promo)

        return promo

    def get_by_id(self, promo_id: int) -> Optional[Promotion]:
        return self.db.query(Promotion).filter(
            Promotion.id == promo_id
        ).first()


class AdminStoreCRUD:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Store]:
        return self.db.query(Store).order_by(Store.name).all()

    def get_by_id(self, store_id: int) -> Optional[Store]:
        return self.db.query(Store).filter(Store.id == store_id).first()

    def update(self, store_id: int, data: Dict) -> Optional[Store]:
        store = self.db.query(Store).filter(Store.id == store_id).first()

        if not store:
            return None

        update_data = {k: v for k, v in data.items() if v is not None}

        if update_data:
            self.db.query(Store).filter(
                Store.id == store_id
            ).update(update_data)
            self.db.commit()
            self.db.refresh(store)

        return store

    def toggle_active(self, store_id: int) -> Optional[Store]:
        store = self.db.query(Store).filter(Store.id == store_id).first()

        if not store:
            return None

        new_status = not store.is_active
        self.db.query(Store).filter(
            Store.id == store_id
        ).update({"is_active": new_status})
        self.db.commit()
        self.db.refresh(store)

        return store


class AdminStatsCRUD:
    def __init__(self, db: Session):
        self.db = db

    def get_dashboard_stats(self) -> Dict:
        total_promos = self.db.query(func.count(Promotion.id)).scalar() or 0
        active_promos = (
            self.db.query(func.count(Promotion.id))
            .filter(Promotion.status == PromotionStatus.ACTIVE)
            .scalar() or 0
        )
        expired_promos = (
            self.db.query(func.count(Promotion.id))
            .filter(Promotion.status == PromotionStatus.EXPIRED)
            .scalar() or 0
        )
        total_stores = self.db.query(func.count(Store.id)).scalar() or 0
        active_stores = (
            self.db.query(func.count(Store.id))
            .filter(Store.is_active == True)
            .scalar() or 0
        )
        total_posts = self.db.query(func.count(PostLog.id)).scalar() or 0
        successful_posts = (
            self.db.query(func.count(PostLog.id))
            .filter(PostLog.success == True)
            .scalar() or 0
        )
        failed_posts = (
            self.db.query(func.count(PostLog.id))
            .filter(PostLog.success == False)
            .scalar() or 0
        )

        return {
            "total_promotions": total_promos,
            "active_promotions": active_promos,
            "expired_promotions": expired_promos,
            "total_stores": total_stores,
            "active_stores": active_stores,
            "total_posts": total_posts,
            "successful_posts": successful_posts,
            "failed_posts": failed_posts,
        }

    def get_recent_promotions(self, limit: int = 10) -> List[Promotion]:
        return (
            self.db.query(Promotion)
            .join(Store)
            .order_by(Promotion.created_at.desc())
            .limit(limit)
            .all()
        )


class AdminLogCRUD:
    def __init__(self, db: Session):
        self.db = db

    def get_logs(
        self,
        platform: Optional[str] = None,
        success: Optional[bool] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> tuple:
        query = self.db.query(PostLog)

        if platform:
            query = query.filter(PostLog.platform == platform)

        if success is not None:
            query = query.filter(PostLog.success == success)

        total = query.count()
        logs = (
            query.order_by(PostLog.posted_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )

        return logs, total
