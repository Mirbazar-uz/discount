from telegram import Bot
from telegram.constants import ParseMode
from typing import Optional, List, Dict
import logging

from .formatter import format_promotion_text, format_rating_text, format_digest_text

logger = logging.getLogger(__name__)


class TelegramPoster:
    def __init__(self, token: str, channel_id: str):
        self.bot = Bot(token=token)
        self.channel_id = channel_id

    async def post_promotion(
        self, data: Dict, image_path: str
    ) -> Optional[str]:
        caption = format_promotion_text(data)

        try:
            with open(image_path, "rb") as photo:
                message = await self.bot.send_photo(
                    chat_id=self.channel_id,
                    photo=photo,
                    caption=caption,
                    parse_mode=ParseMode.HTML,
                )
            return str(message.message_id)
        except Exception as e:
            logger.error("Telegram post error: %s", e)
            return None

    async def post_rating(
        self,
        stores_data: List[Dict],
        image_path: str,
        period: str = "Haftalik",
    ) -> Optional[str]:
        caption = format_rating_text(stores_data, period)

        try:
            with open(image_path, "rb") as photo:
                message = await self.bot.send_photo(
                    chat_id=self.channel_id,
                    photo=photo,
                    caption=caption,
                    parse_mode=ParseMode.HTML,
                )
            return str(message.message_id)
        except Exception as e:
            logger.error("Telegram rating post error: %s", e)
            return None

    async def post_digest(
        self, promotions: List[Dict], image_path: str
    ) -> Optional[str]:
        caption = format_digest_text(promotions)

        try:
            with open(image_path, "rb") as photo:
                message = await self.bot.send_photo(
                    chat_id=self.channel_id,
                    photo=photo,
                    caption=caption,
                    parse_mode=ParseMode.HTML,
                )
            return str(message.message_id)
        except Exception as e:
            logger.error("Telegram digest post error: %s", e)
            return None
