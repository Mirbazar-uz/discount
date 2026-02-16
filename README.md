# Mirbazar.uz — Barcha chegirmalar bir joyda

O'zbekistondagi do'konlarning aksiya va chegirmalarini avtomatik yig'ib, Telegram/Instagram kanallariga post qiladigan tizim.

## Arxitektura

```
Telegram kanallar → Scraper → Groq AI → Database → Image Gen → Poster → Telegram/Instagram
```

## Texnologiyalar

| Qism | Texnologiya |
|------|-------------|
| Backend | Python 3.11, FastAPI, SQLAlchemy |
| AI | Groq API (Llama 3.3 70B) |
| Database | PostgreSQL 15 |
| Frontend | Nuxt 3, TailwindCSS |
| Deploy | Docker, GitHub Actions |

## Development

Barcha build va run faqat serverda (CI/CD orqali).

```bash
# Kod yozish va push qilish
git add .
git commit -m "feat: yangi funksiya"
git push origin main
```

GitHub Actions avtomatik deploy qiladi.

## Server sozlash

`.env.example` dan `.env` yaratib, API kalitlarni to'ldiring.

## Litsenziya

Private project — Mirbazar.uz
