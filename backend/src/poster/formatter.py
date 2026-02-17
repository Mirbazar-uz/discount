from typing import Dict, List


def _format_number(n: float) -> str:
    return f"{n:,.0f}".replace(",", " ")


def format_promotion_text(data: Dict) -> str:
    store = data.get("store", "").upper()
    title = data.get("title", "Aksiya")
    old_price = data.get("old_price")
    new_price = data.get("new_price")
    discount = data.get("discount_text", "")
    discount_pct = data.get("discount_percent", 0)
    deadline = data.get("deadline_text", "")
    source_url = data.get("source_url", "")
    promo_id = data.get("id")

    if not discount and discount_pct:
        discount = f"-{discount_pct}%"

    text = f"\U0001f525 <b>{store} AKSIYASI</b>\n\n"
    text += f"\U0001f3f7 {title}\n\n"

    if old_price and new_price:
        savings = old_price - new_price
        text += f"\U0001f4b0 <s>{_format_number(old_price)}</s> \u2192 <b>{_format_number(new_price)} so'm</b>\n"
        text += f"\U0001f4c9 Tejamkorlik: <b>{_format_number(savings)} so'm</b>\n"
    elif new_price:
        text += f"\U0001f4b0 Narxi: <b>{_format_number(new_price)} so'm</b>\n"

    if discount:
        text += f"\U0001f3af Chegirma: <b>{discount}</b>\n"

    if deadline:
        text += f"\u23f0 Muddat: {deadline}\n"
        text += "\u26a1 Shoshiling, aksiya tugab qolishi mumkin!\n"

    text += "\n"

    if source_url:
        text += f"\U0001f6d2 <a href='{source_url}'>Xarid qilish</a>\n"

    if promo_id:
        text += f"\U0001f310 <a href='https://mirbazar.uz/promotion/{promo_id}'>Batafsil ko'rish</a>\n"

    text += "\n\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n"
    text += "\u2705 @mirbazar_uz \u2014 chegirmalarni o'tkazib yubormang!\n\n"
    text += f"#mirbazar #aksiya #chegirma #{store.lower().replace(' ', '_')}"

    return text


def format_rating_text(stores: List[Dict], period: str = "Haftalik") -> str:
    medals = ["\U0001f947", "\U0001f948", "\U0001f949", "4\ufe0f\u20e3", "5\ufe0f\u20e3", "6\ufe0f\u20e3", "7\ufe0f\u20e3", "8\ufe0f\u20e3"]

    text = f"\U0001f3c6 <b>{period.upper()} REYTING</b>\n\n"
    text += "Eng ko'p chegirma bergan do'konlar:\n\n"

    for i, store in enumerate(stores[:8]):
        medal = medals[i] if i < len(medals) else f"{i + 1}."
        name = store.get("name", "")
        count = store.get("count", 0)
        max_disc = store.get("max_discount", 0)
        text += f"{medal} <b>{name}</b>\n"
        text += f"     {count} ta aksiya \u2022 {max_disc}% gacha chegirma\n\n"

    if stores:
        winner = stores[0].get("name", "")
        text += f"\U0001f389 Bu hafta g'olib: <b>{winner}</b>! \U0001f389\n"

    text += "\n\U0001f310 mirbazar.uz \u2014 barcha chegirmalar bir joyda\n\n"
    text += "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n"
    text += "\u2705 @mirbazar_uz \u2014 o'tkazib yubormang!\n\n"
    text += "#mirbazar #reyting #chegirma #aksiya"

    return text


def format_digest_text(promotions: List[Dict]) -> str:
    medals = ["\U0001f947", "\U0001f948", "\U0001f949", "4\ufe0f\u20e3", "5\ufe0f\u20e3"]

    text = "\U0001f525 <b>BUGUNGI TOP CHEGIRMALAR</b> \U0001f525\n\n"

    for i, promo in enumerate(promotions[:5]):
        medal = medals[i] if i < len(medals) else f"{i + 1}."
        title = promo.get("title", "")[:40]
        store = promo.get("store", "")
        discount = promo.get(
            "discount_text", f"-{promo.get('discount_percent', 0)}%"
        )
        old_price = promo.get("old_price")
        new_price = promo.get("new_price")

        text += f"{medal} <b>{discount}</b> {title}\n"
        text += f"     \U0001f3ea {store}"
        if old_price and new_price:
            text += f" \u2022 {_format_number(new_price)} so'm"
        elif new_price:
            text += f" \u2022 {_format_number(new_price)} so'm"
        text += "\n\n"

    text += "\U0001f310 Barchasi: mirbazar.uz\n\n"
    text += "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n"
    text += "\u2705 @mirbazar_uz \u2014 har kuni eng zo'r chegirmalar!\n\n"
    text += "#mirbazar #top5 #chegirma #aksiya"

    return text


def format_promotion_instagram(data: Dict) -> str:
    store = data.get("store", "").upper()
    title = data.get("title", "Aksiya")
    old_price = data.get("old_price")
    new_price = data.get("new_price")
    discount = data.get("discount_text", "")
    discount_pct = data.get("discount_percent", 0)
    deadline = data.get("deadline_text", "")

    if not discount and discount_pct:
        discount = f"-{discount_pct}%"

    text = f"\U0001f525 {discount} CHEGIRMA! \U0001f525\n\n"
    text += f"\U0001f3f7 {title}\n\n"

    if old_price and new_price:
        savings = old_price - new_price
        text += f"\u274c Eski narx: {_format_number(old_price)} so'm\n"
        text += f"\u2705 Yangi narx: {_format_number(new_price)} so'm\n"
        text += f"\U0001f4b0 Tejamkorlik: {_format_number(savings)} so'm\n\n"
    elif old_price:
        text += f"Eski narx: {_format_number(old_price)} so'm\n\n"
    elif new_price:
        text += f"\u2705 Narxi: {_format_number(new_price)} so'm\n\n"

    text += f"\U0001f3ea Do'kon: {store}\n"

    if deadline:
        text += f"\u23f0 {deadline}\n"

    text += "\n\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n"
    text += "\U0001f4be Saqlab qo'ying!\n"
    text += "\U0001f4e4 Do'stlaringizga ulashing!\n"
    text += "\U0001f514 Obuna bo'ling \u2014 chegirmalarni o'tkazib yubormang!\n\n"
    text += "\U0001f310 mirbazar.uz \u2014 barcha chegirmalar bir joyda\n"
    text += "\U0001f4f1 Telegram: @mirbazar_uz\n\n"
    text += f"#mirbazar #aksiya #chegirma #{store.lower().replace(' ', '_')} "
    text += "#toshkent #uzbekistan #tekinaksiya #arzon #skidka #narx"

    return text


def format_rating_instagram(
    stores: List[Dict], period: str = "Haftalik"
) -> str:
    medals = ["\U0001f947", "\U0001f948", "\U0001f949", "4\ufe0f\u20e3", "5\ufe0f\u20e3"]

    text = f"\U0001f3c6 {period.upper()} REYTING \U0001f3c6\n\n"
    text += "Eng ko'p chegirma bergan do'konlar:\n\n"

    for i, store in enumerate(stores[:5]):
        medal = medals[i]
        name = store.get("name", "")
        count = store.get("count", 0)
        max_disc = store.get("max_discount", 0)
        text += f"{medal} {name} \u2014 {count} aksiya ({max_disc}% gacha)\n"

    if stores:
        winner = stores[0].get("name", "")
        text += f"\n\U0001f389 G'olib: {winner}! Tabriklaymiz! \U0001f389\n"

    text += "\n\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n"
    text += "\U0001f310 mirbazar.uz \u2014 barcha chegirmalar bir joyda\n"
    text += "\U0001f4f1 Telegram: @mirbazar_uz\n\n"
    text += "#mirbazar #reyting #chegirma #aksiya #top5 #uzbekistan"

    return text
