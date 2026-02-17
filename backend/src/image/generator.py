from PIL import Image, ImageDraw, ImageFont
from typing import Dict, List, Tuple
from pathlib import Path
from datetime import datetime
import logging
import re

logger = logging.getLogger(__name__)

COLORS = {
    "bg": "#0a0a1a",
    "card": "#12122a",
    "card_border": "#1e1e45",
    "white": "#ffffff",
    "light": "#e2e8f0",
    "gray": "#94a3b8",
    "dark_gray": "#64748b",
    "green": "#22c55e",
    "green_bg": "#052e16",
    "red": "#ef4444",
    "red_bg": "#450a0a",
    "orange": "#f59e0b",
    "orange_bg": "#451a03",
    "purple": "#a855f7",
    "purple_bg": "#2e1065",
    "cyan": "#06b6d4",
    "accent": "#7c3aed",
    "accent2": "#06b6d4",
}


def _hex(color: str) -> Tuple[int, int, int]:
    c = color.lstrip("#")
    return tuple(int(c[i : i + 2], 16) for i in (0, 2, 4))


def _hex_a(color: str, alpha: int) -> Tuple[int, int, int, int]:
    c = color.lstrip("#")
    return tuple([int(c[i : i + 2], 16) for i in (0, 2, 4)] + [alpha])


def _price(n: float) -> str:
    return f"{n:,.0f}".replace(",", " ")


def _safe_filename(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)


def _draw_gradient_bar(draw: ImageDraw, x: int, y: int, w: int, h: int, r: int):
    left = _hex(COLORS["accent"])
    right = _hex(COLORS["accent2"])
    for i in range(w):
        ratio = i / max(w - 1, 1)
        c = tuple(int(left[j] + (right[j] - left[j]) * ratio) for j in range(3))
        if i < r or i > w - r:
            draw.line([(x + i, y + 1), (x + i, y + h - 2)], fill=c)
        else:
            draw.line([(x + i, y), (x + i, y + h - 1)], fill=c)


class ImageGenerator:
    def __init__(self, assets_path: str = "assets"):
        self.assets_path = Path(assets_path)
        self.fonts_path = self.assets_path / "fonts"
        self.output_path = Path("generated_images")
        self.output_path.mkdir(exist_ok=True)

        self.f_hero = self._load_font("Inter-Bold.ttf", 96)
        self.f_title = self._load_font("Inter-Bold.ttf", 64)
        self.f_subtitle = self._load_font("Inter-Bold.ttf", 52)
        self.f_price = self._load_font("Inter-Bold.ttf", 88)
        self.f_body = self._load_font("Inter-Bold.ttf", 42)
        self.f_label = self._load_font("Inter-Regular.ttf", 36)
        self.f_small = self._load_font("Inter-Regular.ttf", 32)
        self.f_brand = self._load_font("Inter-Bold.ttf", 56)
        self.f_tag = self._load_font("Inter-Bold.ttf", 44)

    def _load_font(self, name: str, size: int) -> ImageFont.FreeTypeFont:
        font_path = self.fonts_path / name
        try:
            return ImageFont.truetype(str(font_path), size)
        except Exception:
            return ImageFont.load_default()

    def create_promotion_image(self, data: Dict) -> str:
        W, H = 1080, 1350
        img = Image.new("RGBA", (W, H), _hex(COLORS["bg"]))
        draw = ImageDraw.Draw(img)

        _draw_gradient_bar(draw, 0, 0, W, 8, 0)

        store_name = data.get("store", "").upper()
        discount_text = data.get(
            "discount_text", f"-{data.get('discount_percent', 0)}%"
        )

        y = 50
        draw.text((60, y), store_name, font=self.f_body, fill=_hex(COLORS["gray"]))
        y += 70

        _draw_gradient_bar(draw, 60, y, 120, 6, 3)
        y += 40

        title = data.get("title", "Aksiya")
        lines = self._wrap_text(title, self.f_title, W - 120)
        for line in lines[:3]:
            draw.text((60, y), line, font=self.f_title, fill=_hex(COLORS["white"]))
            y += 80
        y += 30

        badge_w = min(len(discount_text) * 48 + 60, 500)
        badge_h = 100
        draw.rounded_rectangle(
            (60, y, 60 + badge_w, y + badge_h),
            radius=50,
            fill=_hex(COLORS["red_bg"]),
        )
        draw.rounded_rectangle(
            (60, y, 60 + badge_w, y + badge_h),
            radius=50,
            outline=_hex(COLORS["red"]),
            width=3,
        )
        draw.text(
            (60 + badge_w // 2, y + badge_h // 2),
            discount_text,
            font=self.f_subtitle,
            fill=_hex(COLORS["red"]),
            anchor="mm",
        )
        y += badge_h + 50

        card_top = y
        card_bottom = card_top + 380
        draw.rounded_rectangle(
            (40, card_top, W - 40, card_bottom),
            radius=30,
            fill=_hex(COLORS["card"]),
            outline=_hex(COLORS["card_border"]),
            width=2,
        )

        py = card_top + 40

        if data.get("old_price") and data.get("new_price"):
            draw.text(
                (80, py),
                "OLDINGI NARX",
                font=self.f_small,
                fill=_hex(COLORS["dark_gray"]),
            )
            py += 44
            old_text = f"{_price(data['old_price'])} so'm"
            draw.text(
                (80, py), old_text, font=self.f_body, fill=_hex(COLORS["dark_gray"])
            )
            bbox = draw.textbbox((80, py), old_text, font=self.f_body)
            draw.line(
                [(bbox[0], bbox[1] + 26), (bbox[2], bbox[1] + 26)],
                fill=_hex(COLORS["red"]),
                width=4,
            )
            py += 70

            draw.text(
                (80, py),
                "YANGI NARX",
                font=self.f_small,
                fill=_hex(COLORS["green"]),
            )
            py += 44
            new_text = f"{_price(data['new_price'])} so'm"
            draw.text(
                (80, py), new_text, font=self.f_price, fill=_hex(COLORS["green"])
            )
            py += 110

            savings = data["old_price"] - data["new_price"]
            if savings > 0:
                sav_text = f"Tejamkorlik: {_price(savings)} so'm"
                sav_w = len(sav_text) * 20 + 40
                draw.rounded_rectangle(
                    (80, py, 80 + sav_w, py + 52),
                    radius=26,
                    fill=_hex(COLORS["green_bg"]),
                )
                draw.text(
                    (100, py + 8),
                    sav_text,
                    font=self.f_small,
                    fill=_hex(COLORS["green"]),
                )

        elif data.get("new_price"):
            draw.text(
                (80, py), "NARXI", font=self.f_small, fill=_hex(COLORS["cyan"])
            )
            py += 44
            draw.text(
                (80, py),
                f"{_price(data['new_price'])} so'm",
                font=self.f_price,
                fill=_hex(COLORS["green"]),
            )

        else:
            draw.text(
                (W // 2, card_top + 190),
                "AKSIYA",
                font=self.f_hero,
                fill=_hex(COLORS["accent"]),
                anchor="mm",
            )

        y = card_bottom + 40

        if data.get("deadline_text"):
            dl_text = data["deadline_text"]
            dl_w = len(dl_text) * 22 + 80
            draw.rounded_rectangle(
                (60, y, 60 + dl_w, y + 64),
                radius=32,
                fill=_hex(COLORS["orange_bg"]),
            )
            draw.text(
                (60 + dl_w // 2, y + 32),
                dl_text,
                font=self.f_label,
                fill=_hex(COLORS["orange"]),
                anchor="mm",
            )
            y += 90

        footer_y = H - 260
        draw.line(
            [(60, footer_y), (W - 60, footer_y)],
            fill=_hex(COLORS["card_border"]),
            width=2,
        )

        draw.text(
            (W // 2, footer_y + 50),
            "MIRBAZAR.UZ",
            font=self.f_brand,
            fill=_hex(COLORS["white"]),
            anchor="mm",
        )
        draw.text(
            (W // 2, footer_y + 115),
            "Barcha chegirmalar bir joyda",
            font=self.f_label,
            fill=_hex(COLORS["gray"]),
            anchor="mm",
        )
        draw.text(
            (W // 2, footer_y + 180),
            "@mirbazar_uz",
            font=self.f_tag,
            fill=_hex(COLORS["cyan"]),
            anchor="mm",
        )

        _draw_gradient_bar(draw, 0, H - 8, W, 8, 0)

        safe_store = _safe_filename(data.get("store", "unknown"))
        filename = f"promo_{safe_store}_{data.get('id', 'unknown')}.png"
        filepath = self.output_path / filename
        img = img.convert("RGB")
        img.save(filepath, "PNG", quality=95)

        return str(filepath)

    def create_rating_image(
        self, stores_data: List[Dict], period: str = "Haftalik"
    ) -> str:
        W, H = 1080, 1350
        img = Image.new("RGB", (W, H), _hex(COLORS["bg"]))
        draw = ImageDraw.Draw(img)

        _draw_gradient_bar(draw, 0, 0, W, 8, 0)

        draw.text(
            (W // 2, 70),
            f"{period.upper()} REYTING",
            font=self.f_hero,
            fill=_hex(COLORS["white"]),
            anchor="mm",
        )
        draw.text(
            (W // 2, 140),
            datetime.now().strftime("%d.%m.%Y"),
            font=self.f_label,
            fill=_hex(COLORS["gray"]),
            anchor="mm",
        )

        y_start = 210
        row_h = 130
        max_count = max((s.get("count", 0) for s in stores_data), default=1) or 1

        top_colors = [COLORS["accent"], COLORS["cyan"], COLORS["orange"]]

        for i, store in enumerate(stores_data[:8]):
            y = y_start + i * row_h

            draw.rounded_rectangle(
                (40, y, W - 40, y + row_h - 12),
                radius=20,
                fill=_hex(COLORS["card"]),
            )

            pos_color = top_colors[i] if i < 3 else COLORS["gray"]
            draw.text(
                (80, y + (row_h - 12) // 2),
                f"{i + 1}",
                font=self.f_subtitle,
                fill=_hex(pos_color),
                anchor="lm",
            )

            name = store.get("name", "")
            draw.text(
                (140, y + 18),
                name,
                font=self.f_body,
                fill=_hex(COLORS["white"]),
            )

            bar_full = 500
            bar_w = max(int((store.get("count", 0) / max_count) * bar_full), 8)
            bar_y = y + 72
            draw.rounded_rectangle(
                (140, bar_y, 140 + bar_full, bar_y + 24),
                radius=12,
                fill=_hex("#1a1a40"),
            )
            if bar_w > 0:
                c = _hex(pos_color)
                draw.rounded_rectangle(
                    (140, bar_y, 140 + bar_w, bar_y + 24),
                    radius=12,
                    fill=c,
                )

            count = store.get("count", 0)
            draw.text(
                (700, y + 30),
                f"{count} ta",
                font=self.f_body,
                fill=_hex(COLORS["light"]),
            )

            max_disc = store.get("max_discount", 0)
            if max_disc:
                draw.text(
                    (W - 80, y + 30),
                    f"-{max_disc}%",
                    font=self.f_body,
                    fill=_hex(COLORS["green"]),
                    anchor="ra",
                )

        footer_y = H - 200
        draw.line(
            [(60, footer_y), (W - 60, footer_y)],
            fill=_hex(COLORS["card_border"]),
            width=2,
        )
        draw.text(
            (W // 2, footer_y + 50),
            "MIRBAZAR.UZ",
            font=self.f_brand,
            fill=_hex(COLORS["white"]),
            anchor="mm",
        )
        draw.text(
            (W // 2, footer_y + 120),
            "@mirbazar_uz",
            font=self.f_tag,
            fill=_hex(COLORS["cyan"]),
            anchor="mm",
        )

        _draw_gradient_bar(draw, 0, H - 8, W, 8, 0)

        filename = f"rating_{period.lower()}_{datetime.now().strftime('%Y%m%d')}.png"
        filepath = self.output_path / filename
        img.save(filepath, "PNG", quality=95)
        return str(filepath)

    def create_digest_image(
        self, promotions: List[Dict], title: str = "TOP-5 CHEGIRMALAR"
    ) -> str:
        W, H = 1080, 1350
        img = Image.new("RGB", (W, H), _hex(COLORS["bg"]))
        draw = ImageDraw.Draw(img)

        _draw_gradient_bar(draw, 0, 0, W, 8, 0)

        draw.text(
            (W // 2, 80),
            title,
            font=self.f_hero,
            fill=_hex(COLORS["white"]),
            anchor="mm",
        )
        draw.text(
            (W // 2, 150),
            datetime.now().strftime("%d.%m.%Y"),
            font=self.f_label,
            fill=_hex(COLORS["gray"]),
            anchor="mm",
        )

        y_start = 210
        card_h = 200
        margin = 40
        top_colors = [COLORS["accent"], COLORS["cyan"], COLORS["orange"]]

        for i, promo in enumerate(promotions[:5]):
            y = y_start + i * (card_h + 16)

            draw.rounded_rectangle(
                (margin, y, W - margin, y + card_h),
                radius=24,
                fill=_hex(COLORS["card"]),
            )

            pos_color = top_colors[i] if i < 3 else COLORS["gray"]
            draw.text(
                (margin + 35, y + card_h // 2),
                f"{i + 1}",
                font=self.f_subtitle,
                fill=_hex(pos_color),
                anchor="lm",
            )

            discount = promo.get(
                "discount_text", f"-{promo.get('discount_percent', 0)}%"
            )
            draw.text(
                (W - margin - 30, y + 30),
                discount,
                font=self.f_subtitle,
                fill=_hex(COLORS["red"]),
                anchor="ra",
            )

            title_text = promo.get("title", "")[:45]
            draw.text(
                (margin + 100, y + 25),
                title_text,
                font=self.f_body,
                fill=_hex(COLORS["white"]),
            )

            store = promo.get("store", "")
            draw.text(
                (margin + 100, y + 80),
                store,
                font=self.f_label,
                fill=_hex(COLORS["gray"]),
            )

            if promo.get("new_price"):
                price_text = f"{_price(promo['new_price'])} so'm"
                draw.text(
                    (margin + 100, y + 130),
                    price_text,
                    font=self.f_body,
                    fill=_hex(COLORS["green"]),
                )

        footer_y = H - 200
        draw.line(
            [(60, footer_y), (W - 60, footer_y)],
            fill=_hex(COLORS["card_border"]),
            width=2,
        )
        draw.text(
            (W // 2, footer_y + 50),
            "MIRBAZAR.UZ",
            font=self.f_brand,
            fill=_hex(COLORS["white"]),
            anchor="mm",
        )
        draw.text(
            (W // 2, footer_y + 120),
            "@mirbazar_uz",
            font=self.f_tag,
            fill=_hex(COLORS["cyan"]),
            anchor="mm",
        )

        _draw_gradient_bar(draw, 0, H - 8, W, 8, 0)

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
