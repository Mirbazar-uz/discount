from instagrapi import Client
from typing import Optional, List, Dict
import logging

from .formatter import format_promotion_instagram, format_rating_instagram

logger = logging.getLogger(__name__)


class InstagramPoster:
    def __init__(self, username: str, password: str):
        self.client = Client()
        self.username = username
        self.password = password
        self._logged_in = False

    def login(self):
        if not self._logged_in:
            try:
                self.client.login(self.username, self.password)
                self._logged_in = True
            except Exception as e:
                logger.error("Instagram login error: %s", e)
                raise

    def post_promotion(
        self, data: Dict, image_path: str
    ) -> Optional[str]:
        self.login()
        caption = format_promotion_instagram(data)

        try:
            media = self.client.photo_upload(image_path, caption)
            return str(media.pk)
        except Exception as e:
            logger.error("Instagram post error: %s", e)
            return None

    def post_rating(
        self,
        stores_data: List[Dict],
        image_path: str,
        period: str = "Haftalik",
    ) -> Optional[str]:
        self.login()
        caption = format_rating_instagram(stores_data, period)

        try:
            media = self.client.photo_upload(image_path, caption)
            return str(media.pk)
        except Exception as e:
            logger.error("Instagram rating post error: %s", e)
            return None
