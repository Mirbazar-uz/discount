from pydantic_settings import BaseSettings
from typing import Optional

TIMEZONE = "Asia/Tashkent"


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://mirbazar:password@db:5432/mirbazar"

    GROQ_API_KEY: str = ""

    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_CHANNEL_ID: str = "@mirbazar_uz"
    TELEGRAM_ADMIN_ID: Optional[str] = None

    INSTAGRAM_USERNAME: str = ""
    INSTAGRAM_PASSWORD: str = ""

    ADMIN_PASSWORD: str = "changeme"
    JWT_SECRET: str = "changeme-jwt-secret"
    JWT_EXPIRE_HOURS: int = 24

    SCRAPE_INTERVAL_HOURS: int = 4
    POST_DELAY_SECONDS: int = 60
    MAX_POSTS_PER_DAY: int = 20
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
