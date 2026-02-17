from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class StoreResponse(BaseModel):
    id: int
    name: str
    slug: str
    color: Optional[str] = None
    category: Optional[str] = None
    promotion_count: int = 0

    class Config:
        from_attributes = True


class PromotionResponse(BaseModel):
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
    image_urls: List[str] = []
    status: str = "active"
    store: str = ""
    store_slug: str = ""
    days_left: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class PromotionListResponse(BaseModel):
    promotions: List[PromotionResponse]
    total: int
    page: int = 1
    limit: int = 20


class RatingStoreResponse(BaseModel):
    name: str
    slug: str
    color: Optional[str] = None
    count: int = 0
    max_discount: int = 0
    avg_discount: float = 0.0


class RatingResponse(BaseModel):
    stores: List[RatingStoreResponse]
    period: str = "weekly"


class StatsResponse(BaseModel):
    total_promotions: int = 0
    active_promotions: int = 0
    total_stores: int = 0
    max_discount: int = 0


class HealthResponse(BaseModel):
    status: str = "ok"
    timestamp: datetime
