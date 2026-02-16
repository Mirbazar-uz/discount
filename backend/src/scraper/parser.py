import re
from typing import Optional


def extract_image_url(style: str) -> Optional[str]:
    match = re.search(r"url\('([^']+)'\)", style)
    return match.group(1) if match else None


def clean_price_text(text: str) -> Optional[float]:
    cleaned = re.sub(r"[^\d]", "", text)
    if cleaned:
        return float(cleaned)
    return None


def extract_percentage(text: str) -> Optional[int]:
    match = re.search(r"(\d+)\s*%", text)
    if match:
        return int(match.group(1))
    return None
