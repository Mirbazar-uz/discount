PARSE_PROMOTION_PROMPT = """
Quyidagi Telegram post matnini tahlil qilib, JSON formatida ma'lumot qaytar.

MATN:
{text}

DO'KON: {store_name}
BUGUNGI SANA: {today}

Quyidagi JSON strukturada javob ber:

{{
    "is_promotion": true,
    "title": "Mahsulot nomi (qisqa, 50 belgigacha)",
    "description": "Qo'shimcha tavsif (100 belgigacha)",
    "old_price": 0,
    "new_price": 0,
    "discount_percent": 0,
    "discount_text": "",
    "category": "",
    "deadline": "",
    "deadline_text": "",
    "is_active": true,
    "confidence": 0.9
}}

MUHIM FILTRLASH QOIDALARI:
- Agar post HAQIQIY mahsulot chegirmasi/aksiyasi EMAS bo'lsa — "is_promotion": false, "confidence": 0.0 qaytar.
- Haqiqiy chegirma uchun ALBATTA mahsulot nomi VA narx pasaytirish yoki aniq chegirma foizi bo'lishi kerak.
- Quyidagilar chegirma EMAS: o'yinlar, viktorinalar, so'rovnomalar, maslahatlar, "top mahsulotlar" ro'yxati (narxsiz), yangiliklar, e'lonlar, suhbatlar, hazillar, tabriklar.
- Agar post faqat "arzon narxlar" yoki "foydali" desa lekin ANIQ narx/chegirma ko'rsatmasa — bu chegirma emas.

QOIDALAR:
1. Narxlarni so'mda yoz (million emas): 18500000, 5550000
2. Agar narx "mln" yoki "million" bo'lsa, 1000000 ga ko'paytir
3. deadline ni ISO formatda yoz: "2026-02-28"
4. Agar muddat o'tgan bo'lsa, is_active = false
5. Agar ma'lumot aniq bo'lmasa, null qo'y
6. Faqat JSON qaytar, boshqa matn yo'q
"""

PARSE_PROMOTION_WITH_IMAGE_PROMPT = """
Quyidagi Telegram post MATNINI VA RASMLARINI tahlil qilib, JSON formatida ma'lumot qaytar.

MUHIM: Rasmda ko'rsatilgan narxlar, chegirmalar, muddatlar va mahsulot nomlarini ham o'qi.
Agar matnda narx yo'q lekin rasmda bor bo'lsa — RASMDAGI narxni ishlatib ber.
Agar matn va rasmda ziddiyat bo'lsa — RASMDAGI ma'lumotga ishon.

MATN:
{text}

DO'KON: {store_name}
BUGUNGI SANA: {today}

Quyidagi JSON strukturada javob ber:

{{
    "is_promotion": true,
    "title": "Mahsulot nomi (qisqa, 50 belgigacha)",
    "description": "Qo'shimcha tavsif (100 belgigacha)",
    "old_price": 0,
    "new_price": 0,
    "discount_percent": 0,
    "discount_text": "",
    "category": "",
    "deadline": "",
    "deadline_text": "",
    "is_active": true,
    "confidence": 0.9
}}

MUHIM FILTRLASH QOIDALARI:
- Agar post HAQIQIY mahsulot chegirmasi/aksiyasi EMAS bo'lsa — "is_promotion": false, "confidence": 0.0 qaytar.
- Haqiqiy chegirma uchun ALBATTA mahsulot nomi VA narx pasaytirish yoki aniq chegirma foizi bo'lishi kerak.
- Quyidagilar chegirma EMAS: o'yinlar, viktorinalar, so'rovnomalar, maslahatlar, "top mahsulotlar" ro'yxati (narxsiz), yangiliklar, e'lonlar, suhbatlar, hazillar, tabriklar.
- Agar post faqat "arzon narxlar" yoki "foydali" desa lekin ANIQ narx/chegirma ko'rsatmasa — bu chegirma emas.

QOIDALAR:
1. Narxlarni so'mda yoz (million emas): 18500000, 5550000
2. Agar narx "mln" yoki "million" bo'lsa, 1000000 ga ko'paytir
3. deadline ni ISO formatda yoz: "2026-02-28"
4. Agar muddat o'tgan bo'lsa, is_active = false
5. Agar ma'lumot aniq bo'lmasa, null qo'y
6. Faqat JSON qaytar, boshqa matn yo'q
7. Rasmdan mahsulot nomini, modelini va rangini aniqlashga harakat qil
8. Rasmda narx chizilgan bo'lsa — bu eski narx (old_price), pastdagisi yangi narx (new_price)
"""

GENERATE_CAPTION_PROMPT = """
Quyidagi aksiya ma'lumotlari asosida Telegram post matni yoz:

Mahsulot: {title}
Do'kon: {store}
Eski narx: {old_price} so'm
Yangi narx: {new_price} so'm
Chegirma: {discount}
Muddat: {deadline}

Quyidagi formatda yoz:

🔥 [DO'KON] AKSIYASI

📱 [Mahsulot nomi]
💰 [eski narx] → [yangi narx] so'm
📉 Chegirma: [X]%
⏰ Muddat: [muddat]

🛒 Xarid: [link]

━━━━━━━━━━━━━━━━━━━━━

✅ Kanalga obuna bo'ling: @mirbazar_uz
🤖 Bot: @mirbazar_bot

#aksiya #chegirma #{store_tag}
"""
