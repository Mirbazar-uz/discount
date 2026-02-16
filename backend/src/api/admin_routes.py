import asyncio
import logging

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from ..auth.dependencies import get_current_admin
from ..auth.jwt_handler import create_token, verify_password
from ..database.connection import get_db
from ..database.admin_crud import (
    AdminPromotionCRUD,
    AdminStoreCRUD,
    AdminStatsCRUD,
    AdminLogCRUD,
)
from ..database.models import PromotionStatus
from .admin_schemas import (
    LoginRequest,
    TokenResponse,
    DashboardResponse,
    DashboardStats,
    AdminPromotionResponse,
    AdminPromotionListResponse,
    PromotionUpdateRequest,
    StatusUpdateRequest,
    AdminStoreResponse,
    AdminStoreListResponse,
    StoreUpdateRequest,
    SchedulerJobResponse,
    SchedulerJobsListResponse,
    TriggerResponse,
    PostLogResponse,
    PostLogListResponse,
)

logger = logging.getLogger(__name__)

admin_router = APIRouter(prefix="/admin", tags=["admin"])

_running_jobs: set = set()


def _build_promo_response(p) -> AdminPromotionResponse:
    return AdminPromotionResponse(
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
        store_name=p.store.name if p.store else "",
        store_slug=p.store.slug if p.store else "",
        posted_telegram=p.posted_telegram or False,
        posted_instagram=p.posted_instagram or False,
        created_at=p.created_at,
    )


def _build_store_response(s) -> AdminStoreResponse:
    active_count = len(
        [p for p in s.promotions if p.status == PromotionStatus.ACTIVE]
    ) if s.promotions else 0

    return AdminStoreResponse(
        id=s.id,
        name=s.name,
        slug=s.slug,
        telegram_channel=s.telegram_channel,
        website=s.website,
        color=s.color,
        category=s.category,
        is_active=s.is_active if s.is_active is not None else True,
        promotion_count=active_count,
        created_at=s.created_at,
    )


@admin_router.post("/login", response_model=TokenResponse)
async def admin_login(body: LoginRequest):
    if not verify_password(body.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Noto'g'ri parol",
        )

    token = create_token({"sub": "admin", "role": "admin"})
    return TokenResponse(access_token=token)


@admin_router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    admin: dict = Depends(get_current_admin),
):
    token = create_token({"sub": "admin", "role": "admin"})
    return TokenResponse(access_token=token)


@admin_router.get("/dashboard/stats", response_model=DashboardResponse)
async def dashboard_stats(
    admin: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    stats_crud = AdminStatsCRUD(db)
    stats_data = stats_crud.get_dashboard_stats()
    recent = stats_crud.get_recent_promotions(limit=10)

    return DashboardResponse(
        stats=DashboardStats(**stats_data),
        recent_promotions=[_build_promo_response(p) for p in recent],
    )


@admin_router.get("/promotions", response_model=AdminPromotionListResponse)
async def list_promotions(
    status_filter: str = Query(default="all", alias="status"),
    store: str = Query(default=None),
    search: str = Query(default=None),
    limit: int = Query(default=20, le=100),
    offset: int = 0,
    admin: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    crud = AdminPromotionCRUD(db)
    promotions, total = crud.get_all(
        status=status_filter,
        store_slug=store,
        search=search,
        limit=limit,
        offset=offset,
    )

    return AdminPromotionListResponse(
        promotions=[_build_promo_response(p) for p in promotions],
        total=total,
        limit=limit,
    )


@admin_router.put("/promotions/{promo_id}", response_model=AdminPromotionResponse)
async def update_promotion(
    promo_id: int,
    body: PromotionUpdateRequest,
    admin: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    crud = AdminPromotionCRUD(db)
    promo = crud.update(promo_id, body.model_dump(exclude_unset=True))

    if not promo:
        raise HTTPException(status_code=404, detail="Aksiya topilmadi")

    return _build_promo_response(promo)


@admin_router.delete("/promotions/{promo_id}")
async def delete_promotion(
    promo_id: int,
    admin: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    crud = AdminPromotionCRUD(db)
    deleted = crud.delete(promo_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Aksiya topilmadi")

    return {"success": True, "message": "Aksiya o'chirildi"}


@admin_router.patch(
    "/promotions/{promo_id}/status", response_model=AdminPromotionResponse
)
async def change_promotion_status(
    promo_id: int,
    body: StatusUpdateRequest,
    admin: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    crud = AdminPromotionCRUD(db)
    promo = crud.update_status(promo_id, body.status)

    if not promo:
        raise HTTPException(
            status_code=404, detail="Aksiya topilmadi yoki noto'g'ri status"
        )

    return _build_promo_response(promo)


@admin_router.get("/stores", response_model=AdminStoreListResponse)
async def list_stores(
    admin: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    crud = AdminStoreCRUD(db)
    stores = crud.get_all()

    return AdminStoreListResponse(
        stores=[_build_store_response(s) for s in stores],
        total=len(stores),
    )


@admin_router.put("/stores/{store_id}", response_model=AdminStoreResponse)
async def update_store(
    store_id: int,
    body: StoreUpdateRequest,
    admin: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    crud = AdminStoreCRUD(db)
    store = crud.update(store_id, body.model_dump(exclude_unset=True))

    if not store:
        raise HTTPException(status_code=404, detail="Do'kon topilmadi")

    return _build_store_response(store)


@admin_router.patch("/stores/{store_id}/toggle", response_model=AdminStoreResponse)
async def toggle_store(
    store_id: int,
    admin: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    crud = AdminStoreCRUD(db)
    store = crud.toggle_active(store_id)

    if not store:
        raise HTTPException(status_code=404, detail="Do'kon topilmadi")

    return _build_store_response(store)


@admin_router.get("/scheduler/jobs", response_model=SchedulerJobsListResponse)
async def list_scheduler_jobs(
    admin: dict = Depends(get_current_admin),
):
    from ..main import mirbazar_app

    scheduler = mirbazar_app.scheduler.scheduler
    jobs = scheduler.get_jobs()

    return SchedulerJobsListResponse(
        jobs=[
            SchedulerJobResponse(
                id=job.id,
                name=job.name or job.id,
                next_run_time=str(job.next_run_time) if job.next_run_time else None,
                trigger=str(job.trigger),
            )
            for job in jobs
        ]
    )


@admin_router.post("/scheduler/trigger/{job_id}", response_model=TriggerResponse)
async def trigger_job(
    job_id: str,
    admin: dict = Depends(get_current_admin),
):
    from ..main import mirbazar_app

    job_map = {
        "scraping": mirbazar_app.run_scraping,
        "daily_digest": mirbazar_app.post_daily_digest,
        "weekly_rating": mirbazar_app.post_weekly_rating,
        "monthly_summary": mirbazar_app.post_monthly_summary,
        "cleanup": mirbazar_app.cleanup_expired_promotions,
    }

    job_func = job_map.get(job_id)
    if not job_func:
        raise HTTPException(status_code=404, detail="Job topilmadi")

    if job_id in _running_jobs:
        raise HTTPException(
            status_code=409, detail=f"'{job_id}' allaqachon ishlamoqda"
        )

    _running_jobs.add(job_id)

    async def _run_and_cleanup():
        try:
            await job_func()
        finally:
            _running_jobs.discard(job_id)

    asyncio.create_task(_run_and_cleanup())
    logger.info("Admin triggered job: %s", job_id)

    return TriggerResponse(
        success=True,
        message=f"'{job_id}' job ishga tushirildi",
    )


@admin_router.get("/logs", response_model=PostLogListResponse)
async def list_logs(
    platform: str = Query(default=None),
    success: bool = Query(default=None),
    limit: int = Query(default=20, le=100),
    offset: int = 0,
    admin: dict = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    crud = AdminLogCRUD(db)
    logs, total = crud.get_logs(
        platform=platform,
        success=success,
        limit=limit,
        offset=offset,
    )

    from ..database.models import Promotion as PromoModel

    items = []
    for log in logs:
        promo_title = None
        if log.promotion_id:
            p = db.query(PromoModel).filter(
                PromoModel.id == log.promotion_id
            ).first()
            promo_title = p.title if p else None

        items.append(
            PostLogResponse(
                id=log.id,
                promotion_id=log.promotion_id,
                promotion_title=promo_title,
                platform=log.platform,
                post_type=log.post_type,
                post_id=log.post_id,
                success=log.success if log.success is not None else True,
                error_message=log.error_message,
                posted_at=log.posted_at,
            )
        )

    return PostLogListResponse(
        logs=items,
        total=total,
        limit=limit,
    )
