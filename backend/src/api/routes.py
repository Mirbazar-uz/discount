from fastapi import APIRouter, Query, Depends
from typing import Optional, List
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy.orm import Session
from sqlalchemy import func

UZB_TZ = ZoneInfo("Asia/Tashkent")

from ..database.connection import get_db
from ..database.models import Promotion, Store, PromotionStatus
from ..database.crud import PromotionCRUD, StoreCRUD
from ..rating.calculator import RatingCalculator
from .schemas import (
    PromotionResponse,
    PromotionListResponse,
    RatingResponse,
    RatingStoreResponse,
    StoreResponse,
    StatsResponse,
    HealthResponse,
)

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="ok", timestamp=datetime.now(UZB_TZ))


@router.get("/promotions", response_model=PromotionListResponse)
async def get_promotions(
    category: Optional[str] = None,
    stores: Optional[str] = None,
    search: Optional[str] = None,
    status: str = "active",
    limit: int = Query(default=20, le=100),
    offset: int = 0,
    db: Session = Depends(get_db),
):
    crud = PromotionCRUD(db)
    store_slugs = stores.split(",") if stores else None

    promotions, total = crud.get_active_promotions(
        category=category,
        store_slugs=store_slugs,
        search=search,
        limit=limit,
        offset=offset,
    )

    now = datetime.now(UZB_TZ)
    items = []
    for p in promotions:
        days_left = None
        if p.deadline:
            days_left = max(0, (p.deadline - now).days)

        items.append(
            PromotionResponse(
                id=p.id,
                title=p.title,
                description=p.description,
                old_price=p.old_price,
                new_price=p.new_price,
                discount_percent=p.discount_percent,
                discount_text=p.discount_text,
                category=p.category,
                deadline_text=p.deadline_text,
                source_url=p.source_url,
                image_url=p.image_url,
                status=p.status.value if p.status else "active",
                store=p.store.name if p.store else "",
                store_slug=p.store.slug if p.store else "",
                days_left=days_left,
                created_at=p.created_at,
            )
        )

    return PromotionListResponse(
        promotions=items,
        total=total,
        limit=limit,
    )


@router.get("/promotions/{promo_id}", response_model=PromotionResponse)
async def get_promotion(promo_id: int, db: Session = Depends(get_db)):
    crud = PromotionCRUD(db)
    p = crud.get_by_id(promo_id)

    if not p:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="Promotion not found")

    now = datetime.now(UZB_TZ)
    days_left = None
    if p.deadline:
        days_left = max(0, (p.deadline - now).days)

    return PromotionResponse(
        id=p.id,
        title=p.title,
        description=p.description,
        old_price=p.old_price,
        new_price=p.new_price,
        discount_percent=p.discount_percent,
        discount_text=p.discount_text,
        category=p.category,
        deadline_text=p.deadline_text,
        source_url=p.source_url,
        image_url=p.image_url,
        status=p.status.value if p.status else "active",
        store=p.store.name if p.store else "",
        store_slug=p.store.slug if p.store else "",
        days_left=days_left,
        created_at=p.created_at,
    )


@router.get("/rating/weekly", response_model=RatingResponse)
async def get_weekly_rating(db: Session = Depends(get_db)):
    calc = RatingCalculator(db)
    stores_data = calc.calculate_weekly_rating()

    return RatingResponse(
        stores=[
            RatingStoreResponse(
                name=s["name"],
                slug=s["slug"],
                color=s.get("color"),
                count=s["count"],
                max_discount=s["max_discount"],
                avg_discount=s["avg_discount"],
            )
            for s in stores_data
        ],
        period="weekly",
    )


@router.get("/rating/monthly", response_model=RatingResponse)
async def get_monthly_rating(db: Session = Depends(get_db)):
    calc = RatingCalculator(db)
    stores_data = calc.calculate_monthly_rating()

    return RatingResponse(
        stores=[
            RatingStoreResponse(
                name=s["name"],
                slug=s["slug"],
                color=s.get("color"),
                count=s["count"],
                max_discount=s["max_discount"],
                avg_discount=s["avg_discount"],
            )
            for s in stores_data
        ],
        period="monthly",
    )


@router.get("/stores", response_model=List[StoreResponse])
async def get_stores(db: Session = Depends(get_db)):
    crud = StoreCRUD(db)
    stores = crud.get_all_active()

    return [
        StoreResponse(
            id=s.id,
            name=s.name,
            slug=s.slug,
            color=s.color,
            category=s.category,
            promotion_count=len(
                [p for p in s.promotions if p.status == PromotionStatus.ACTIVE]
            ),
        )
        for s in stores
    ]


@router.get("/stats", response_model=StatsResponse)
async def get_stats(db: Session = Depends(get_db)):
    total = db.query(func.count(Promotion.id)).scalar() or 0
    active = (
        db.query(func.count(Promotion.id))
        .filter(Promotion.status == PromotionStatus.ACTIVE)
        .scalar()
        or 0
    )
    store_count = (
        db.query(func.count(Store.id)).filter(Store.is_active == True).scalar() or 0
    )
    max_disc = (
        db.query(func.max(Promotion.discount_percent))
        .filter(Promotion.status == PromotionStatus.ACTIVE)
        .scalar()
        or 0
    )

    return StatsResponse(
        total_promotions=total,
        active_promotions=active,
        total_stores=store_count,
        max_discount=max_disc,
    )
