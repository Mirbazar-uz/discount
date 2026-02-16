from PIL import Image, ImageDraw, ImageFont
from typing import Dict, List, Tuple
from pathlib import Path
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

COLORS = {
    "background": "#0f0f23",
    "card_bg": "#1a1a3e",
    "white": "#ffffff",
    "gray": "#9ca3af",
    "green": "#10b981",
    "red": "#ef4444",
    "orange": "#f97316",
    "gradient_start": "#7c3aed",
    "gradient_end": "#00d4ff",
}


def _hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


class ImageGenerator:
    def __init__(self, assets_path: str = "assets"):
        self.assets_path = Path(assets_path)
        self.fonts_path = self.assets_path / "fonts"
        self.output_path = Path("generated_images")
        self.output_path.mkdir(exist_ok=True)

        self.font_bold = self._load_font("Inter-Bold.ttf", 48)
        self.font_regular = self._load_font("Inter-Regular.ttf", 32)
        self.font_small = self._load_font("Inter-Regular.ttf", 24)
        self.font_large = self._load_font("Inter-Bold.ttf", 72)

    def _load_font(self, name: str, size: int) -> ImageFont.FreeTypeFont:
        font_path = self.fonts_path / name
        try:
            return ImageFont.truetype(str(font_path), size)
        except Exception:
            return ImageFont.load_default()

    def create_promotion_image(self, data: Dict) -> str:
        width, height = 1080, 1350

        img = Image.new("RGB", (width, height), _hex_to_rgb(COLORS["background"]))
        draw = ImageDraw.Draw(img)

        card_margin = 40
        card_top = 200
        card_height = 800
        draw.rounded_rectangle(
            (card_margin, card_top, width - card_margin, card_top + card_height),
            radius=30,
            fill=_hex_to_rgb(COLORS["card_bg"]),
        )

        discount_text = data.get(
            "discount_text", f"-{data.get('discount_percent', 0)}%"
        )
        badge_width = 200
        badge_height = 80
        badge_x = width - card_margin - badge_width - 20
        badge_y = card_top + 20

        draw.rounded_rectangle(
            (badge_x, badge_y, badge_x + badge_width, badge_y + badge_height),
            radius=40,
            fill=_hex_to_rgb(COLORS["red"]),
        )

        draw.text(
            (badge_x + badge_width // 2, badge_y + badge_height // 2),
            discount_text,
            font=self.font_bold,
            fill=_hex_to_rgb(COLORS["white"]),
            anchor="mm",
        )

        store_name = data.get("store", "").upper()
        draw.text(
            (card_margin + 30, card_top + 40),
            store_name,
            font=self.font_regular,
            fill=_hex_to_rgb(COLORS["gray"]),
        )

        title = data.get("title", "Aksiya")
        title_lines = self._wrap_text(title, self.font_bold, width - 2 * card_margin - 60)
        y_offset = card_top + 150
        for line in title_lines[:2]:
            draw.text(
                (card_margin + 30, y_offset),
                line,
                font=self.font_bold,
                fill=_hex_to_rgb(COLORS["white"]),
            )
            y_offset += 60

        y_offset += 50
        if data.get("old_price"):
            old_price_text = f"{data['old_price']:,.0f} so'm".replace(",", " ")
            draw.text(
                (card_margin + 30, y_offset),
                old_price_text,
                font=self.font_regular,
                fill=_hex_to_rgb(COLORS["gray"]),
            )
            bbox = draw.textbbox(
                (card_margin + 30, y_offset), old_price_text, font=self.font_regular
            )
            draw.line(
                [(bbox[0], bbox[1] + 20), (bbox[2], bbox[1] + 20)],
                fill=_hex_to_rgb(COLORS["gray"]),
                width=2,
            )
            y_offset += 50

        if data.get("new_price"):
            new_price_text = f"{data['new_price']:,.0f} so'm".replace(",", " ")
            draw.text(
                (card_margin + 30, y_offset),
                new_price_text,
                font=self.font_large,
                fill=_hex_to_rgb(COLORS["green"]),
            )
            y_offset += 100

        if data.get("deadline_text"):
            draw.text(
                (card_margin + 30, y_offset),
                data["deadline_text"],
                font=self.font_regular,
                fill=_hex_to_rgb(COLORS["orange"]),
            )

        branding_top = card_top + card_height + 50

        draw.text(
            (width // 2, branding_top),
            "MIRBAZAR.UZ",
            font=self.font_bold,
            fill=_hex_to_rgb(COLORS["white"]),
            anchor="mm",
        )

        draw.text(
            (width // 2, branding_top + 50),
            "Barcha chegirmalar bir joyda!",
            font=self.font_regular,
            fill=_hex_to_rgb(COLORS["gray"]),
            anchor="mm",
        )

        cta_y = branding_top + 120
        cta_texts = [
            "Kunlik yangi aksiyalar",
            "Eng arzon narxlar",
            "Bepul obuna",
        ]
        for i, cta in enumerate(cta_texts):
            draw.text(
                (width // 2, cta_y + i * 40),
                cta,
                font=self.font_small,
                fill=_hex_to_rgb(COLORS["gray"]),
                anchor="mm",
            )

        draw.text(
            (width // 2, height - 60),
            "@mirbazar_uz",
            font=self.font_bold,
            fill=_hex_to_rgb(COLORS["gradient_end"]),
            anchor="mm",
        )

        filename = f"promo_{data.get('store', 'unknown')}_{data.get('id', 'unknown')}.png"
        filepath = self.output_path / filename
        img.save(filepath, "PNG", quality=95)

        return str(filepath)

    def create_rating_image(
        self, stores_data: List[Dict], period: str = "Haftalik"
    ) -> str:
        width, height = 1080, 1350
        img = Image.new("RGB", (width, height), _hex_to_rgb(COLORS["background"]))
        draw = ImageDraw.Draw(img)

        draw.text(
            (width // 2, 80),
            f"{period.upper()} REYTING",
            font=self.font_large,
            fill=_hex_to_rgb(COLORS["white"]),
            anchor="mm",
        )

        draw.text(
            (width // 2, 150),
            datetime.now().strftime("%d.%m.%Y"),
            font=self.font_regular,
            fill=_hex_to_rgb(COLORS["gray"]),
            anchor="mm",
        )

        medals = ["1", "2", "3", "4", "5", "6", "7", "8"]
        y_start = 250
        row_height = 120

        max_count = (
            max(s.get("count", 0) for s in stores_data) if stores_data else 1
        )

        for i, store in enumerate(stores_data[:8]):
            y = y_start + i * row_height
            medal = medals[i] if i < len(medals) else f"{i + 1}"

            draw.text(
                (60, y + 20),
                f"{medal}. {store.get('name', '')}",
                font=self.font_bold,
                fill=_hex_to_rgb(COLORS["white"]),
            )

            bar_width = int((store.get("count", 0) / max_count) * 600)
            bar_x = 60
            bar_y = y + 70
            bar_h = 30

            draw.rounded_rectangle(
                (bar_x, bar_y, bar_x + 600, bar_y + bar_h),
                radius=15,
                fill=_hex_to_rgb("#2d2d5a"),
            )

            if bar_width > 0:
                store_color = store.get("color", COLORS["gradient_start"])
                draw.rounded_rectangle(
                    (bar_x, bar_y, bar_x + bar_width, bar_y + bar_h),
                    radius=15,
                    fill=_hex_to_rgb(store_color),
                )

            draw.text(
                (700, y + 50),
                f"{store.get('count', 0)} aksiya",
                font=self.font_regular,
                fill=_hex_to_rgb(COLORS["gray"]),
            )

            draw.text(
                (900, y + 50),
                f"{store.get('max_discount', 0)}%",
                font=self.font_regular,
                fill=_hex_to_rgb(COLORS["green"]),
            )

        draw.text(
            (width // 2, height - 120),
            "MIRBAZAR.UZ",
            font=self.font_bold,
            fill=_hex_to_rgb(COLORS["white"]),
            anchor="mm",
        )

        draw.text(
            (width // 2, height - 60),
            "@mirbazar_uz",
            font=self.font_regular,
            fill=_hex_to_rgb(COLORS["gradient_end"]),
            anchor="mm",
        )

        filename = f"rating_{period.lower()}_{datetime.now().strftime('%Y%m%d')}.png"
        filepath = self.output_path / filename
        img.save(filepath, "PNG", quality=95)

        return str(filepath)

    def create_digest_image(
        self, promotions: List[Dict], title: str = "TOP-5 CHEGIRMALAR"
    ) -> str:
        width, height = 1080, 1350
        img = Image.new("RGB", (width, height), _hex_to_rgb(COLORS["background"]))
        draw = ImageDraw.Draw(img)

        draw.text(
            (width // 2, 80),
            title,
            font=self.font_large,
            fill=_hex_to_rgb(COLORS["white"]),
            anchor="mm",
        )

        y_start = 200
        card_height = 180
        card_margin = 40

        for i, promo in enumerate(promotions[:5]):
            y = y_start + i * (card_height + 20)

            draw.rounded_rectangle(
                (card_margin, y, width - card_margin, y + card_height),
                radius=20,
                fill=_hex_to_rgb(COLORS["card_bg"]),
            )

            draw.text(
                (card_margin + 30, y + 30),
                f"{i + 1}.",
                font=self.font_bold,
                fill=_hex_to_rgb(COLORS["white"]),
            )

            discount = promo.get(
                "discount_text", f"-{promo.get('discount_percent', 0)}%"
            )
            draw.text(
                (width - card_margin - 30, y + 30),
                discount,
                font=self.font_bold,
                fill=_hex_to_rgb(COLORS["red"]),
                anchor="ra",
            )

            title_text = promo.get("title", "")[:40]
            draw.text(
                (card_margin + 100, y + 35),
                title_text,
                font=self.font_regular,
                fill=_hex_to_rgb(COLORS["white"]),
            )

            store = promo.get("store", "")
            draw.text(
                (card_margin + 100, y + 85),
                store,
                font=self.font_small,
                fill=_hex_to_rgb(COLORS["gray"]),
            )

            if promo.get("new_price"):
                price_text = f"{promo['new_price']:,.0f} so'm".replace(",", " ")
                draw.text(
                    (card_margin + 100, y + 125),
                    price_text,
                    font=self.font_regular,
                    fill=_hex_to_rgb(COLORS["green"]),
                )

        draw.text(
            (width // 2, height - 120),
            "MIRBAZAR.UZ",
            font=self.font_bold,
            fill=_hex_to_rgb(COLORS["white"]),
            anchor="mm",
        )

        draw.text(
            (width // 2, height - 60),
            "@mirbazar_uz",
            font=self.font_regular,
            fill=_hex_to_rgb(COLORS["gradient_end"]),
            anchor="mm",
        )

        filename = f"digest_{datetime.now().strftime('%Y%m%d_%H%M')}.png"
        filepath = self.output_path / filename
        img.save(filepath, "PNG", quality=95)

        return str(filepath)

    def _wrap_text(self, text: str, font: ImageFont, max_width: int) -> List[str]:
        words = text.split()
        lines: List[str] = []
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            bbox = font.getbbox(test_line)
            if bbox[2] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines
