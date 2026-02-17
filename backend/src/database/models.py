from sqlalchemy import (
    Column, Integer, String, Float, DateTime,
    Boolean, Enum, ForeignKey, Text,
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
import enum

Base = declarative_base()


class PromotionStatus(enum.Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    DELETED = "deleted"


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(50), unique=True, nullable=False)
    telegram_channel = Column(String(100))
    website = Column(String(200))
    logo_path = Column(String(200))
    color = Column(String(7))
    category = Column(String(50))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    promotions = relationship("Promotion", back_populates="store")
    stats = relationship("StoreStats", back_populates="store")


class PromotionImage(Base):
    __tablename__ = "promotion_images"

    id = Column(Integer, primary_key=True)
    promotion_id = Column(Integer, ForeignKey("promotions.id", ondelete="CASCADE"), nullable=False)
    image_url = Column(String(500), nullable=False)
    position = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    promotion = relationship("Promotion", back_populates="images")


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)

    title = Column(String(300), nullable=False)
    description = Column(Text)

    old_price = Column(Float)
    new_price = Column(Float)
    discount_percent = Column(Integer)
    discount_text = Column(String(50))

    category = Column(String(50))

    deadline = Column(DateTime)
    deadline_text = Column(String(100))

    source_url = Column(String(500))
    source_post_id = Column(String(100))
    image_url = Column(String(500))

    status = Column(Enum(PromotionStatus), default=PromotionStatus.ACTIVE)

    created_at = Column(DateTime, default=datetime.utcnow)
    expired_at = Column(DateTime)

    posted_telegram = Column(Boolean, default=False)
    posted_instagram = Column(Boolean, default=False)
    telegram_post_id = Column(String(100))
    instagram_post_id = Column(String(100))

    generated_image_path = Column(String(300))

    store = relationship("Store", back_populates="promotions")
    images = relationship(
        "PromotionImage",
        back_populates="promotion",
        order_by="PromotionImage.position",
        cascade="all, delete-orphan",
    )


class StoreStats(Base):
    __tablename__ = "store_stats"

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)

    period_type = Column(String(20))
    period_start = Column(DateTime)
    period_end = Column(DateTime)

    total_promotions = Column(Integer, default=0)
    max_discount = Column(Integer, default=0)
    avg_discount = Column(Float, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)

    store = relationship("Store", back_populates="stats")


class PostLog(Base):
    __tablename__ = "post_logs"

    id = Column(Integer, primary_key=True)
    promotion_id = Column(Integer, ForeignKey("promotions.id"))

    platform = Column(String(20))
    post_type = Column(String(30))
    post_id = Column(String(100))

    success = Column(Boolean, default=True)
    error_message = Column(Text)

    posted_at = Column(DateTime, default=datetime.utcnow)
