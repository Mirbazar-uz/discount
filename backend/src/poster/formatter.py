from typing import Dict, List


def format_promotion_text(data: Dict) -> str:
    store = data.get("store", "").upper()
    title = data.get("title", "Aksiya")
    old_price = data.get("old_price")
    new_price = data.get("new_price")
    discount = data.get("discount_text", f"{data.get('discount_percent', 0)}%")
    deadline = data.get("deadline_text", "")
    source_url = data.get("source_url", "")

    text = f"<b>{store} AKSIYASI</b>\n\n"
    text += f"{title}\n"

    if old_price and new_price:
        text += f"<s>{old_price:,.0f}</s> → <b>{new_price:,.0f} so'm</b>\n"
    elif new_price:
        text += f"<b>{new_price:,.0f} so'm</b>\n"

    text += f"Chegirma: <b>{discount}</b>\n"

    if deadline:
        text += f"Muddat: {deadline}\n"

    if source_url:
        text += f"\n<a href='{source_url}'>Xarid qilish</a>\n"

    text += "\n━━━━━━━━━━━━━━━━━━━━━\n\n"
    text += "Kanalga obuna bo'ling: @mirbazar_uz\n\n"
    text += f"#aksiya #chegirma #{store.lower()}"

    return text


def format_rating_text(stores: List[Dict], period: str = "Haftalik") -> str:
    medals = ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8."]

    text = f"<b>{period.upper()} REYTING</b>\n\n"
    text += "Eng ko'p chegirma bergan do'konlar:\n\n"

    for i, store in enumerate(stores[:8]):
        medal = medals[i] if i < len(medals) else f"{i + 1}."
        name = store.get("name", "")
        count = store.get("count", 0)
        max_disc = store.get("max_discount", 0)
        text += f"{medal} <b>{name}</b> — {count} aksiya ({max_disc}% gacha)\n"

    if stores:
        winner = stores[0].get("name", "")
        text += f"\nBu hafta g'olib: <b>{winner}</b>\n"

    text += "\n━━━━━━━━━━━━━━━━━━━━━\n\n"
    text += "@mirbazar_uz — o'tkazib yubormang!\n\n"
    text += "#reyting #chegirma #aksiya"

    return text


def format_digest_text(promotions: List[Dict]) -> str:
    text = "<b>BUGUNGI TOP CHEGIRMALAR</b>\n\n"

    for i, promo in enumerate(promotions[:5], 1):
        title = promo.get("title", "")[:30]
        store = promo.get("store", "")
        discount = promo.get(
            "discount_text", f"{promo.get('discount_percent', 0)}%"
        )
        text += f"{i}. <b>{discount}</b> {title}\n   {store}\n\n"

    text += "━━━━━━━━━━━━━━━━━━━━━\n\n"
    text += "Batafsil: @mirbazar_uz\n"
    text += "Obuna bo'ling — o'tkazib yubormang!\n\n"
    text += "#top5 #chegirma #aksiya"

    return text


def format_promotion_instagram(data: Dict) -> str:
    store = data.get("store", "").upper()
    title = data.get("title", "Aksiya")
    old_price = data.get("old_price")
    new_price = data.get("new_price")
    discount = data.get("discount_text", f"{data.get('discount_percent', 0)}%")
    deadline = data.get("deadline_text", "")

    text = f"{discount} CHEGIRMA!\n\n"
    text += f"{title}\n\n"

    if old_price:
        text += f"Eski narx: {old_price:,.0f} so'm\n"
    if new_price:
        text += f"Yangi narx: {new_price:,.0f} so'm\n"

    text += f"Do'kon: {store}\n"

    if deadline:
        text += f"{deadline}\n"

    text += "\n━━━━━━━━━━━━━━━\n\n"
    text += "Chegirmalarni o'tkazib yubormang!\n"
    text += "Telegram: @mirbazar_uz (bio'da link)\n\n"
    text += "Saqlab qo'ying va do'stlaringizga ulashing!\n\n"
    text += f"#mirbazar #aksiya #chegirma #{store.lower()} "
    text += "#toshkent #uzbekistan #tekinaksiya #arzon"

    return text


def format_rating_instagram(
    stores: List[Dict], period: str = "Haftalik"
) -> str:
    medals = ["1.", "2.", "3.", "4.", "5."]

    text = f"{period.upper()} REYTING\n\n"
    text += "Eng ko'p chegirma bergan do'konlar:\n\n"

    for i, store in enumerate(stores[:5]):
        medal = medals[i]
        name = store.get("name", "")
        count = store.get("count", 0)
        text += f"{medal} {name} — {count} aksiya\n"

    text += "\n━━━━━━━━━━━━━━━\n\n"
    text += "Har hafta yangi reyting!\n"
    text += "Telegram: @mirbazar_uz\n\n"
    text += "#mirbazar #reyting #chegirma #aksiya #top5"

    return text
