from groq import Groq
from typing import Dict, Optional
import json
import logging
from datetime import datetime

from .prompts import PARSE_PROMOTION_PROMPT

logger = logging.getLogger(__name__)


class GroqClient:
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def parse_promotion(self, text: str, store_name: str) -> Optional[Dict]:
        today = datetime.now().strftime("%Y-%m-%d")

        prompt = PARSE_PROMOTION_PROMPT.format(
            text=text,
            store_name=store_name,
            today=today,
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Siz JSON formatida javob beradigan AI assistentsiz. "
                            "Faqat JSON qaytar, boshqa hech narsa yo'q."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.1,
                max_tokens=1000,
            )

            content = response.choices[0].message.content.strip()

            if content.startswith("```json"):
                content = content[7:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]

            return json.loads(content.strip())

        except Exception as e:
            logger.error("Groq parse error: %s", e)
            return None

    def check_is_promotion(self, text: str) -> bool:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "Faqat 'true' yoki 'false' javob ber.",
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Bu matn chegirma yoki aksiya haqidami?\n\n"
                            f"{text[:500]}"
                        ),
                    },
                ],
                temperature=0,
                max_tokens=10,
            )

            answer = response.choices[0].message.content.strip().lower()
            return answer == "true"

        except Exception:
            return False
