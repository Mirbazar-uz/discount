from PIL import Image, ImageDraw, ImageFont
from typing import Dict, List, Tuple
from pathlib import Path
from datetime import datetime
import logging
import re

logger = logging.getLogger(__name__)


def _rgb(c: str) -> Tuple[int, int, int]:
    h = c.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def _fmt(n) -> str:
    try:
        return f"{float(n):,.0f}".replace(",", " ")
    except (TypeError, ValueError):
        return str(n)


def _safe(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)


class ImageGenerator:

    BG1 = "#0B1120"
    BG2 = "#180D2B"

    CARD = "#131C30"
    EDGE = "#1E2E4D"

    WH = "#FFFFFF"
    LT = "#E2E8F0"
    MT = "#94A3B8"
    DK = "#64748B"

    RD = "#FF3B5C"
    GN = "#00D68F"
    BL = "#00B4D8"
    AM = "#FFBE0B"
    PR = "#8B5CF6"

    GN_BG = "#0D2A1F"
    GN_BD = "#1A4D38"
    AM_BG = "#2A2008"
    AM_BD = "#4A3818"
    PILL = "#182640"
    PILL_BD = "#283E60"

    GOLD = "#FFD700"
    SILVER = "#D1D5DB"
    BRONZE = "#E8A850"

    def __init__(self, assets_path: str = "assets"):
        self.assets_path = Path(assets_path)
        self.fonts_path = self.assets_path / "fonts"
        self.output_path = Path("generated_images")
        self.output_path.mkdir(exist_ok=True)

        self.f = {
            "mega":  self._font("Inter-Bold.ttf", 160),
            "hero":  self._font("Inter-Bold.ttf", 84),
            "disc2": self._font("Inter-Bold.ttf", 72),
            "title": self._font("Inter-Bold.ttf", 60),
            "price": self._font("Inter-Bold.ttf", 70),
            "old":   self._font("Inter-Bold.ttf", 40),
            "sub":   self._font("Inter-Bold.ttf", 44),
            "body":  self._font("Inter-Bold.ttf", 36),
            "label": self._font("Inter-Regular.ttf", 30),
            "small": self._font("Inter-Regular.ttf", 26),
            "brand": self._font("Inter-Bold.ttf", 42),
            "store": self._font("Inter-Bold.ttf", 34),
            "pos":   self._font("Inter-Bold.ttf", 48),
        }

    def _font(self, name: str, size: int):
        try:
            return ImageFont.truetype(str(self.fonts_path / name), size)
        except Exception:
            return ImageFont.load_default()

    def _tw(self, d, text: str, font) -> int:
        bb = d.textbbox((0, 0), text, font=font)
        return bb[2] - bb[0]

    # ── Background & Decorations ─────────────────────────

    def _bg(self, w: int, h: int) -> Image.Image:
        img = Image.new("RGB", (w, h))
        d = ImageDraw.Draw(img)
        c1, c2 = _rgb(self.BG1), _rgb(self.BG2)
        for y in range(h):
            t = y / h
            t = t * t * (3 - 2 * t)
            c = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
            d.line([(0, y), (w, y)], fill=c)
        return img

    def _accent(self, d, y: int, w: int, h: int = 5):
        a, b = _rgb(self.RD), _rgb(self.BL)
        for x in range(w):
            t = x / max(w - 1, 1)
            c = tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))
            d.line([(x, y), (x, y + h - 1)], fill=c)

    def _sep(self, d, y: int, w: int):
        d.line(
            [(w // 2 - 80, y), (w // 2 + 80, y)],
            fill=_rgb(self.EDGE), width=1,
        )

    def _corners(self, d, w: int, h: int):
        c = _rgb(self.EDGE)
        s, m = 25, 16
        d.line([(m, m), (m, m + s)], fill=c, width=2)
        d.line([(m, m), (m + s, m)], fill=c, width=2)
        d.line([(w - m, m), (w - m, m + s)], fill=c, width=2)
        d.line([(w - m, m), (w - m - s, m)], fill=c, width=2)
        d.line([(m, h - m), (m, h - m - s)], fill=c, width=2)
        d.line([(m, h - m), (m + s, h - m)], fill=c, width=2)
        d.line([(w - m, h - m), (w - m, h - m - s)], fill=c, width=2)
        d.line([(w - m, h - m), (w - m - s, h - m)], fill=c, width=2)

    def _footer(self, d, w: int, h: int):
        fy = h - 150
        self._accent(d, fy, w, 2)
        d.text(
            (w // 2, fy + 40), "MIRBAZAR.UZ",
            font=self.f["brand"], fill=_rgb(self.WH), anchor="mm",
        )
        d.text(
            (w // 2, fy + 90),
            "Barcha chegirmalar bir joyda  ·  @mirbazar_uz",
            font=self.f["small"], fill=_rgb(self.MT), anchor="mm",
        )

    def _best_disc_font(self, d, disc: str, w: int):
        max_w = w - 180
        for key, lh in [("mega", 170), ("hero", 100), ("disc2", 85)]:
            font = self.f[key]
            lines = self._wrap(disc, font, max_w)
            if len(lines) <= 2:
                return font, lines, lh
        return self.f["disc2"], self._wrap(disc, self.f["disc2"], max_w)[:2], 85

    # ── Promotion Image ──────────────────────────────────

    def create_promotion_image(self, data: Dict) -> str:
        W, H = 1080, 1350
        img = self._bg(W, H)
        d = ImageDraw.Draw(img)

        self._accent(d, 0, W)
        self._corners(d, W, H)

        store = data.get("store", "").upper()
        disc = data.get("discount_text", "")
        pct = data.get("discount_percent")
        if not disc and pct:
            disc = f"-{pct}%"
        title = data.get("title", "Aksiya")
        old_p, new_p = data.get("old_price"), data.get("new_price")
        dl = data.get("deadline_text")

        title_lines = self._wrap(title, self.f["title"], W - 140)[:3]

        if disc:
            disc_font, disc_lines, disc_lh = self._best_disc_font(d, disc, W)
        else:
            disc_font = self.f["hero"]
            disc_lines = ["AKSIYA"]
            disc_lh = 110

        # Calculate banner height
        banner_pad = 40
        banner_h = max(disc_lh * len(disc_lines) + banner_pad * 2, 220)

        # Vertical centering
        h_est = 0
        if store:
            h_est += 80
        h_est += banner_h + 30
        h_est += len(title_lines) * 75 + 40
        if old_p and new_p:
            h_est += 300
        elif new_p:
            h_est += 160
        if dl:
            h_est += 70

        area_top = 50
        area_bot = H - 170
        y = area_top + max((area_bot - area_top - h_est) // 2, 0)

        # ─ Store pill ─
        if store:
            sw = self._tw(d, store, self.f["store"]) + 48
            sx = (W - sw) // 2
            d.rounded_rectangle(
                [sx, y, sx + sw, y + 50], radius=25,
                fill=_rgb(self.PILL), outline=_rgb(self.PILL_BD), width=1,
            )
            d.text(
                (W // 2, y + 25), store,
                font=self.f["store"], fill=_rgb(self.LT), anchor="mm",
            )
            y += 80

        # ─ Discount Banner ─
        banner_color = self.RD if disc else self.PR
        d.rounded_rectangle(
            [60, y, W - 60, y + banner_h], radius=20,
            fill=_rgb(banner_color),
        )

        text_y = y + (banner_h - disc_lh * len(disc_lines)) // 2
        for line in disc_lines:
            d.text(
                (W // 2, text_y + disc_lh // 2), line,
                font=disc_font, fill=_rgb(self.WH), anchor="mm",
            )
            text_y += disc_lh

        y += banner_h + 30

        # ─ Title ─
        for line in title_lines:
            d.text(
                (W // 2, y + 37), line,
                font=self.f["title"], fill=_rgb(self.WH), anchor="mm",
            )
            y += 75
        y += 40

        # ─ Price card ─
        if old_p and new_p:
            ch = 290
            ct = y

            d.rounded_rectangle(
                [50, ct, W - 50, ct + ch], radius=22,
                fill=_rgb(self.CARD), outline=_rgb(self.EDGE), width=2,
            )

            py = ct + 28
            otxt = f"{_fmt(old_p)} so'm"
            d.text(
                (W // 2, py + 14), otxt,
                font=self.f["old"], fill=_rgb(self.DK), anchor="mm",
            )
            tw = self._tw(d, otxt, self.f["old"])
            d.line(
                [(W // 2 - tw // 2, py + 14), (W // 2 + tw // 2, py + 14)],
                fill=_rgb(self.RD), width=3,
            )
            py += 55

            d.text(
                (W // 2, py), "▼",
                font=self.f["small"], fill=_rgb(self.GN), anchor="mm",
            )
            py += 30

            ntxt = f"{_fmt(new_p)} so'm"
            d.text(
                (W // 2, py + 22), ntxt,
                font=self.f["price"], fill=_rgb(self.GN), anchor="mm",
            )
            py += 78

            sav = float(old_p) - float(new_p)
            if sav > 0:
                stxt = f"Tejamkorlik: {_fmt(sav)} so'm"
                stw = self._tw(d, stxt, self.f["label"]) + 36
                sx = (W - stw) // 2
                d.rounded_rectangle(
                    [sx, py, sx + stw, py + 42], radius=21,
                    fill=_rgb(self.GN_BG), outline=_rgb(self.GN_BD), width=1,
                )
                d.text(
                    (W // 2, py + 21), stxt,
                    font=self.f["label"], fill=_rgb(self.GN), anchor="mm",
                )

            y = ct + ch + 28

        elif new_p:
            ch = 130
            ct = y
            d.rounded_rectangle(
                [50, ct, W - 50, ct + ch], radius=22,
                fill=_rgb(self.CARD), outline=_rgb(self.EDGE), width=2,
            )
            d.text(
                (W // 2, ct + ch // 2), f"{_fmt(new_p)} so'm",
                font=self.f["price"], fill=_rgb(self.GN), anchor="mm",
            )
            y = ct + ch + 28

        # ─ Deadline ─
        if dl:
            dw = self._tw(d, dl, self.f["label"]) + 44
            dx = (W - dw) // 2
            d.rounded_rectangle(
                [dx, y, dx + dw, y + 48], radius=24,
                fill=_rgb(self.AM_BG), outline=_rgb(self.AM_BD), width=1,
            )
            d.text(
                (W // 2, y + 24), dl,
                font=self.f["label"], fill=_rgb(self.AM), anchor="mm",
            )

        self._footer(d, W, H)
        self._accent(d, H - 5, W)

        safe = _safe(data.get("store", "unknown"))
        fname = f"promo_{safe}_{data.get('id', 'x')}.png"
        path = self.output_path / fname
        img.save(path, "PNG", quality=95)
        return str(path)

    # ── Rating Image ─────────────────────────────────────

    def create_rating_image(
        self, stores_data: List[Dict], period: str = "Haftalik"
    ) -> str:
        W, H = 1080, 1350
        img = self._bg(W, H)
        d = ImageDraw.Draw(img)

        self._accent(d, 0, W)
        self._corners(d, W, H)

        d.text(
            (W // 2, 70), f"{period.upper()} REYTING",
            font=self.f["hero"], fill=_rgb(self.WH), anchor="mm",
        )
        d.text(
            (W // 2, 135), datetime.now().strftime("%d.%m.%Y"),
            font=self.f["label"], fill=_rgb(self.MT), anchor="mm",
        )

        y0 = 200
        rh = 120
        mx = max((s.get("count", 0) for s in stores_data), default=1) or 1
        medals = [self.GOLD, self.SILVER, self.BRONZE]

        for i, s in enumerate(stores_data[:8]):
            cy = y0 + i * rh

            d.rounded_rectangle(
                [45, cy, W - 45, cy + rh - 8], radius=16,
                fill=_rgb(self.CARD), outline=_rgb(self.EDGE), width=1,
            )

            pc = medals[i] if i < 3 else self.DK
            d.text(
                (82, cy + (rh - 8) // 2), f"{i + 1}",
                font=self.f["pos"], fill=_rgb(pc), anchor="lm",
            )

            d.text(
                (140, cy + 16), s.get("name", ""),
                font=self.f["body"], fill=_rgb(self.WH),
            )

            bw = max(int(s.get("count", 0) / mx * 460), 6)
            by = cy + 66
            d.rounded_rectangle(
                [140, by, 600, by + 18], radius=9,
                fill=_rgb("#0F172A"),
            )
            d.rounded_rectangle(
                [140, by, 140 + bw, by + 18], radius=9,
                fill=_rgb(pc),
            )

            d.text(
                (660, cy + 20), f"{s.get('count', 0)} ta",
                font=self.f["body"], fill=_rgb(self.LT),
            )

            md = s.get("max_discount", 0)
            if md:
                d.text(
                    (W - 75, cy + 20), f"-{md}%",
                    font=self.f["body"], fill=_rgb(self.GN), anchor="ra",
                )

        self._footer(d, W, H)
        self._accent(d, H - 5, W)

        fname = f"rating_{period.lower()}_{datetime.now().strftime('%Y%m%d')}.png"
        path = self.output_path / fname
        img.save(path, "PNG", quality=95)
        return str(path)

    # ── Digest Image ─────────────────────────────────────

    def create_digest_image(
        self, promotions: List[Dict], title: str = "TOP-5 CHEGIRMALAR"
    ) -> str:
        W, H = 1080, 1350
        img = self._bg(W, H)
        d = ImageDraw.Draw(img)

        self._accent(d, 0, W)
        self._corners(d, W, H)

        d.text(
            (W // 2, 75), title,
            font=self.f["hero"], fill=_rgb(self.WH), anchor="mm",
        )
        d.text(
            (W // 2, 140), datetime.now().strftime("%d.%m.%Y"),
            font=self.f["label"], fill=_rgb(self.MT), anchor="mm",
        )

        y0 = 200
        ch = 185
        medals = [self.GOLD, self.SILVER, self.BRONZE]

        for i, p in enumerate(promotions[:5]):
            cy = y0 + i * (ch + 12)

            d.rounded_rectangle(
                [45, cy, W - 45, cy + ch], radius=18,
                fill=_rgb(self.CARD), outline=_rgb(self.EDGE), width=1,
            )

            pc = medals[i] if i < 3 else self.DK
            d.text(
                (82, cy + ch // 2), f"{i + 1}",
                font=self.f["pos"], fill=_rgb(pc), anchor="lm",
            )

            disc = p.get(
                "discount_text", f"-{p.get('discount_percent', 0)}%"
            )
            d.text(
                (W - 75, cy + 24), disc,
                font=self.f["sub"], fill=_rgb(self.RD), anchor="ra",
            )

            d.text(
                (140, cy + 20), p.get("title", "")[:38],
                font=self.f["body"], fill=_rgb(self.WH),
            )

            d.text(
                (140, cy + 68), p.get("store", ""),
                font=self.f["label"], fill=_rgb(self.MT),
            )

            if p.get("new_price"):
                d.text(
                    (140, cy + 115), f"{_fmt(p['new_price'])} so'm",
                    font=self.f["body"], fill=_rgb(self.GN),
                )

        self._footer(d, W, H)
        self._accent(d, H - 5, W)

        fname = f"digest_{datetime.now().strftime('%Y%m%d_%H%M')}.png"
        path = self.output_path / fname
        img.save(path, "PNG", quality=95)
        return str(path)

    # ── Helpers ───────────────────────────────────────────

    def _wrap(self, text: str, font, max_w: int) -> List[str]:
        words = text.split()
        lines, cur = [], ""
        for w in words:
            test = f"{cur} {w}".strip()
            if font.getbbox(test)[2] <= max_w:
                cur = test
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines
