import httpx
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import re
import logging

from .parser import extract_image_url

logger = logging.getLogger(__name__)

PROMOTION_KEYWORDS = [
    "chegirma", "aksiya", "скидка", "акция",
    "%", "chegirmada", "sovg'a", "подарок",
    "arzon", "foydali", "выгодн", "bepul",
    "muddatli", "nasiya", "рассрочка",
    "1+1", "cashback", "keshbek", "кэшбек",
    "sale", "promo", "maxsus narx", "super narx",
]


class TelegramScraper:
    def __init__(self):
        self.client = httpx.Client(
            timeout=30,
            follow_redirects=True,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36"
                )
            },
        )

    def fetch_channel_posts(
        self, channel_url: str, limit: int = 20
    ) -> List[Dict]:
        try:
            response = self.client.get(channel_url)
            response.raise_for_status()
        except Exception as e:
            logger.error("Error fetching %s: %s", channel_url, e)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        posts: List[Dict] = []

        message_wraps = soup.find_all("div", class_="tgme_widget_message_wrap")

        for wrap in message_wraps[-limit:]:
            try:
                post = self._parse_message(wrap)
                if post:
                    posts.append(post)
            except Exception:
                continue

        return posts

    def _parse_message(self, wrap) -> Optional[Dict]:
        text_div = wrap.find("div", class_="tgme_widget_message_text")
        text = text_div.get_text(strip=True) if text_div else ""

        if not text:
            return None

        html_text = str(text_div) if text_div else ""

        time_tag = wrap.find("time")
        date_str = time_tag.get("datetime", "") if time_tag else ""

        link_tag = wrap.find("a", class_="tgme_widget_message_date")
        post_link = link_tag.get("href", "") if link_tag else ""
        post_id = post_link.split("/")[-1] if post_link else ""

        photo_wraps = wrap.find_all("a", class_="tgme_widget_message_photo_wrap")
        image_urls = []
        for pw in photo_wraps:
            img_style = pw.get("style", "")
            url = extract_image_url(img_style)
            if url:
                image_urls.append(url)

        views_span = wrap.find("span", class_="tgme_widget_message_views")
        views = views_span.get_text(strip=True) if views_span else "0"

        return {
            "text": text,
            "html_text": html_text,
            "date": date_str,
            "post_link": post_link,
            "post_id": post_id,
            "image_url": image_urls[0] if image_urls else None,
            "image_urls": image_urls,
            "views": views,
        }

    def is_promotion_post(self, text: str) -> bool:
        text_lower = text.lower()
        return any(kw in text_lower for kw in PROMOTION_KEYWORDS)

    def close(self):
        self.client.close()
