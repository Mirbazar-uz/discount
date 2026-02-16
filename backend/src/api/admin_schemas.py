from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class LoginRequest(BaseModel):
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class DashboardStats(BaseModel):
    total_promotions: int = 0
    active_promotions: int = 0
    expired_promotions: int = 0
    total_stores: int = 0
    active_stores: int = 0
    total_posts: int = 0
    successful_posts: int = 0
    failed_posts: int = 0


class AdminPromotionResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    old_price: Optional[float] = None
    new_price: Optional[float] = None
    discount_percent: Optional[int] = None
    discount_text: Optional[str] = None
    category: Optional[str] = None
    deadline_text: Optional[str] = None
    source_url: Optional[str] = None
    image_url: Optional[str] = None
    status: str = "active"
    store_name: str = ""
    store_slug: str = ""
    posted_telegram: bool = False
    posted_instagram: bool = False
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class AdminPromotionListResponse(BaseModel):
    promotions: List[AdminPromotionResponse]
    total: int
    page: int = 1
    limit: int = 20


class PromotionUpdateRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    old_price: Optional[float] = None
    new_price: Optional[float] = None
    discount_percent: Optional[int] = None
    discount_text: Optional[str] = None
    category: Optional[str] = None
    deadline_text: Optional[str] = None


class StatusUpdateRequest(BaseModel):
    status: str


class AdminStoreResponse(BaseModel):
    id: int
    name: str
    slug: str
    telegram_channel: Optional[str] = None
    website: Optional[str] = None
    color: Optional[str] = None
    category: Optional[str] = None
    is_active: bool = True
    promotion_count: int = 0
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class AdminStoreListResponse(BaseModel):
    stores: List[AdminStoreResponse]
    total: int


class StoreUpdateRequest(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    telegram_channel: Optional[str] = None
    website: Optional[str] = None
    color: Optional[str] = None
    category: Optional[str] = None


class SchedulerJobResponse(BaseModel):
    id: str
    name: str
    next_run_time: Optional[str] = None
    trigger: str = ""


class SchedulerJobsListResponse(BaseModel):
    jobs: List[SchedulerJobResponse]


class TriggerResponse(BaseModel):
    success: bool
    message: str


class PostLogResponse(BaseModel):
    id: int
    promotion_id: Optional[int] = None
    promotion_title: Optional[str] = None
    platform: Optional[str] = None
    post_type: Optional[str] = None
    post_id: Optional[str] = None
    success: bool = True
    error_message: Optional[str] = None
    posted_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class PostLogListResponse(BaseModel):
    logs: List[PostLogResponse]
    total: int
    page: int = 1
    limit: int = 20


class DashboardResponse(BaseModel):
    stats: DashboardStats
    recent_promotions: List[AdminPromotionResponse]
