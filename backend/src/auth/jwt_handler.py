import hmac
from datetime import datetime, timedelta, timezone

import jwt

from ..config import Settings

settings = Settings()


def verify_password(plain_password: str) -> bool:
    return hmac.compare_digest(plain_password, settings.ADMIN_PASSWORD)


def create_token(data: dict) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        hours=settings.JWT_EXPIRE_HOURS
    )
    payload = {
        **data,
        "exp": expire,
        "iat": datetime.now(timezone.utc),
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")


def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET, algorithms=["HS256"]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token muddati tugagan")
    except jwt.InvalidTokenError:
        raise ValueError("Noto'g'ri token")
