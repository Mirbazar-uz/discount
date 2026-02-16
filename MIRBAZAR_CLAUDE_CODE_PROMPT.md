# 🚀 MIRBAZAR — CHEGIRMA AGGREGATOR LOYIHASI

## CLAUDE CODE UCHUN TO'LIQ PROMPT

Salom Claude! Men Mirbazar loyihasini yaratmoqchiman. Bu O'zbekistondagi barcha do'konlarning aksiya va chegirmalarini bir joyga to'plovchi avtomatik tizim. Quyida to'liq texnik spetsifikatsiya berilgan. Shu asosida loyihani yozib ber.

---

## 🚨🚨🚨 QATTIQ QOIDA: LOCAL DA HECH NARSA BO'LMAYDI! 🚨🚨🚨

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ⛔⛔⛔ MUTLAQO TA'QIQLANGAN (LOCAL DA):                                ║
║                                                                           ║
║   ❌ python main.py                  — TA'QIQLANGAN                      ║
║   ❌ docker build                    — TA'QIQLANGAN                      ║
║   ❌ docker compose up               — TA'QIQLANGAN                      ║
║   ❌ docker run                      — TA'QIQLANGAN                      ║
║   ❌ pytest                          — TA'QIQLANGAN                      ║
║   ❌ pip install                     — TA'QIQLANGAN                      ║
║   ❌ npm run build                   — TA'QIQLANGAN                      ║
║   ❌ npm run dev                     — TA'QIQLANGAN                      ║
║   ❌ npm test                        — TA'QIQLANGAN                      ║
║   ❌ .env yaratish                   — TA'QIQLANGAN                      ║
║   ❌ Har qanday build/run/test       — TA'QIQLANGAN                      ║
║                                                                           ║
║   ✅✅✅ FAQAT RUXSAT BERILGAN:                                          ║
║                                                                           ║
║   ✅ Kod yozish (fayllar yaratish)                                       ║
║   ✅ git add .                                                            ║
║   ✅ git commit -m "..."                                                  ║
║   ✅ git push origin main                                                 ║
║                                                                           ║
║   🔄 QOLGAN HAMMASI SERVERDA AVTOMATIK:                                  ║
║                                                                           ║
║   🖥️  BUILD    → Serverda (CI/CD orqali)                                 ║
║   🖥️  RUN      → Serverda (CI/CD orqali)                                 ║
║   🖥️  TEST     → Serverda (CI/CD orqali)                                 ║
║   🖥️  DEPLOY   → Serverda (CI/CD orqali)                                 ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### ⚠️ AGAR CLAUDE CODE LOCAL DA BIROR NARSA RUN QILMOQCHI BO'LSA:

```
TO'XTAT! 

"Men local da hech narsa run qilmayman. 
Faqat kod yozaman va git push qilaman.
Barcha build, run, test serverda CI/CD orqali bo'ladi."
```

---

## 🔄 CI/CD WORKFLOW DIAGRAMMASI

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  👨‍💻 DEVELOPER (LOCAL)              ☁️  GITHUB                🖥️  SERVER    │
│  ──────────────────              ──────────                ──────────      │
│                                                                             │
│  ┌─────────────────┐            ┌─────────────────┐      ┌─────────────┐   │
│  │                 │   git      │                 │  SSH │             │   │
│  │   VS Code +     │──push────▶│  GitHub Actions │─────▶│  Docker     │   │
│  │   Claude Code   │            │                 │      │  Container  │   │
│  │                 │            │  ┌───────────┐  │      │             │   │
│  │  📝 Kod yozish  │            │  │  CI/CD    │  │      │  🔨 Build   │   │
│  │                 │            │  │  Pipeline │  │      │  🧪 Test    │   │
│  └─────────────────┘            │  └───────────┘  │      │  🚀 Run     │   │
│                                 │                 │      │             │   │
│        ❌ BUILD                 └─────────────────┘      └─────────────┘   │
│        ❌ RUN                                                   ✅         │
│        ❌ TEST                                              HAMMASI       │
│                                                             SHU YERDA     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚨🚨🚨 ENG MUHIM QOIDA — O'QI VA ESLAB QOL! 🚨🚨🚨

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ⛔⛔⛔ LOCAL DA HECH NARSA QILMA! ⛔⛔⛔                                    ║
║                                                                               ║
║   ❌ LOCAL DA BUILD QILMA          — SERVERDA BO'LADI                        ║
║   ❌ LOCAL DA RUN QILMA            — SERVERDA BO'LADI                        ║
║   ❌ LOCAL DA TEST QILMA           — SERVERDA BO'LADI                        ║
║   ❌ LOCAL DA DOCKER ISHLATMA      — SERVERDA BO'LADI                        ║
║   ❌ LOCAL DA pip install QILMA    — SERVERDA BO'LADI                        ║
║   ❌ LOCAL DA python ... QILMA     — SERVERDA BO'LADI                        ║
║   ❌ LOCAL DA npm/yarn ISHLATMA    — SERVERDA BO'LADI                        ║
║                                                                               ║
║   ✅ FAQAT KOD YOZ                                                           ║
║   ✅ FAQAT FAYLLARNI YARAT                                                   ║
║   ✅ FAQAT GIT PUSH QIL                                                      ║
║                                                                               ║
║   SABAB: Biz CI/CD pipeline ishlatamiz.                                      ║
║          Barcha build, test, run SERVERDA avtomatik bo'ladi.                 ║
║          GitHub ga push qilsang — tamom, serverda ishlaydi.                  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### ⚠️ AGAR CLAUDE CODE QUYIDAGILARNI QILMOQCHI BO'LSA — TO'XTAT:

```
❌ "Let me run this locally to test..."      — YO'Q! Faqat kod yoz
❌ "I'll build the Docker image..."          — YO'Q! Faqat kod yoz  
❌ "Let me install dependencies..."          — YO'Q! Faqat kod yoz
❌ "Running python script..."                — YO'Q! Faqat kod yoz
❌ "Testing the API..."                      — YO'Q! Faqat kod yoz
❌ "npm install..."                          — YO'Q! Faqat kod yoz
❌ "docker compose up..."                    — YO'Q! Faqat kod yoz
```

### ✅ CLAUDE CODE FAQAT SHU ISHLARNI QILSIN:

```
✅ Fayllarni yaratsin (create file)
✅ Kod yozsin
✅ Papka strukturasini tuzsin
✅ README, config fayllarni yozsin
✅ Keyin MEN git push qilaman — serverda ishlaydi
```

---

## 📋 LOYIHA HAQIDA

**Nomi:** Mirbazar.uz — Barcha chegirmalar bir joyda
**Maqsad:** O'zbekistondagi do'konlarning aksiyalarini avtomatik yig'ish, chiroyli rasm yaratish va Telegram/Instagram kanallariga post qilish
**Server:** 62.84.186.84 (Ubuntu, Docker)
**Domain:** mirbazar.uz

---

## 🏗️ ARXITEKTURA

```
┌─────────────────────────────────────────────────────────────────────┐
│                         MIRBAZAR PIPELINE                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────┐    ┌──────────────┐    ┌──────────────────┐   │
│  │  1. SCRAPER     │───▶│  2. GROQ AI  │───▶│  3. DATABASE     │   │
│  │  Telegram       │    │  Parse JSON  │    │  PostgreSQL      │   │
│  │  kanallardan    │    │  Aktuallik   │    │  Saqlash         │   │
│  └─────────────────┘    └──────────────┘    └──────────────────┘   │
│                                                      │              │
│                                                      ▼              │
│  ┌─────────────────┐    ┌──────────────┐    ┌──────────────────┐   │
│  │  6. SCHEDULER   │◀───│  5. POSTER   │◀───│  4. IMAGE GEN    │   │
│  │  APScheduler    │    │  Telegram    │    │  Pillow          │   │
│  │  Har 4 soatda   │    │  Instagram   │    │  Chiroyli rasm   │   │
│  └─────────────────┘    └──────────────┘    └──────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📁 PAPKA STRUKTURASI

```
mirbazar/
├── .github/
│   └── workflows/
│       └── deploy.yml              # CI/CD pipeline
├── docker-compose.yml
├── .env.example
├── README.md
│
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI entry point
│   │   ├── config.py                  # Sozlamalar
│   │   │
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py              # API endpoints
│   │   │   └── schemas.py             # Pydantic schemas
│   │   │
│   │   ├── scraper/
│   │   │   ├── __init__.py
│   │   │   ├── telegram_scraper.py    # Telegram kanallardan olish
│   │   │   ├── channels.py            # Kanallar ro'yxati
│   │   │   └── parser.py              # HTML parsing
│   │   │
│   │   ├── ai/
│   │   │   ├── __init__.py
│   │   │   ├── groq_client.py         # Groq API client
│   │   │   ├── prompts.py             # AI promptlar
│   │   │   └── validator.py           # Aktuallik tekshirish
│   │   │
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── models.py              # SQLAlchemy modellari
│   │   │   ├── connection.py          # DB ulanish
│   │   │   └── crud.py                # CRUD operatsiyalar
│   │   │
│   │   ├── image/
│   │   │   ├── __init__.py
│   │   │   ├── generator.py           # Rasm yaratish (Pillow)
│   │   │   └── templates/             # Rasm shablonlari
│   │   │
│   │   ├── poster/
│   │   │   ├── __init__.py
│   │   │   ├── telegram_poster.py     # Telegram kanalga post
│   │   │   ├── instagram_poster.py    # Instagram post
│   │   │   └── formatter.py           # Matn formatlash
│   │   │
│   │   ├── rating/
│   │   │   ├── __init__.py
│   │   │   └── calculator.py          # Reyting hisoblash
│   │   │
│   │   └── scheduler/
│   │       ├── __init__.py
│   │       └── jobs.py                # Jadval ishlari
│   │
│   ├── tests/                         # SERVERDA ISHLATILADI
│   │   ├── __init__.py
│   │   ├── test_scraper.py
│   │   ├── test_ai.py
│   │   └── test_api.py
│   │
│   └── assets/
│       ├── fonts/
│       └── logos/
│
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── nuxt.config.ts
│   ├── tailwind.config.js
│   ├── app.vue
│   │
│   ├── pages/
│   │   ├── index.vue                  # Bosh sahifa
│   │   ├── category/
│   │   │   └── [slug].vue             # Kategoriya sahifasi
│   │   ├── store/
│   │   │   └── [slug].vue             # Do'kon sahifasi
│   │   └── promotion/
│   │       └── [id].vue               # Aksiya sahifasi
│   │
│   ├── components/
│   │   ├── Header.vue
│   │   ├── Footer.vue
│   │   ├── HeroSection.vue
│   │   ├── PromotionCard.vue
│   │   ├── StoreCard.vue
│   │   ├── CategoryFilter.vue
│   │   ├── SearchBar.vue
│   │   ├── RatingBadge.vue
│   │   ├── CountdownTimer.vue
│   │   └── TelegramCTA.vue
│   │
│   ├── layouts/
│   │   └── default.vue
│   │
│   ├── composables/
│   │   ├── useApi.ts
│   │   └── usePromotion.ts
│   │
│   ├── assets/
│   │   └── css/
│   │       └── main.css
│   │
│   └── public/
│       ├── favicon.ico
│       └── og-image.png
│
└── nginx/
    └── nginx.conf
```

---

## 🎨 WEBSITE DIZAYNI (CREATIVE & MODERN)

### DIZAYN KONSEPTI

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   🎨 DIZAYN USLUBI:                                                        │
│                                                                             │
│   • Dark Mode (asosiy) + Light Mode                                        │
│   • Gradient backgrounds (Purple → Cyan)                                   │
│   • Glassmorphism kartalar                                                 │
│   • Smooth animations (Framer Motion style)                                │
│   • Neon glow effectlar                                                    │
│   • Modern typography (Inter font)                                         │
│   • Mobile-first responsive                                                │
│                                                                             │
│   🎯 ILHOM:                                                                │
│   • Linear.app                                                             │
│   • Vercel Dashboard                                                       │
│   • Stripe Homepage                                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### RANGLAR PALITRASI

```css
/* Asosiy ranglar */
--bg-primary: #0a0a0f;           /* Qop-qora fon */
--bg-secondary: #12121a;         /* Karta fon */
--bg-card: rgba(255,255,255,0.03); /* Glassmorphism */

/* Gradient */
--gradient-primary: linear-gradient(135deg, #7c3aed 0%, #00d4ff 100%);
--gradient-hover: linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%);

/* Aksent ranglar */
--accent-purple: #7c3aed;
--accent-cyan: #00d4ff;
--accent-green: #10b981;
--accent-red: #ef4444;
--accent-orange: #f97316;
--accent-yellow: #eab308;

/* Matn */
--text-primary: #ffffff;
--text-secondary: #9ca3af;
--text-muted: #6b7280;

/* Glow effectlar */
--glow-purple: 0 0 30px rgba(124,58,237,0.3);
--glow-cyan: 0 0 30px rgba(0,212,255,0.3);
```

### SAHIFALAR DIZAYNI

#### 🏠 BOSH SAHIFA (index.vue)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  🔥 MIRBAZAR                    [🔍 Qidirish...]    [Kategoriyalar ▾] │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ╔═══════════════════════════════════════════════════════════════════════╗  │
│  ║                                                                       ║  │
│  ║         🔥 BARCHA CHEGIRMALAR                                        ║  │
│  ║              BIR JOYDA                                               ║  │
│  ║                                                                       ║  │
│  ║    O'zbekistondagi eng yaxshi aksiyalarni o'tkazib yubormang!       ║  │
│  ║                                                                       ║  │
│  ║    ┌─────────────────────┐  ┌─────────────────────┐                  ║  │
│  ║    │  📱 Telegram        │  │  🔔 Bildirishnoma   │                  ║  │
│  ║    │  @mirbazar_uz       │  │  olish              │                  ║  │
│  ║    └─────────────────────┘  └─────────────────────┘                  ║  │
│  ║                                                                       ║  │
│  ║    📊 156 ta aksiya  •  12 ta do'kon  •  70% gacha chegirma         ║  │
│  ║                                                                       ║  │
│  ╚═══════════════════════════════════════════════════════════════════════╝  │
│                                                                             │
│  ┌─ 🏆 HAFTALIK REYTING ────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │   🥇 TEXNOMART     ████████████████████  23 aksiya  •  70% gacha    │  │
│  │   🥈 ASAXIY        ██████████████        18 aksiya  •  50% gacha    │  │
│  │   🥉 MEDIAPARK     ███████████           15 aksiya  •  45% gacha    │  │
│  │   4️⃣  GOODZONE     █████████             12 aksiya  •  40% gacha    │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌─ 🔥 ENG KATTA CHEGIRMALAR ───────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐            │  │
│  │  │ ╭───────────╮ │  │ ╭───────────╮ │  │ ╭───────────╮ │            │  │
│  │  │ │  -70%     │ │  │ │  -50%     │ │  │ │  -45%     │ │            │  │
│  │  │ ╰───────────╯ │  │ ╰───────────╯ │  │ ╰───────────╯ │            │  │
│  │  │               │  │               │  │               │            │  │
│  │  │ iPhone 15 Pro │  │ Samsung TV    │  │ MacBook Air   │            │  │
│  │  │               │  │               │  │               │            │  │
│  │  │ 18.5M → 5.5M  │  │ 12M → 6M      │  │ 15M → 8.2M    │            │  │
│  │  │               │  │               │  │               │            │  │
│  │  │ ⏰ 3 kun qoldi │  │ ⏰ 5 kun qoldi │  │ ⏰ 7 kun qoldi │            │  │
│  │  │ 📍 TEXNOMART  │  │ 📍 ASAXIY     │  │ 📍 MEDIAPARK  │            │  │
│  │  └───────────────┘  └───────────────┘  └───────────────┘            │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌─ 📱 KATEGORIYALAR ───────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │   ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐        │  │
│  │   │   📱   │  │   📺   │  │   💻   │  │   🍎   │  │   🏠   │        │  │
│  │   │Telefonlar│ │   TV   │  │ Laptop │  │ Oziq-  │  │Maishiy │        │  │
│  │   │  45 ta │  │  23 ta │  │  18 ta │  │ ovqat  │  │texnika │        │  │
│  │   └────────┘  └────────┘  └────────┘  └────────┘  └────────┘        │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌─ 🏪 DO'KONLAR ───────────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │  │
│  │   │ [LOGO]   │  │ [LOGO]   │  │ [LOGO]   │  │ [LOGO]   │            │  │
│  │   │TEXNOMART │  │ ASAXIY   │  │MEDIAPARK │  │ GOODZONE │            │  │
│  │   │ 23 aksiya│  │ 18 aksiya│  │ 15 aksiya│  │ 12 aksiya│            │  │
│  │   └──────────┘  └──────────┘  └──────────┘  └──────────┘            │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌─ 📲 TELEGRAM KANALGA QO'SHILING ─────────────────────────────────────┐  │
│  │                                                                       │  │
│  │   ╔═══════════════════════════════════════════════════════════════╗  │  │
│  │   ║                                                               ║  │  │
│  │   ║   📱 Chegirmalarni birinchi bo'lib bilmoqchimisiz?           ║  │  │
│  │   ║                                                               ║  │  │
│  │   ║   ┌─────────────────────────────────────────────────────┐    ║  │  │
│  │   ║   │   👉 @mirbazar_uz ga obuna bo'ling                  │    ║  │  │
│  │   ║   └─────────────────────────────────────────────────────┘    ║  │  │
│  │   ║                                                               ║  │  │
│  │   ║   ✅ Kunlik yangi aksiyalar                                  ║  │  │
│  │   ║   ✅ Eng arzon narxlar                                       ║  │  │
│  │   ║   ✅ Haftalik reyting                                        ║  │  │
│  │   ║                                                               ║  │  │
│  │   ╚═══════════════════════════════════════════════════════════════╝  │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  MIRBAZAR.UZ  •  Barcha chegirmalar bir joyda  •  © 2026            │  │
│  │  Telegram: @mirbazar_uz  •  Instagram: @mirbazar.uz                  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### KOMPONENTLAR DIZAYNI

#### PromotionCard.vue

```vue
<template>
  <div class="promotion-card group">
    <!-- Chegirma badge -->
    <div class="discount-badge">
      <span class="discount-text">-{{ promotion.discount_percent }}%</span>
    </div>
    
    <!-- Rasm -->
    <div class="image-container">
      <img :src="promotion.image_url" :alt="promotion.title" />
      <div class="image-overlay"></div>
    </div>
    
    <!-- Content -->
    <div class="card-content">
      <!-- Do'kon -->
      <div class="store-badge">
        <img :src="promotion.store.logo" class="store-logo" />
        <span>{{ promotion.store.name }}</span>
      </div>
      
      <!-- Title -->
      <h3 class="title">{{ promotion.title }}</h3>
      
      <!-- Narxlar -->
      <div class="prices">
        <span class="old-price">{{ formatPrice(promotion.old_price) }}</span>
        <span class="arrow">→</span>
        <span class="new-price">{{ formatPrice(promotion.new_price) }}</span>
      </div>
      
      <!-- Countdown -->
      <div class="countdown" v-if="promotion.deadline">
        <span class="countdown-icon">⏰</span>
        <CountdownTimer :deadline="promotion.deadline" />
      </div>
    </div>
    
    <!-- Hover glow effect -->
    <div class="glow-effect"></div>
  </div>
</template>

<style scoped>
.promotion-card {
  @apply relative bg-white/5 backdrop-blur-xl rounded-2xl overflow-hidden;
  @apply border border-white/10 transition-all duration-500;
  @apply hover:border-purple-500/50 hover:scale-[1.02];
  @apply hover:shadow-[0_0_40px_rgba(124,58,237,0.2)];
}

.discount-badge {
  @apply absolute top-4 right-4 z-10;
  @apply bg-gradient-to-r from-red-500 to-orange-500;
  @apply px-4 py-2 rounded-full;
  @apply font-bold text-white text-lg;
  @apply shadow-[0_0_20px_rgba(239,68,68,0.5)];
  animation: pulse 2s infinite;
}

.image-container {
  @apply relative h-48 overflow-hidden;
}

.image-overlay {
  @apply absolute inset-0;
  background: linear-gradient(to bottom, transparent 50%, rgba(10,10,15,0.9));
}

.card-content {
  @apply p-5 space-y-3;
}

.store-badge {
  @apply flex items-center gap-2 text-gray-400 text-sm;
}

.store-logo {
  @apply w-5 h-5 rounded-full;
}

.title {
  @apply text-white font-semibold text-lg line-clamp-2;
  @apply group-hover:text-transparent group-hover:bg-clip-text;
  @apply group-hover:bg-gradient-to-r group-hover:from-purple-400 group-hover:to-cyan-400;
}

.prices {
  @apply flex items-center gap-2;
}

.old-price {
  @apply text-gray-500 line-through text-sm;
}

.new-price {
  @apply text-green-400 font-bold text-xl;
}

.countdown {
  @apply flex items-center gap-2 text-orange-400 text-sm;
}

.glow-effect {
  @apply absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500;
  background: radial-gradient(circle at 50% 50%, rgba(124,58,237,0.1), transparent 70%);
  pointer-events: none;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}
</style>
```

#### HeroSection.vue

```vue
<template>
  <section class="hero">
    <!-- Animated background -->
    <div class="hero-bg">
      <div class="gradient-orb orb-1"></div>
      <div class="gradient-orb orb-2"></div>
      <div class="grid-pattern"></div>
    </div>
    
    <!-- Content -->
    <div class="hero-content">
      <div class="badge animate-float">
        <span class="badge-dot"></span>
        <span>{{ totalPromotions }} ta aktiv aksiya</span>
      </div>
      
      <h1 class="hero-title">
        <span class="gradient-text">Barcha chegirmalar</span>
        <br />
        bir joyda
      </h1>
      
      <p class="hero-subtitle">
        O'zbekistondagi eng yaxshi aksiyalarni o'tkazib yubormang!
        <br />
        Texnomart, Asaxiy, Mediapark va boshqa do'konlar.
      </p>
      
      <div class="hero-buttons">
        <a href="https://t.me/mirbazar_uz" class="btn-primary">
          <span>📱 Telegram kanal</span>
          <span class="btn-arrow">→</span>
        </a>
        <button class="btn-secondary">
          <span>🔔 Bildirishnoma olish</span>
        </button>
      </div>
      
      <div class="hero-stats">
        <div class="stat">
          <span class="stat-value">{{ totalPromotions }}</span>
          <span class="stat-label">Aksiyalar</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat">
          <span class="stat-value">{{ totalStores }}</span>
          <span class="stat-label">Do'konlar</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat">
          <span class="stat-value">{{ maxDiscount }}%</span>
          <span class="stat-label">Gacha chegirma</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  @apply relative min-h-[80vh] flex items-center justify-center overflow-hidden;
}

.hero-bg {
  @apply absolute inset-0;
}

.gradient-orb {
  @apply absolute rounded-full blur-3xl opacity-30;
}

.orb-1 {
  @apply w-96 h-96 bg-purple-500 -top-20 -left-20;
  animation: float 20s ease-in-out infinite;
}

.orb-2 {
  @apply w-80 h-80 bg-cyan-500 -bottom-20 -right-20;
  animation: float 15s ease-in-out infinite reverse;
}

.grid-pattern {
  @apply absolute inset-0 opacity-20;
  background-image: 
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 50px 50px;
}

.hero-content {
  @apply relative z-10 text-center max-w-4xl mx-auto px-6;
}

.badge {
  @apply inline-flex items-center gap-2 px-4 py-2 rounded-full;
  @apply bg-white/10 backdrop-blur-xl border border-white/20;
  @apply text-sm text-gray-300 mb-8;
}

.badge-dot {
  @apply w-2 h-2 bg-green-400 rounded-full;
  animation: pulse 2s infinite;
}

.hero-title {
  @apply text-5xl md:text-7xl font-bold text-white mb-6;
  line-height: 1.1;
}

.gradient-text {
  @apply bg-clip-text text-transparent;
  background-image: linear-gradient(135deg, #7c3aed 0%, #00d4ff 100%);
}

.hero-subtitle {
  @apply text-xl text-gray-400 mb-10 max-w-2xl mx-auto;
}

.hero-buttons {
  @apply flex flex-wrap justify-center gap-4 mb-12;
}

.btn-primary {
  @apply flex items-center gap-2 px-8 py-4 rounded-full;
  @apply bg-gradient-to-r from-purple-500 to-cyan-500;
  @apply text-white font-semibold text-lg;
  @apply hover:shadow-[0_0_30px_rgba(124,58,237,0.5)];
  @apply transition-all duration-300 hover:scale-105;
}

.btn-secondary {
  @apply flex items-center gap-2 px-8 py-4 rounded-full;
  @apply bg-white/10 backdrop-blur-xl border border-white/20;
  @apply text-white font-semibold text-lg;
  @apply hover:bg-white/20 transition-all duration-300;
}

.hero-stats {
  @apply flex justify-center items-center gap-8;
  @apply bg-white/5 backdrop-blur-xl rounded-2xl p-6;
  @apply border border-white/10;
}

.stat {
  @apply text-center;
}

.stat-value {
  @apply block text-3xl font-bold text-white;
}

.stat-label {
  @apply text-sm text-gray-400;
}

.stat-divider {
  @apply w-px h-12 bg-white/20;
}

@keyframes float {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(30px, 30px); }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}
</style>
```

### NUXT CONFIG

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  devtools: { enabled: false },
  
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/google-fonts',
    '@vueuse/nuxt',
    'nuxt-icon'
  ],
  
  css: ['~/assets/css/main.css'],
  
  googleFonts: {
    families: {
      Inter: [400, 500, 600, 700, 800]
    }
  },
  
  app: {
    head: {
      title: 'Mirbazar — Barcha chegirmalar bir joyda',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { 
          name: 'description', 
          content: "O'zbekistondagi eng yaxshi aksiyalar va chegirmalar. Texnomart, Asaxiy, Mediapark va boshqa do'konlarning barcha aksiyalari."
        },
        { property: 'og:title', content: 'Mirbazar — Barcha chegirmalar bir joyda' },
        { property: 'og:image', content: '/og-image.png' },
        { name: 'theme-color', content: '#0a0a0f' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  },
  
  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE_URL || 'http://localhost:8000'
    }
  },
  
  // SSR for SEO
  ssr: true,
  
  // Nitro config
  nitro: {
    preset: 'node-server'
  }
})
```

### TAILWIND CONFIG

```javascript
// tailwind.config.js
module.exports = {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './app.vue'
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#7c3aed',
          50: '#f5f3ff',
          100: '#ede9fe',
          500: '#7c3aed',
          600: '#6d28d9',
          700: '#5b21b6'
        },
        dark: {
          DEFAULT: '#0a0a0f',
          50: '#18181b',
          100: '#12121a',
          200: '#1a1a2e'
        },
        cyan: {
          DEFAULT: '#00d4ff',
          400: '#22d3ee',
          500: '#06b6d4'
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif']
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'pulse-glow': 'pulse-glow 2s ease-in-out infinite',
        'gradient': 'gradient 8s linear infinite'
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-20px)' }
        },
        'pulse-glow': {
          '0%, 100%': { boxShadow: '0 0 20px rgba(124,58,237,0.3)' },
          '50%': { boxShadow: '0 0 40px rgba(124,58,237,0.6)' }
        },
        gradient: {
          '0%, 100%': { backgroundPosition: '0% 50%' },
          '50%': { backgroundPosition: '100% 50%' }
        }
      },
      backdropBlur: {
        xs: '2px'
      }
    }
  },
  plugins: [
    require('@tailwindcss/line-clamp')
  ]
}
```

---

## 🔧 TEXNOLOGIYALAR

| Qism | Texnologiya | Versiya |
|------|-------------|---------|
| Backend | Python | 3.11+ |
| HTTP Client | httpx | latest |
| HTML Parsing | beautifulsoup4 | latest |
| AI | Groq API (Llama 3.3 70B) | latest |
| Database | PostgreSQL | 15+ |
| ORM | SQLAlchemy | 2.0+ |
| Image | Pillow | latest |
| Telegram | python-telegram-bot | 20+ |
| Instagram | instagrapi | latest |
| Scheduler | APScheduler | latest |
| Container | Docker + Docker Compose | latest |
| Env | python-dotenv | latest |

---

## 📦 REQUIREMENTS.TXT

```
httpx>=0.25.0
beautifulsoup4>=4.12.0
groq>=0.4.0
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
alembic>=1.13.0
pillow>=10.0.0
python-telegram-bot>=20.0
instagrapi>=2.0.0
apscheduler>=3.10.0
python-dotenv>=1.0.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
```

---

## 🔐 .ENV.EXAMPLE

```env
# Database
DATABASE_URL=postgresql://mirbazar:password@localhost:5432/mirbazar

# Groq AI
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx

# Telegram
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHANNEL_ID=@mirbazar_uz
TELEGRAM_ADMIN_ID=123456789

# Instagram
INSTAGRAM_USERNAME=mirbazar.uz
INSTAGRAM_PASSWORD=your_password

# App Settings
SCRAPE_INTERVAL_HOURS=4
POST_DELAY_SECONDS=60
MAX_POSTS_PER_DAY=20
DEBUG=false
```

---

## 💾 DATABASE MODELLARI

### src/database/models.py

```python
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class PromotionStatus(enum.Enum):
    ACTIVE = "active"          # Aktual
    EXPIRED = "expired"        # Tugagan (30 kun saqlanadi)
    DELETED = "deleted"        # O'chirilgan

class Store(Base):
    __tablename__ = "stores"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)           # Texnomart
    slug = Column(String(50), unique=True, nullable=False)  # texnomart
    telegram_channel = Column(String(100))               # @texnomart
    website = Column(String(200))                        # texnomart.uz
    logo_path = Column(String(200))                      # assets/logos/texnomart.png
    color = Column(String(7))                            # #3b82f6
    category = Column(String(50))                        # electronics / grocery
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    promotions = relationship("Promotion", back_populates="store")
    stats = relationship("StoreStats", back_populates="store")

class Promotion(Base):
    __tablename__ = "promotions"
    
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    
    # Asosiy ma'lumotlar
    title = Column(String(300), nullable=False)          # iPhone 15 Pro Max
    description = Column(Text)                           # Tavsif
    
    # Narxlar
    old_price = Column(Float)                            # 18500000
    new_price = Column(Float)                            # 5550000
    discount_percent = Column(Integer)                   # 70
    discount_text = Column(String(50))                   # "70%" yoki "1+1"
    
    # Kategoriya
    category = Column(String(50))                        # smartphones, tv, food
    
    # Muddatlar
    deadline = Column(DateTime)                          # Aksiya tugash sanasi
    deadline_text = Column(String(100))                  # "28-fevral gacha"
    
    # Manbalar
    source_url = Column(String(500))                     # Asl havola
    source_post_id = Column(String(100))                 # Telegram post ID
    image_url = Column(String(500))                      # Mahsulot rasmi (agar bor bo'lsa)
    
    # Holat
    status = Column(Enum(PromotionStatus), default=PromotionStatus.ACTIVE)
    
    # Vaqtlar
    created_at = Column(DateTime, default=datetime.utcnow)
    expired_at = Column(DateTime)                        # Qachon expired bo'ldi
    
    # Post holati
    posted_telegram = Column(Boolean, default=False)
    posted_instagram = Column(Boolean, default=False)
    telegram_post_id = Column(String(100))
    instagram_post_id = Column(String(100))
    
    # Generatsiya qilingan rasm
    generated_image_path = Column(String(300))
    
    store = relationship("Store", back_populates="promotions")

class StoreStats(Base):
    """Haftalik/oylik statistika"""
    __tablename__ = "store_stats"
    
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    
    period_type = Column(String(20))                     # weekly / monthly
    period_start = Column(DateTime)                      # Hafta/oy boshi
    period_end = Column(DateTime)                        # Hafta/oy oxiri
    
    total_promotions = Column(Integer, default=0)        # Aksiyalar soni
    max_discount = Column(Integer, default=0)            # Eng katta chegirma %
    avg_discount = Column(Float, default=0)              # O'rtacha chegirma %
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    store = relationship("Store", back_populates="stats")

class PostLog(Base):
    """Post tarixini saqlash"""
    __tablename__ = "post_logs"
    
    id = Column(Integer, primary_key=True)
    promotion_id = Column(Integer, ForeignKey("promotions.id"))
    
    platform = Column(String(20))                        # telegram / instagram
    post_type = Column(String(30))                       # single / digest / rating
    post_id = Column(String(100))                        # Platform post ID
    
    success = Column(Boolean, default=True)
    error_message = Column(Text)
    
    posted_at = Column(DateTime, default=datetime.utcnow)
```

---

## 🔍 SCRAPER

### src/scraper/channels.py

```python
TELEGRAM_CHANNELS = [
    {
        "slug": "texnomart",
        "name": "Texnomart",
        "channel": "texnomart",
        "url": "https://t.me/s/texnomart",
        "category": "electronics",
        "color": "#3b82f6"
    },
    {
        "slug": "asaxiy",
        "name": "Asaxiy",
        "channel": "asaxiyuz",
        "url": "https://t.me/s/asaxiyuz",
        "category": "electronics",
        "color": "#8b5cf6"
    },
    {
        "slug": "mediapark",
        "name": "Mediapark",
        "channel": "mediapark_uzb",
        "url": "https://t.me/s/mediapark_uzb",
        "category": "electronics",
        "color": "#ec4899"
    },
    {
        "slug": "goodzone",
        "name": "Goodzone",
        "channel": "goodzone_uzbekistan",
        "url": "https://t.me/s/goodzone_uzbekistan",
        "category": "electronics",
        "color": "#ef4444"
    },
    {
        "slug": "elmakon",
        "name": "Elmakon",
        "channel": "elmakonuz",
        "url": "https://t.me/s/elmakonuz",
        "category": "electronics",
        "color": "#f97316"
    },
    {
        "slug": "korzinka",
        "name": "Korzinka",
        "channel": "korzinka_uz",
        "url": "https://t.me/s/korzinka_uz",
        "category": "grocery",
        "color": "#22c55e"
    },
    {
        "slug": "makro",
        "name": "Makro",
        "channel": "makrosupermarket",
        "url": "https://t.me/s/makrosupermarket",
        "category": "grocery",
        "color": "#eab308"
    },
    {
        "slug": "havas",
        "name": "Havas",
        "channel": "havasuz",
        "url": "https://t.me/s/havasuz",
        "category": "grocery",
        "color": "#10b981"
    }
]
```

### src/scraper/telegram_scraper.py

```python
import httpx
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List, Dict, Optional
import re

class TelegramScraper:
    def __init__(self):
        self.client = httpx.Client(
            timeout=30,
            follow_redirects=True,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        )
    
    def fetch_channel_posts(self, channel_url: str, limit: int = 20) -> List[Dict]:
        """Telegram kanaldan postlarni olish"""
        try:
            response = self.client.get(channel_url)
            response.raise_for_status()
        except Exception as e:
            print(f"Error fetching {channel_url}: {e}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = []
        
        message_wraps = soup.find_all('div', class_='tgme_widget_message_wrap')
        
        for wrap in message_wraps[-limit:]:
            try:
                post = self._parse_message(wrap)
                if post:
                    posts.append(post)
            except Exception as e:
                continue
        
        return posts
    
    def _parse_message(self, wrap) -> Optional[Dict]:
        """Bitta postni parse qilish"""
        # Matn
        text_div = wrap.find('div', class_='tgme_widget_message_text')
        text = text_div.get_text(strip=True) if text_div else ""
        
        if not text:
            return None
        
        # HTML matn (linklar bilan)
        html_text = str(text_div) if text_div else ""
        
        # Sana
        time_tag = wrap.find('time')
        date_str = time_tag.get('datetime', '') if time_tag else ""
        
        # Post link
        link_tag = wrap.find('a', class_='tgme_widget_message_date')
        post_link = link_tag.get('href', '') if link_tag else ""
        
        # Post ID
        post_id = post_link.split('/')[-1] if post_link else ""
        
        # Rasm
        photo_wrap = wrap.find('a', class_='tgme_widget_message_photo_wrap')
        image_style = photo_wrap.get('style', '') if photo_wrap else ""
        image_url = self._extract_image_url(image_style)
        
        # Ko'rishlar
        views_span = wrap.find('span', class_='tgme_widget_message_views')
        views = views_span.get_text(strip=True) if views_span else "0"
        
        return {
            "text": text,
            "html_text": html_text,
            "date": date_str,
            "post_link": post_link,
            "post_id": post_id,
            "image_url": image_url,
            "views": views
        }
    
    def _extract_image_url(self, style: str) -> Optional[str]:
        """CSS style dan rasm URL olish"""
        match = re.search(r"url\('([^']+)'\)", style)
        return match.group(1) if match else None
    
    def is_promotion_post(self, text: str) -> bool:
        """Post aksiya haqidami tekshirish"""
        keywords = [
            'chegirma', 'aksiya', 'скидка', 'акция',
            '%', 'chegirmada', 'sovg\'a', 'подарок',
            'arzon', 'foydali', 'выгодн', 'bepul',
            'muddatli', 'nasiya', 'рассрочка',
            '1+1', 'cashback', 'keshbek', 'кэшбек',
            'sale', 'promo', 'maxsus narx', 'super narx'
        ]
        text_lower = text.lower()
        return any(kw in text_lower for kw in keywords)
    
    def close(self):
        self.client.close()
```

---

## 🤖 GROQ AI

### src/ai/groq_client.py

```python
from groq import Groq
from typing import Dict, Optional
import json
from datetime import datetime
from .prompts import PARSE_PROMOTION_PROMPT

class GroqClient:
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"
    
    def parse_promotion(self, text: str, store_name: str) -> Optional[Dict]:
        """Aksiya matni ni JSON ga parse qilish"""
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        prompt = PARSE_PROMOTION_PROMPT.format(
            text=text,
            store_name=store_name,
            today=today
        )
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Siz JSON formatida javob beradigan AI assistentsiz. Faqat JSON qaytar, boshqa hech narsa yo'q."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=1000
            )
            
            content = response.choices[0].message.content.strip()
            
            # JSON ni tozalash
            if content.startswith("```json"):
                content = content[7:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            
            return json.loads(content.strip())
            
        except Exception as e:
            print(f"Groq parse error: {e}")
            return None
    
    def check_is_promotion(self, text: str) -> bool:
        """Matn aksiya haqidami tekshirish"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Faqat 'true' yoki 'false' javob ber."},
                    {"role": "user", "content": f"Bu matn chegirma yoki aksiya haqidami?\n\n{text[:500]}"}
                ],
                temperature=0,
                max_tokens=10
            )
            
            answer = response.choices[0].message.content.strip().lower()
            return answer == "true"
            
        except Exception:
            return False
```

### src/ai/prompts.py

```python
PARSE_PROMOTION_PROMPT = """
Quyidagi Telegram post matnini tahlil qilib, JSON formatida ma'lumot qaytar.

MATN:
{text}

DO'KON: {store_name}
BUGUNGI SANA: {today}

Quyidagi JSON strukturada javob ber:

{{
    "title": "Mahsulot nomi (qisqa, 50 belgigacha)",
    "description": "Qo'shimcha tavsif (100 belgigacha)",
    "old_price": 0,           // Eski narx (so'mda, raqam, null agar yo'q bo'lsa)
    "new_price": 0,           // Yangi narx (so'mda, raqam, null agar yo'q bo'lsa)
    "discount_percent": 0,    // Chegirma foizi (raqam)
    "discount_text": "",      // "70%" yoki "1+1" yoki "Sovg'a"
    "category": "",           // smartphones, tv, laptop, appliances, food, other
    "deadline": "",           // ISO format: "2026-02-28" yoki null
    "deadline_text": "",      // "28-fevral gacha" yoki ""
    "is_active": true,        // Aktualmi? (deadline > bugun)
    "confidence": 0.9         // Ishonch darajasi 0-1
}}

QOIDALAR:
1. Narxlarni so'mda yoz (million emas): 18500000, 5550000
2. Agar narx "mln" yoki "million" bo'lsa, 1000000 ga ko'paytir
3. deadline ni ISO formatda yoz: "2026-02-28"
4. Agar muddat o'tgan bo'lsa, is_active = false
5. Agar ma'lumot aniq bo'lmasa, null qo'y
6. Faqat JSON qaytar, boshqa matn yo'q
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
```

### src/ai/validator.py

```python
from datetime import datetime, timedelta
from typing import Dict

class PromotionValidator:
    def __init__(self):
        self.today = datetime.now().date()
    
    def validate(self, data: Dict) -> Dict:
        """Aksiya ma'lumotlarini tekshirish va tozalash"""
        
        # Deadline tekshirish
        if data.get("deadline"):
            try:
                deadline = datetime.fromisoformat(data["deadline"]).date()
                data["is_active"] = deadline >= self.today
                
                # 30 kundan oshgan tugagan aksiyalarni o'chirish
                if not data["is_active"]:
                    days_expired = (self.today - deadline).days
                    data["should_delete"] = days_expired > 30
                else:
                    data["should_delete"] = False
                    
            except ValueError:
                data["deadline"] = None
                data["is_active"] = True
                data["should_delete"] = False
        else:
            # Deadline yo'q bo'lsa, post sanasiga qarab 7 kun aktual deb hisoblaymiz
            data["is_active"] = True
            data["should_delete"] = False
        
        # Narxlarni tekshirish
        if data.get("old_price") and data.get("new_price"):
            if data["old_price"] > 0 and data["new_price"] > 0:
                discount = ((data["old_price"] - data["new_price"]) / data["old_price"]) * 100
                data["discount_percent"] = round(discount)
        
        # Confidence tekshirish
        if data.get("confidence", 0) < 0.5:
            data["low_confidence"] = True
        
        return data
    
    def get_status(self, data: Dict) -> str:
        """Aksiya statusini aniqlash"""
        if data.get("should_delete"):
            return "deleted"
        elif not data.get("is_active"):
            return "expired"
        else:
            return "active"
```

---

## 🎨 IMAGE GENERATOR

### src/image/generator.py

```python
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, Optional, Tuple
import os
from pathlib import Path

class ImageGenerator:
    def __init__(self, assets_path: str = "assets"):
        self.assets_path = Path(assets_path)
        self.fonts_path = self.assets_path / "fonts"
        self.logos_path = self.assets_path / "logos"
        self.output_path = Path("generated_images")
        self.output_path.mkdir(exist_ok=True)
        
        # Shriftlar
        self.font_bold = self._load_font("Inter-Bold.ttf", 48)
        self.font_regular = self._load_font("Inter-Regular.ttf", 32)
        self.font_small = self._load_font("Inter-Regular.ttf", 24)
        self.font_large = self._load_font("Inter-Bold.ttf", 72)
        
        # Ranglar
        self.colors = {
            "background": "#0f0f23",
            "card_bg": "#1a1a3e",
            "white": "#ffffff",
            "gray": "#9ca3af",
            "green": "#10b981",
            "red": "#ef4444",
            "orange": "#f97316",
            "gradient_start": "#7c3aed",
            "gradient_end": "#00d4ff"
        }
    
    def _load_font(self, name: str, size: int) -> ImageFont.FreeTypeFont:
        """Shrift yuklash"""
        font_path = self.fonts_path / name
        try:
            return ImageFont.truetype(str(font_path), size)
        except:
            return ImageFont.load_default()
    
    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """HEX ni RGB ga aylantirish"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def create_promotion_image(self, data: Dict) -> str:
        """Aksiya uchun rasm yaratish"""
        
        width, height = 1080, 1350  # Instagram format
        
        # Yangi rasm
        img = Image.new('RGB', (width, height), self._hex_to_rgb(self.colors["background"]))
        draw = ImageDraw.Draw(img)
        
        # Karta fon
        card_margin = 40
        card_top = 200
        card_height = 800
        self._draw_rounded_rect(
            draw,
            (card_margin, card_top, width - card_margin, card_top + card_height),
            radius=30,
            fill=self._hex_to_rgb(self.colors["card_bg"])
        )
        
        # Chegirma badge
        discount_text = data.get("discount_text", f"-{data.get('discount_percent', 0)}%")
        badge_width = 200
        badge_height = 80
        badge_x = width - card_margin - badge_width - 20
        badge_y = card_top + 20
        
        self._draw_rounded_rect(
            draw,
            (badge_x, badge_y, badge_x + badge_width, badge_y + badge_height),
            radius=40,
            fill=self._hex_to_rgb(self.colors["red"])
        )
        
        # Chegirma matni
        draw.text(
            (badge_x + badge_width // 2, badge_y + badge_height // 2),
            discount_text,
            font=self.font_bold,
            fill=self._hex_to_rgb(self.colors["white"]),
            anchor="mm"
        )
        
        # Do'kon nomi
        store_name = data.get("store", "").upper()
        draw.text(
            (card_margin + 30, card_top + 40),
            f"📍 {store_name}",
            font=self.font_regular,
            fill=self._hex_to_rgb(self.colors["gray"])
        )
        
        # Mahsulot nomi
        title = data.get("title", "Aksiya")
        # Matnni wrap qilish
        title_lines = self._wrap_text(title, self.font_bold, width - 2 * card_margin - 60)
        y_offset = card_top + 150
        for line in title_lines[:2]:  # Max 2 qator
            draw.text(
                (card_margin + 30, y_offset),
                line,
                font=self.font_bold,
                fill=self._hex_to_rgb(self.colors["white"])
            )
            y_offset += 60
        
        # Narxlar
        y_offset += 50
        if data.get("old_price"):
            old_price_text = f"{data['old_price']:,.0f} so'm".replace(",", " ")
            draw.text(
                (card_margin + 30, y_offset),
                old_price_text,
                font=self.font_regular,
                fill=self._hex_to_rgb(self.colors["gray"])
            )
            # Chiziq
            bbox = draw.textbbox((card_margin + 30, y_offset), old_price_text, font=self.font_regular)
            draw.line(
                [(bbox[0], bbox[1] + 20), (bbox[2], bbox[1] + 20)],
                fill=self._hex_to_rgb(self.colors["gray"]),
                width=2
            )
            y_offset += 50
        
        if data.get("new_price"):
            new_price_text = f"{data['new_price']:,.0f} so'm".replace(",", " ")
            draw.text(
                (card_margin + 30, y_offset),
                new_price_text,
                font=self.font_large,
                fill=self._hex_to_rgb(self.colors["green"])
            )
            y_offset += 100
        
        # Muddat
        if data.get("deadline_text"):
            draw.text(
                (card_margin + 30, y_offset),
                f"⏰ {data['deadline_text']}",
                font=self.font_regular,
                fill=self._hex_to_rgb(self.colors["orange"])
            )
        
        # Mirbazar branding (pastda)
        branding_top = card_top + card_height + 50
        
        # Mirbazar logo/text
        draw.text(
            (width // 2, branding_top),
            "MIRBAZAR.UZ",
            font=self.font_bold,
            fill=self._hex_to_rgb(self.colors["white"]),
            anchor="mm"
        )
        
        draw.text(
            (width // 2, branding_top + 50),
            "Barcha chegirmalar bir joyda!",
            font=self.font_regular,
            fill=self._hex_to_rgb(self.colors["gray"]),
            anchor="mm"
        )
        
        # CTA
        cta_y = branding_top + 120
        cta_texts = [
            "✅ Kunlik yangi aksiyalar",
            "✅ Eng arzon narxlar",
            "✅ Bepul obuna"
        ]
        for i, cta in enumerate(cta_texts):
            draw.text(
                (width // 2, cta_y + i * 40),
                cta,
                font=self.font_small,
                fill=self._hex_to_rgb(self.colors["gray"]),
                anchor="mm"
            )
        
        # Telegram handle
        draw.text(
            (width // 2, height - 60),
            "👉 @mirbazar_uz",
            font=self.font_bold,
            fill=self._hex_to_rgb(self.colors["gradient_end"]),
            anchor="mm"
        )
        
        # Saqlash
        filename = f"promo_{data.get('store', 'unknown')}_{data.get('id', 'unknown')}.png"
        filepath = self.output_path / filename
        img.save(filepath, "PNG", quality=95)
        
        return str(filepath)
    
    def create_rating_image(self, stores_data: list, period: str = "Haftalik") -> str:
        """Reyting rasmi yaratish"""
        
        width, height = 1080, 1350
        img = Image.new('RGB', (width, height), self._hex_to_rgb(self.colors["background"]))
        draw = ImageDraw.Draw(img)
        
        # Sarlavha
        draw.text(
            (width // 2, 80),
            f"🏆 {period.upper()} REYTING",
            font=self.font_large,
            fill=self._hex_to_rgb(self.colors["white"]),
            anchor="mm"
        )
        
        # Sana
        from datetime import datetime
        draw.text(
            (width // 2, 150),
            datetime.now().strftime("%d.%m.%Y"),
            font=self.font_regular,
            fill=self._hex_to_rgb(self.colors["gray"]),
            anchor="mm"
        )
        
        # Reyting ro'yxati
        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]
        y_start = 250
        row_height = 120
        
        max_count = max([s.get("count", 0) for s in stores_data]) if stores_data else 1
        
        for i, store in enumerate(stores_data[:8]):
            y = y_start + i * row_height
            medal = medals[i] if i < len(medals) else f"{i+1}."
            
            # Medal va nom
            draw.text(
                (60, y + 20),
                f"{medal} {store.get('name', '')}",
                font=self.font_bold,
                fill=self._hex_to_rgb(self.colors["white"])
            )
            
            # Bar
            bar_width = int((store.get("count", 0) / max_count) * 600)
            bar_x = 60
            bar_y = y + 70
            bar_height = 30
            
            # Bar fon
            self._draw_rounded_rect(
                draw,
                (bar_x, bar_y, bar_x + 600, bar_y + bar_height),
                radius=15,
                fill=self._hex_to_rgb("#2d2d5a")
            )
            
            # Bar qiymati
            if bar_width > 0:
                store_color = store.get("color", self.colors["gradient_start"])
                self._draw_rounded_rect(
                    draw,
                    (bar_x, bar_y, bar_x + bar_width, bar_y + bar_height),
                    radius=15,
                    fill=self._hex_to_rgb(store_color)
                )
            
            # Aksiyalar soni
            draw.text(
                (700, y + 50),
                f"{store.get('count', 0)} aksiya",
                font=self.font_regular,
                fill=self._hex_to_rgb(self.colors["gray"])
            )
            
            # Max chegirma
            draw.text(
                (900, y + 50),
                f"{store.get('max_discount', 0)}%",
                font=self.font_regular,
                fill=self._hex_to_rgb(self.colors["green"])
            )
        
        # Mirbazar branding
        draw.text(
            (width // 2, height - 120),
            "MIRBAZAR.UZ",
            font=self.font_bold,
            fill=self._hex_to_rgb(self.colors["white"]),
            anchor="mm"
        )
        
        draw.text(
            (width // 2, height - 60),
            "👉 @mirbazar_uz",
            font=self.font_regular,
            fill=self._hex_to_rgb(self.colors["gradient_end"]),
            anchor="mm"
        )
        
        # Saqlash
        filename = f"rating_{period.lower()}_{datetime.now().strftime('%Y%m%d')}.png"
        filepath = self.output_path / filename
        img.save(filepath, "PNG", quality=95)
        
        return str(filepath)
    
    def create_digest_image(self, promotions: list, title: str = "TOP-5 CHEGIRMALAR") -> str:
        """Kunlik digest rasmi"""
        
        width, height = 1080, 1350
        img = Image.new('RGB', (width, height), self._hex_to_rgb(self.colors["background"]))
        draw = ImageDraw.Draw(img)
        
        # Sarlavha
        draw.text(
            (width // 2, 80),
            f"🔥 {title}",
            font=self.font_large,
            fill=self._hex_to_rgb(self.colors["white"]),
            anchor="mm"
        )
        
        # Aksiyalar ro'yxati
        y_start = 200
        card_height = 180
        card_margin = 40
        
        for i, promo in enumerate(promotions[:5]):
            y = y_start + i * (card_height + 20)
            
            # Karta fon
            self._draw_rounded_rect(
                draw,
                (card_margin, y, width - card_margin, y + card_height),
                radius=20,
                fill=self._hex_to_rgb(self.colors["card_bg"])
            )
            
            # Raqam
            draw.text(
                (card_margin + 30, y + 30),
                f"{i + 1}️⃣",
                font=self.font_bold,
                fill=self._hex_to_rgb(self.colors["white"])
            )
            
            # Chegirma
            discount = promo.get("discount_text", f"-{promo.get('discount_percent', 0)}%")
            draw.text(
                (width - card_margin - 30, y + 30),
                discount,
                font=self.font_bold,
                fill=self._hex_to_rgb(self.colors["red"]),
                anchor="ra"
            )
            
            # Mahsulot nomi
            title_text = promo.get("title", "")[:40]
            draw.text(
                (card_margin + 100, y + 35),
                title_text,
                font=self.font_regular,
                fill=self._hex_to_rgb(self.colors["white"])
            )
            
            # Do'kon
            store = promo.get("store", "")
            draw.text(
                (card_margin + 100, y + 85),
                f"📍 {store}",
                font=self.font_small,
                fill=self._hex_to_rgb(self.colors["gray"])
            )
            
            # Narx
            if promo.get("new_price"):
                price_text = f"{promo['new_price']:,.0f} so'm".replace(",", " ")
                draw.text(
                    (card_margin + 100, y + 125),
                    price_text,
                    font=self.font_regular,
                    fill=self._hex_to_rgb(self.colors["green"])
                )
        
        # Mirbazar branding
        draw.text(
            (width // 2, height - 120),
            "MIRBAZAR.UZ",
            font=self.font_bold,
            fill=self._hex_to_rgb(self.colors["white"]),
            anchor="mm"
        )
        
        draw.text(
            (width // 2, height - 60),
            "👉 @mirbazar_uz",
            font=self.font_regular,
            fill=self._hex_to_rgb(self.colors["gradient_end"]),
            anchor="mm"
        )
        
        # Saqlash
        from datetime import datetime
        filename = f"digest_{datetime.now().strftime('%Y%m%d_%H%M')}.png"
        filepath = self.output_path / filename
        img.save(filepath, "PNG", quality=95)
        
        return str(filepath)
    
    def _draw_rounded_rect(self, draw: ImageDraw, coords: tuple, radius: int, fill: tuple):
        """Yumaloq burchakli to'rtburchak chizish"""
        x1, y1, x2, y2 = coords
        
        draw.rounded_rectangle(coords, radius=radius, fill=fill)
    
    def _wrap_text(self, text: str, font: ImageFont, max_width: int) -> list:
        """Matnni wrap qilish"""
        words = text.split()
        lines = []
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
```

---

## 📱 POSTER

### src/poster/telegram_poster.py

```python
from telegram import Bot, InputMediaPhoto
from telegram.constants import ParseMode
import asyncio
from typing import Optional
from .formatter import format_promotion_text, format_rating_text, format_digest_text

class TelegramPoster:
    def __init__(self, token: str, channel_id: str):
        self.bot = Bot(token=token)
        self.channel_id = channel_id
    
    async def post_promotion(self, data: dict, image_path: str) -> Optional[str]:
        """Aksiya postini yuborish"""
        caption = format_promotion_text(data)
        
        try:
            with open(image_path, 'rb') as photo:
                message = await self.bot.send_photo(
                    chat_id=self.channel_id,
                    photo=photo,
                    caption=caption,
                    parse_mode=ParseMode.HTML
                )
            return str(message.message_id)
        except Exception as e:
            print(f"Telegram post error: {e}")
            return None
    
    async def post_rating(self, stores_data: list, image_path: str, period: str = "Haftalik") -> Optional[str]:
        """Reyting postini yuborish"""
        caption = format_rating_text(stores_data, period)
        
        try:
            with open(image_path, 'rb') as photo:
                message = await self.bot.send_photo(
                    chat_id=self.channel_id,
                    photo=photo,
                    caption=caption,
                    parse_mode=ParseMode.HTML
                )
            return str(message.message_id)
        except Exception as e:
            print(f"Telegram rating post error: {e}")
            return None
    
    async def post_digest(self, promotions: list, image_path: str) -> Optional[str]:
        """Kunlik digest postini yuborish"""
        caption = format_digest_text(promotions)
        
        try:
            with open(image_path, 'rb') as photo:
                message = await self.bot.send_photo(
                    chat_id=self.channel_id,
                    photo=photo,
                    caption=caption,
                    parse_mode=ParseMode.HTML
                )
            return str(message.message_id)
        except Exception as e:
            print(f"Telegram digest post error: {e}")
            return None
```

### src/poster/instagram_poster.py

```python
from instagrapi import Client
from typing import Optional
from .formatter import format_promotion_instagram, format_rating_instagram

class InstagramPoster:
    def __init__(self, username: str, password: str):
        self.client = Client()
        self.username = username
        self.password = password
        self._logged_in = False
    
    def login(self):
        """Instagram ga kirish"""
        if not self._logged_in:
            try:
                self.client.login(self.username, self.password)
                self._logged_in = True
            except Exception as e:
                print(f"Instagram login error: {e}")
                raise
    
    def post_promotion(self, data: dict, image_path: str) -> Optional[str]:
        """Aksiya postini Instagram ga yuborish"""
        self.login()
        caption = format_promotion_instagram(data)
        
        try:
            media = self.client.photo_upload(image_path, caption)
            return media.pk
        except Exception as e:
            print(f"Instagram post error: {e}")
            return None
    
    def post_rating(self, stores_data: list, image_path: str, period: str = "Haftalik") -> Optional[str]:
        """Reyting postini Instagram ga yuborish"""
        self.login()
        caption = format_rating_instagram(stores_data, period)
        
        try:
            media = self.client.photo_upload(image_path, caption)
            return media.pk
        except Exception as e:
            print(f"Instagram rating post error: {e}")
            return None
```

### src/poster/formatter.py

```python
from typing import Dict, List

def format_promotion_text(data: Dict) -> str:
    """Telegram uchun aksiya matni"""
    
    store = data.get("store", "").upper()
    title = data.get("title", "Aksiya")
    old_price = data.get("old_price")
    new_price = data.get("new_price")
    discount = data.get("discount_text", f"{data.get('discount_percent', 0)}%")
    deadline = data.get("deadline_text", "")
    source_url = data.get("source_url", "")
    
    text = f"🔥 <b>{store} AKSIYASI</b>\n\n"
    text += f"📱 {title}\n"
    
    if old_price and new_price:
        text += f"💰 <s>{old_price:,.0f}</s> → <b>{new_price:,.0f} so'm</b>\n"
    elif new_price:
        text += f"💰 <b>{new_price:,.0f} so'm</b>\n"
    
    text += f"📉 Chegirma: <b>{discount}</b>\n"
    
    if deadline:
        text += f"⏰ Muddat: {deadline}\n"
    
    if source_url:
        text += f"\n🛒 <a href='{source_url}'>Xarid qilish</a>\n"
    
    text += "\n━━━━━━━━━━━━━━━━━━━━━\n\n"
    text += "✅ Kanalga obuna bo'ling: @mirbazar_uz\n"
    text += "🤖 Bot: @mirbazar_bot\n\n"
    text += f"#aksiya #chegirma #{store.lower()}"
    
    return text

def format_rating_text(stores: List[Dict], period: str = "Haftalik") -> str:
    """Reyting matni"""
    
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]
    
    text = f"🏆 <b>{period.upper()} REYTING</b>\n\n"
    text += "Eng ko'p chegirma bergan do'konlar:\n\n"
    
    for i, store in enumerate(stores[:8]):
        medal = medals[i] if i < len(medals) else f"{i+1}."
        name = store.get("name", "")
        count = store.get("count", 0)
        max_disc = store.get("max_discount", 0)
        text += f"{medal} <b>{name}</b> — {count} aksiya ({max_disc}% gacha)\n"
    
    if stores:
        winner = stores[0].get("name", "")
        text += f"\n🏆 Bu hafta g'olib: <b>{winner}</b>\n"
    
    text += "\n━━━━━━━━━━━━━━━━━━━━━\n\n"
    text += "👉 @mirbazar_uz — o'tkazib yubormang!\n\n"
    text += "#reyting #chegirma #aksiya"
    
    return text

def format_digest_text(promotions: List[Dict]) -> str:
    """Kunlik digest matni"""
    
    text = "🔥 <b>BUGUNGI TOP CHEGIRMALAR</b>\n\n"
    
    for i, promo in enumerate(promotions[:5], 1):
        title = promo.get("title", "")[:30]
        store = promo.get("store", "")
        discount = promo.get("discount_text", f"{promo.get('discount_percent', 0)}%")
        text += f"{i}️⃣ <b>{discount}</b> {title}\n   📍 {store}\n\n"
    
    text += "━━━━━━━━━━━━━━━━━━━━━\n\n"
    text += "✅ Batafsil: @mirbazar_uz\n"
    text += "🔔 Obuna bo'ling — o'tkazib yubormang!\n\n"
    text += "#top5 #chegirma #aksiya"
    
    return text

def format_promotion_instagram(data: Dict) -> str:
    """Instagram uchun aksiya matni"""
    
    store = data.get("store", "").upper()
    title = data.get("title", "Aksiya")
    old_price = data.get("old_price")
    new_price = data.get("new_price")
    discount = data.get("discount_text", f"{data.get('discount_percent', 0)}%")
    deadline = data.get("deadline_text", "")
    
    text = f"🔥 {discount} CHEGIRMA!\n\n"
    text += f"{title}\n\n"
    
    if old_price:
        text += f"💰 Eski narx: {old_price:,.0f} so'm\n"
    if new_price:
        text += f"✅ Yangi narx: {new_price:,.0f} so'm\n"
    
    text += f"📍 Do'kon: {store}\n"
    
    if deadline:
        text += f"⏰ {deadline}\n"
    
    text += "\n━━━━━━━━━━━━━━━\n\n"
    text += "📢 Chegirmalarni o'tkazib yubormang!\n"
    text += "👉 Telegram: @mirbazar_uz (bio'da link)\n\n"
    text += "Saqlab qo'ying 📌 va do'stlaringizga ulashing!\n\n"
    text += f"#mirbazar #aksiya #chegirma #{store.lower()} "
    text += "#toshkent #uzbekistan #tekinaksiya #arzon"
    
    return text

def format_rating_instagram(stores: List[Dict], period: str = "Haftalik") -> str:
    """Instagram reyting matni"""
    
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
    
    text = f"🏆 {period.upper()} REYTING\n\n"
    text += "Eng ko'p chegirma bergan do'konlar:\n\n"
    
    for i, store in enumerate(stores[:5]):
        medal = medals[i]
        name = store.get("name", "")
        count = store.get("count", 0)
        text += f"{medal} {name} — {count} aksiya\n"
    
    text += "\n━━━━━━━━━━━━━━━\n\n"
    text += "📢 Har hafta yangi reyting!\n"
    text += "👉 Telegram: @mirbazar_uz\n\n"
    text += "#mirbazar #reyting #chegirma #aksiya #top5"
    
    return text
```

---

## 📊 RATING

### src/rating/calculator.py

```python
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from typing import List, Dict
from ..database.models import Promotion, Store, StoreStats, PromotionStatus

class RatingCalculator:
    def __init__(self, db: Session):
        self.db = db
    
    def calculate_weekly_rating(self) -> List[Dict]:
        """Haftalik reyting hisoblash"""
        
        week_ago = datetime.utcnow() - timedelta(days=7)
        
        # Har bir do'kon uchun statistika
        stats = self.db.query(
            Store.id,
            Store.name,
            Store.slug,
            Store.color,
            func.count(Promotion.id).label('count'),
            func.max(Promotion.discount_percent).label('max_discount'),
            func.avg(Promotion.discount_percent).label('avg_discount')
        ).join(
            Promotion, Store.id == Promotion.store_id
        ).filter(
            Promotion.created_at >= week_ago,
            Promotion.status == PromotionStatus.ACTIVE
        ).group_by(
            Store.id
        ).order_by(
            func.count(Promotion.id).desc()
        ).all()
        
        return [
            {
                "id": s.id,
                "name": s.name,
                "slug": s.slug,
                "color": s.color,
                "count": s.count,
                "max_discount": s.max_discount or 0,
                "avg_discount": round(s.avg_discount or 0, 1)
            }
            for s in stats
        ]
    
    def calculate_monthly_rating(self) -> List[Dict]:
        """Oylik reyting hisoblash"""
        
        month_ago = datetime.utcnow() - timedelta(days=30)
        
        stats = self.db.query(
            Store.id,
            Store.name,
            Store.slug,
            Store.color,
            func.count(Promotion.id).label('count'),
            func.max(Promotion.discount_percent).label('max_discount'),
            func.avg(Promotion.discount_percent).label('avg_discount')
        ).join(
            Promotion, Store.id == Promotion.store_id
        ).filter(
            Promotion.created_at >= month_ago
        ).group_by(
            Store.id
        ).order_by(
            func.count(Promotion.id).desc()
        ).all()
        
        return [
            {
                "id": s.id,
                "name": s.name,
                "slug": s.slug,
                "color": s.color,
                "count": s.count,
                "max_discount": s.max_discount or 0,
                "avg_discount": round(s.avg_discount or 0, 1)
            }
            for s in stats
        ]
    
    def get_top_discounts(self, limit: int = 5) -> List[Dict]:
        """Eng katta chegirmalar"""
        
        promotions = self.db.query(
            Promotion
        ).join(
            Store
        ).filter(
            Promotion.status == PromotionStatus.ACTIVE
        ).order_by(
            Promotion.discount_percent.desc()
        ).limit(limit).all()
        
        return [
            {
                "id": p.id,
                "title": p.title,
                "store": p.store.name,
                "discount_percent": p.discount_percent,
                "discount_text": p.discount_text,
                "new_price": p.new_price,
                "old_price": p.old_price
            }
            for p in promotions
        ]
    
    def save_weekly_stats(self):
        """Haftalik statistikani saqlash"""
        
        stats = self.calculate_weekly_rating()
        now = datetime.utcnow()
        week_start = now - timedelta(days=7)
        
        for s in stats:
            store_stat = StoreStats(
                store_id=s["id"],
                period_type="weekly",
                period_start=week_start,
                period_end=now,
                total_promotions=s["count"],
                max_discount=s["max_discount"],
                avg_discount=s["avg_discount"]
            )
            self.db.add(store_stat)
        
        self.db.commit()
```

---

## ⏰ SCHEDULER

### src/scheduler/jobs.py

```python
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import asyncio

class MirbazarScheduler:
    def __init__(self, app):
        self.app = app
        self.scheduler = AsyncIOScheduler()
    
    def setup_jobs(self):
        """Jadval ishlarini sozlash"""
        
        # Har 4 soatda scraping
        self.scheduler.add_job(
            self.app.run_scraping,
            CronTrigger(hour='*/4'),
            id='scraping',
            name='Telegram kanallardan scraping'
        )
        
        # Har kuni 09:00 da digest
        self.scheduler.add_job(
            self.app.post_daily_digest,
            CronTrigger(hour=9, minute=0),
            id='daily_digest',
            name='Kunlik TOP-5 digest'
        )
        
        # Har dushanba 10:00 da haftalik reyting
        self.scheduler.add_job(
            self.app.post_weekly_rating,
            CronTrigger(day_of_week='mon', hour=10, minute=0),
            id='weekly_rating',
            name='Haftalik reyting'
        )
        
        # Har oyning 1-kuni 11:00 da oylik xulosa
        self.scheduler.add_job(
            self.app.post_monthly_summary,
            CronTrigger(day=1, hour=11, minute=0),
            id='monthly_summary',
            name='Oylik xulosa'
        )
        
        # Har kuni 00:00 da eskirgan aksiyalarni tozalash
        self.scheduler.add_job(
            self.app.cleanup_expired_promotions,
            CronTrigger(hour=0, minute=0),
            id='cleanup',
            name='Eskirgan aksiyalarni tozalash'
        )
    
    def start(self):
        """Schedulerni ishga tushirish"""
        self.scheduler.start()
    
    def stop(self):
        """Schedulerni to'xtatish"""
        self.scheduler.shutdown()
```

---

## 🚀 MAIN

### src/main.py

```python
import asyncio
from datetime import datetime, timedelta
from typing import List
from dotenv import load_dotenv
import os

from .config import Settings
from .scraper.telegram_scraper import TelegramScraper
from .scraper.channels import TELEGRAM_CHANNELS
from .ai.groq_client import GroqClient
from .ai.validator import PromotionValidator
from .database.connection import get_db, init_db
from .database.crud import PromotionCRUD, StoreCRUD
from .database.models import PromotionStatus
from .image.generator import ImageGenerator
from .poster.telegram_poster import TelegramPoster
from .poster.instagram_poster import InstagramPoster
from .rating.calculator import RatingCalculator
from .scheduler.jobs import MirbazarScheduler

load_dotenv()

class MirbazarApp:
    def __init__(self):
        self.settings = Settings()
        
        # Components
        self.scraper = TelegramScraper()
        self.groq = GroqClient(self.settings.GROQ_API_KEY)
        self.validator = PromotionValidator()
        self.image_gen = ImageGenerator()
        self.telegram = TelegramPoster(
            self.settings.TELEGRAM_BOT_TOKEN,
            self.settings.TELEGRAM_CHANNEL_ID
        )
        self.instagram = InstagramPoster(
            self.settings.INSTAGRAM_USERNAME,
            self.settings.INSTAGRAM_PASSWORD
        )
        
        # Database
        init_db()
        self.db = next(get_db())
        self.promo_crud = PromotionCRUD(self.db)
        self.store_crud = StoreCRUD(self.db)
        self.rating_calc = RatingCalculator(self.db)
        
        # Scheduler
        self.scheduler = MirbazarScheduler(self)
    
    async def run_scraping(self):
        """Barcha kanallardan scraping"""
        print(f"[{datetime.now()}] Scraping boshlandi...")
        
        for channel in TELEGRAM_CHANNELS:
            await self._scrape_channel(channel)
            await asyncio.sleep(5)  # Rate limiting
        
        print(f"[{datetime.now()}] Scraping tugadi")
    
    async def _scrape_channel(self, channel: dict):
        """Bitta kanaldan scraping"""
        print(f"  Scraping: {channel['name']}")
        
        # Do'konni bazadan olish yoki yaratish
        store = self.store_crud.get_or_create(channel)
        
        # Postlarni olish
        posts = self.scraper.fetch_channel_posts(channel['url'], limit=20)
        
        for post in posts:
            # Aksiyami tekshirish
            if not self.scraper.is_promotion_post(post['text']):
                continue
            
            # Allaqachon bazada bormi
            if self.promo_crud.exists_by_source_id(post['post_id']):
                continue
            
            # Groq bilan parse qilish
            parsed = self.groq.parse_promotion(post['text'], channel['name'])
            if not parsed:
                continue
            
            # Validatsiya
            validated = self.validator.validate(parsed)
            
            # Bazaga saqlash
            promotion = self.promo_crud.create(
                store_id=store.id,
                data=validated,
                source_post_id=post['post_id'],
                source_url=post['post_link'],
                image_url=post.get('image_url')
            )
            
            # Rasm yaratish
            if promotion and validated.get('is_active'):
                image_data = {
                    **validated,
                    'store': channel['name'],
                    'id': promotion.id
                }
                image_path = self.image_gen.create_promotion_image(image_data)
                self.promo_crud.update_image_path(promotion.id, image_path)
                
                # Telegram ga post qilish
                await self._post_to_telegram(promotion, image_path)
                
                # Instagram ga post qilish (kun davomida max 5 ta)
                await self._post_to_instagram(promotion, image_path)
    
    async def _post_to_telegram(self, promotion, image_path: str):
        """Telegram ga post"""
        data = {
            'store': promotion.store.name,
            'title': promotion.title,
            'old_price': promotion.old_price,
            'new_price': promotion.new_price,
            'discount_text': promotion.discount_text,
            'deadline_text': promotion.deadline_text,
            'source_url': promotion.source_url
        }
        
        post_id = await self.telegram.post_promotion(data, image_path)
        
        if post_id:
            self.promo_crud.mark_posted(promotion.id, 'telegram', post_id)
            await asyncio.sleep(self.settings.POST_DELAY_SECONDS)
    
    async def _post_to_instagram(self, promotion, image_path: str):
        """Instagram ga post"""
        # Kunlik limit tekshirish
        today_posts = self.promo_crud.count_today_instagram_posts()
        if today_posts >= 5:
            return
        
        data = {
            'store': promotion.store.name,
            'title': promotion.title,
            'old_price': promotion.old_price,
            'new_price': promotion.new_price,
            'discount_text': promotion.discount_text,
            'deadline_text': promotion.deadline_text
        }
        
        post_id = self.instagram.post_promotion(data, image_path)
        
        if post_id:
            self.promo_crud.mark_posted(promotion.id, 'instagram', post_id)
    
    async def post_daily_digest(self):
        """Kunlik TOP-5 digest"""
        print(f"[{datetime.now()}] Kunlik digest...")
        
        top_promos = self.rating_calc.get_top_discounts(5)
        
        if not top_promos:
            return
        
        image_path = self.image_gen.create_digest_image(top_promos)
        await self.telegram.post_digest(top_promos, image_path)
    
    async def post_weekly_rating(self):
        """Haftalik reyting"""
        print(f"[{datetime.now()}] Haftalik reyting...")
        
        stores_data = self.rating_calc.calculate_weekly_rating()
        
        if not stores_data:
            return
        
        image_path = self.image_gen.create_rating_image(stores_data, "Haftalik")
        await self.telegram.post_rating(stores_data, image_path, "Haftalik")
        
        # Statistikani saqlash
        self.rating_calc.save_weekly_stats()
    
    async def post_monthly_summary(self):
        """Oylik xulosa"""
        print(f"[{datetime.now()}] Oylik xulosa...")
        
        stores_data = self.rating_calc.calculate_monthly_rating()
        
        if not stores_data:
            return
        
        image_path = self.image_gen.create_rating_image(stores_data, "Oylik")
        await self.telegram.post_rating(stores_data, image_path, "Oylik")
    
    async def cleanup_expired_promotions(self):
        """Eskirgan aksiyalarni tozalash"""
        print(f"[{datetime.now()}] Tozalash...")
        
        # 30 kundan oshgan expired aksiyalarni o'chirish
        threshold = datetime.utcnow() - timedelta(days=30)
        self.promo_crud.delete_old_expired(threshold)
        
        # Yangi expired aksiyalarni belgilash
        self.promo_crud.mark_expired()
    
    def run(self):
        """Asosiy ishga tushirish"""
        print("🚀 Mirbazar ishga tushmoqda...")
        
        # Scheduler ishga tushirish
        self.scheduler.setup_jobs()
        self.scheduler.start()
        
        # Event loop
        loop = asyncio.get_event_loop()
        
        try:
            # Dastlabki scraping
            loop.run_until_complete(self.run_scraping())
            
            # Cheksiz ishlash
            loop.run_forever()
        except KeyboardInterrupt:
            print("\n⏹️ To'xtatilmoqda...")
        finally:
            self.scheduler.stop()
            self.scraper.close()
            loop.close()


if __name__ == "__main__":
    app = MirbazarApp()
    app.run()
```

---

## 🐳 DOCKER

### docker-compose.yml

```yaml
version: '3.8'

services:
  # ==================== BACKEND ====================
  backend:
    build: ./backend
    container_name: mirbazar_backend
    restart: unless-stopped
    env_file:
      - .env
    volumes:
      - ./backend/assets:/app/assets
      - ./generated_images:/app/generated_images
    depends_on:
      - db
    networks:
      - mirbazar_net
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # ==================== FRONTEND ====================
  frontend:
    build: ./frontend
    container_name: mirbazar_frontend
    restart: unless-stopped
    environment:
      - NUXT_PUBLIC_API_BASE=http://backend:8000
    depends_on:
      - backend
    networks:
      - mirbazar_net

  # ==================== DATABASE ====================
  db:
    image: postgres:15-alpine
    container_name: mirbazar_db
    restart: unless-stopped
    environment:
      POSTGRES_USER: mirbazar
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: mirbazar
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - mirbazar_net

  # ==================== NGINX ====================
  nginx:
    image: nginx:alpine
    container_name: mirbazar_nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
    depends_on:
      - backend
      - frontend
    networks:
      - mirbazar_net

volumes:
  postgres_data:

networks:
  mirbazar_net:
    driver: bridge
```

### backend/Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY src/ ./src/
COPY tests/ ./tests/
COPY assets/ ./assets/

# Create directories
RUN mkdir -p generated_images

# Expose port
EXPOSE 8000

# Run
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### frontend/Dockerfile

```dockerfile
FROM node:20-alpine AS builder

WORKDIR /app

# Dependencies
COPY package*.json ./
RUN npm ci

# Build
COPY . .
RUN npm run build

# Production
FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app/.output ./.output

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]
```

### nginx/nginx.conf

```nginx
events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    # Gzip
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

    upstream backend {
        server backend:8000;
    }

    upstream frontend {
        server frontend:3000;
    }

    server {
        listen 80;
        server_name mirbazar.uz www.mirbazar.uz;

        # Redirect to HTTPS (agar SSL bor bo'lsa)
        # return 301 https://$server_name$request_uri;

        # API routes
        location /api/ {
            proxy_pass http://backend/;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Health check
        location /health {
            proxy_pass http://backend/health;
        }

        # Frontend
        location / {
            proxy_pass http://frontend;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_cache_bypass $http_upgrade;
        }

        # Static files cache
        location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2)$ {
            proxy_pass http://frontend;
            expires 30d;
            add_header Cache-Control "public, immutable";
        }
    }
}
```

---

## ✅ MUHIM ESLATMALAR

1. **Groq API Key** — console.groq.com dan olish (BEPUL)
2. **Telegram Bot** — @BotFather dan yaratish
3. **Instagram** — 2FA o'chirilgan akkaunt kerak
4. **Shriftlar** — Inter shriftini assets/fonts ga yuklab qo'yish
5. **Do'kon logolari** — assets/logos papkasiga PNG formatda qo'yish

---

## 🚨 MUHIM: CI/CD VA DEPLOYMENT QOIDALARI

### ⛔ QATTIQ QOIDA: LOCAL BUILD YO'Q!

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   ❌ LOCAL DA HECH NARSA BUILD QILINMAYDI                          │
│   ❌ LOCAL DA HECH NARSA RUN QILINMAYDI                            │
│   ❌ LOCAL DA DOCKER ISHLATILMAYDI                                 │
│                                                                     │
│   ✅ FAQAT KOD YOZILADI                                            │
│   ✅ GITHUB GA PUSH QILINADI                                       │
│   ✅ CI/CD SERVERDA HAMMASI AVTOMATIK                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 CI/CD WORKFLOW

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   DEVELOPER  │────▶│    GITHUB    │────▶│    SERVER    │
│   (local)    │     │   Actions    │     │  62.84.186.84│
│              │     │              │     │              │
│  Kod yozish  │     │  CI/CD       │     │  Build       │
│  Git push    │     │  Pipeline    │     │  Run         │
│              │     │              │     │  Deploy      │
└──────────────┘     └──────────────┘     └──────────────┘
```

---

## 📁 GITHUB ACTIONS WORKFLOW

### .github/workflows/deploy.yml

```yaml
name: Deploy Mirbazar

on:
  push:
    branches: [main]

jobs:
  deploy:
    name: Build, Test & Deploy to Production
    runs-on: ubuntu-latest

    steps:
      - name: Deploy to Server
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          port: ${{ secrets.SERVER_PORT }}
          script: |
            cd /var/www/mirbazar_uz_usr/data/www/mirbazar.uz
            
            echo "📥 Pulling latest code..."
            git pull origin main
            
            echo "🛑 Stopping containers..."
            docker compose down
            
            echo "🔨 Building containers..."
            docker compose build --no-cache
            
            echo "🧪 Running tests..."
            docker compose run --rm backend pytest tests/ -v --tb=short
            
            if [ $? -ne 0 ]; then
              echo "❌ Tests failed! Aborting deployment."
              exit 1
            fi
            
            echo "🚀 Starting containers..."
            docker compose up -d
            
            echo "⏳ Waiting for startup..."
            sleep 20
            
            echo "🔍 Health check..."
            curl -f http://127.0.0.1:8000/health || exit 1
            curl -f http://127.0.0.1:3000 || exit 1
            
            echo "🧹 Cleanup old images..."
            docker image prune -f
            
            echo "✅ Mirbazar deployed successfully!"
```

---

## 🔐 GITHUB SECRETS (Settings → Secrets → Actions)

| Secret Name | Value |
|-------------|-------|
| `SERVER_HOST` | 62.84.186.84 |
| `SERVER_USER` | root |
| `SERVER_PORT` | 22 |
| `SSH_PRIVATE_KEY` | (server SSH private key) |

---

## 📂 SERVER STRUKTURA

```
/var/www/mirbazar_uz_usr/data/www/mirbazar.uz/
├── .env                    # Production environment (SERVERDA YARATILADI)
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── src/
│   └── ... (barcha kod)
├── assets/
│   ├── fonts/
│   └── logos/
└── generated_images/       # Docker volume
```

---

## 🛠️ SERVER SETUP (BIR MARTALIK)

Serverda quyidagilar **oldindan** o'rnatilgan bo'lishi kerak:

```bash
# 1. Docker o'rnatish
curl -fsSL https://get.docker.com | sh

# 2. Docker Compose o'rnatish
apt install docker-compose-plugin

# 3. Git o'rnatish
apt install git

# 4. Repo clone (birinchi marta)
cd /var/www/mirbazar_uz_usr/data/www/
git clone https://github.com/YOUR_USERNAME/mirbazar.git mirbazar.uz
cd mirbazar.uz

# 5. .env yaratish (FAQAT SERVERDA)
cp .env.example .env
nano .env
# Barcha API kalitlarni yozish

# 6. Assets yuklash
# fonts/ va logos/ papkalarini serverga yuklash

# 7. Birinchi ishga tushirish
docker compose up -d
```

---

## 📋 DEVELOPER WORKFLOW

```bash
# 1. Local da kod yozish
code .

# 2. Git commit
git add .
git commit -m "feat: add new feature"

# 3. Push to GitHub
git push origin main

# 4. GitHub Actions avtomatik ishga tushadi
#    - Serverga SSH orqali ulanadi
#    - git pull qiladi
#    - docker compose build qiladi
#    - docker compose up -d qiladi

# 5. Tayyor! Serverda ishlayapti
```

---

## ⚠️ ESLATMALAR

1. **Local test yo'q** — Kod to'g'ridan-to'g'ri serverda test qilinadi
2. **.env local da yo'q** — Faqat serverda mavjud
3. **Docker local da ishlatilmaydi** — Faqat serverda
4. **Assets serverda** — fonts/, logos/ serverda saqlanadi
5. **generated_images/** — Docker volume sifatida serverda

---

## 🔍 DEBUGGING (Serverda)

```bash
# SSH orqali serverga kirish
ssh root@62.84.186.84

# Mirbazar papkasiga o'tish
cd /var/www/mirbazar_uz_usr/data/www/mirbazar.uz

# Loglarni ko'rish
docker compose logs -f app

# Container ichiga kirish
docker compose exec app bash

# Restart
docker compose restart app

# To'liq rebuild
docker compose down
docker compose build --no-cache
docker compose up -d
```

---

## 🎯 ISHGA TUSHIRISH QADAMLARI

**Claude Code uchun:**

1. ✅ Barcha kodlarni yoz
2. ✅ GitHub repository yarat
3. ✅ GitHub Secrets sozla
4. ✅ Serverda bir martalik setup qil
5. ✅ `git push origin main` — tamom!

**HECH QACHON:**
- ❌ `docker build` local da
- ❌ `docker compose up` local da
- ❌ `python main.py` local da
- ❌ `.env` local da yaratish

---

## 🚀 ISHNI BOSHLASH QO'LLANMASI (STEP BY STEP)

### 📋 UMUMIY JARAYON

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  1️⃣ TAYYORGARLIK (bir martalik)                                   │
│     ├── GitHub repo yaratish                                       │
│     ├── Server sozlash                                             │
│     ├── API kalitlar olish                                         │
│     └── GitHub Secrets qo'shish                                    │
│                                                                     │
│  2️⃣ DEVELOPMENT                                                    │
│     ├── Claude Code bilan kod yozish                               │
│     ├── Git commit & push                                          │
│     └── CI/CD avtomatik deploy                                     │
│                                                                     │
│  3️⃣ MONITORING                                                     │
│     ├── Loglarni kuzatish                                          │
│     └── Xatolarni tuzatish                                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 1️⃣ TAYYORGARLIK (BIR MARTALIK)

### A. API KALITLARNI OLISH

#### Groq API Key (BEPUL):
```
1. https://console.groq.com ga o'ting
2. Google/GitHub bilan ro'yxatdan o'ting
3. "API Keys" → "Create API Key"
4. Kalitni nusxalang: gsk_xxxxxxxxxxxx
```

#### Telegram Bot Token:
```
1. Telegram da @BotFather ni oching
2. /newbot buyrug'ini yuboring
3. Bot nomini kiriting: Mirbazar Bot
4. Username kiriting: mirbazar_bot
5. Token nusxalang: 123456789:ABCxxxxx
```

#### Telegram Channel:
```
1. Telegram da yangi kanal yarating: @mirbazar_uz
2. Botni kanalga admin qilib qo'shing
3. Channel ID: @mirbazar_uz
```

#### Instagram (ixtiyoriy):
```
1. Yangi Instagram akkaunt yarating: mirbazar.uz
2. 2FA o'chiring (muhim!)
3. Username va parolni saqlang
```

---

### B. GITHUB REPO YARATISH

```bash
# 1. GitHub da yangi repo yaratish
#    https://github.com/new
#    Repo nomi: mirbazar
#    Private yoki Public

# 2. Local papka yaratish
mkdir mirbazar
cd mirbazar

# 3. Git init
git init
git remote add origin https://github.com/YOUR_USERNAME/mirbazar.git

# 4. README qo'shish
echo "# Mirbazar" > README.md
git add .
git commit -m "init"
git push -u origin main
```

---

### C. GITHUB SECRETS QO'SHISH

```
1. GitHub repo → Settings → Secrets and variables → Actions
2. "New repository secret" bosing
3. Quyidagilarni qo'shing:

┌─────────────────────┬─────────────────────────────────┐
│ Secret Name         │ Value                           │
├─────────────────────┼─────────────────────────────────┤
│ SERVER_HOST         │ 62.84.186.84                    │
│ SERVER_USER         │ root                            │
│ SERVER_PORT         │ 22                              │
│ SSH_PRIVATE_KEY     │ (serverdan olgan private key)   │
└─────────────────────┴─────────────────────────────────┘
```

#### SSH Key olish:
```bash
# Serverga kirish
ssh root@62.84.186.84

# SSH key yaratish (agar yo'q bo'lsa)
ssh-keygen -t ed25519 -f ~/.ssh/mirbazar_deploy -N ""

# Public keyni authorized_keys ga qo'shish
cat ~/.ssh/mirbazar_deploy.pub >> ~/.ssh/authorized_keys

# Private keyni ko'rish (GitHub Secret ga qo'yish uchun)
cat ~/.ssh/mirbazar_deploy
# Bu chiqgan matnni to'liq nusxalab GitHub SECRET ga qo'ying
```

---

### D. SERVER SOZLASH (BIR MARTALIK)

```bash
# 1. Serverga kirish
ssh root@62.84.186.84

# 2. Docker o'rnatish
curl -fsSL https://get.docker.com | sh
systemctl enable docker
systemctl start docker

# 3. Docker Compose o'rnatish
apt update
apt install -y docker-compose-plugin

# 4. Papka yaratish
mkdir -p /var/www/mirbazar_uz_usr/data/www/
cd /var/www/mirbazar_uz_usr/data/www/

# 5. Repo clone
git clone https://github.com/YOUR_USERNAME/mirbazar.git mirbazar.uz
cd mirbazar.uz

# 6. .env yaratish
cat > .env << 'EOF'
# Database
DATABASE_URL=postgresql://mirbazar:your_secure_password@db:5432/mirbazar

# Groq AI
GROQ_API_KEY=gsk_your_groq_api_key_here

# Telegram
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHANNEL_ID=@mirbazar_uz
TELEGRAM_ADMIN_ID=your_telegram_user_id

# Instagram
INSTAGRAM_USERNAME=mirbazar.uz
INSTAGRAM_PASSWORD=your_instagram_password

# App Settings
SCRAPE_INTERVAL_HOURS=4
POST_DELAY_SECONDS=60
MAX_POSTS_PER_DAY=20
DEBUG=false
EOF

# 7. .env ni tahrirlash
nano .env
# Barcha qiymatlarni to'g'ri yozing

# 8. Assets papkalarini yaratish
mkdir -p assets/fonts assets/logos generated_images

# 9. Shriftlarni yuklash
cd assets/fonts
wget https://github.com/rsms/inter/releases/download/v3.19/Inter-3.19.zip
unzip Inter-3.19.zip
cp "Inter Desktop/Inter-Bold.otf" Inter-Bold.ttf
cp "Inter Desktop/Inter-Regular.otf" Inter-Regular.ttf
rm -rf Inter-3.19.zip "Inter Desktop"
cd ../..

# 10. Tayyor! Endi kod push qilinsa avtomatik deploy bo'ladi
```

---

## 2️⃣ DEVELOPMENT (CLAUDE CODE BILAN)

### A. EVERYTHING CLAUDE CODE O'RNATISH

```
1. VS Code oching
2. Extensions (Ctrl+Shift+X)
3. "Everything Claude Code" qidiring
4. Install bosing
5. Claude API key kiriting (agar so'rasa)
```

### B. YANGI CHAT BOSHLASH

```
1. VS Code da Ctrl+Shift+P
2. "Claude Code: New Chat" tanlang
3. Yoki sidebar da Claude ikonkasini bosing
```

### C. PROMPTNI YUBORISH

```
1. MIRBAZAR_CLAUDE_CODE_PROMPT.md faylini oching
2. To'liq matnni nusxalang (Ctrl+A, Ctrl+C)
3. Claude Code chatga joylashtiring (Ctrl+V)
4. Enter bosing

Claude Code:
- Barcha fayllarni yaratadi
- Papka strukturasini tuzadi
- Kodlarni yozadi
```

### D. FAYLLARNI KO'RISH VA TEKSHIRISH

```
Claude Code yozgan fayllarni ko'ring:
- src/main.py
- src/scraper/telegram_scraper.py
- src/ai/groq_client.py
- docker-compose.yml
- va boshqalar...

Agar biror narsa yetishmasa, Claude Code ga ayting:
"... qismini to'liqroq yozib ber"
```

### E. GIT PUSH

```bash
# Barcha o'zgarishlarni qo'shish
git add .

# Commit
git commit -m "feat: initial mirbazar setup"

# Push
git push origin main
```

### F. DEPLOY TEKSHIRISH

```
1. GitHub repo → Actions tab
2. Workflow ishlaganini ko'ring
3. Yashil ✓ bo'lsa — muvaffaqiyatli
4. Qizil ✗ bo'lsa — xatoni o'qing
```

---

## 3️⃣ MONITORING VA DEBUGGING

### A. SERVERDA LOGLARNI KO'RISH

```bash
# SSH orqali serverga kirish
ssh root@62.84.186.84

# Mirbazar papkasiga o'tish
cd /var/www/mirbazar_uz_usr/data/www/mirbazar.uz

# Barcha containerlar holati
docker compose ps

# App loglari (real-time)
docker compose logs -f app

# Faqat oxirgi 100 qator
docker compose logs --tail=100 app

# Database loglari
docker compose logs -f db
```

### B. XATOLARNI TUZATISH

```bash
# Container restart
docker compose restart app

# To'liq rebuild
docker compose down
docker compose build --no-cache
docker compose up -d

# Container ichiga kirish
docker compose exec app bash

# Python shell
docker compose exec app python
```

### C. MA'LUMOTLAR BAZASI

```bash
# PostgreSQL ga kirish
docker compose exec db psql -U mirbazar -d mirbazar

# Jadvallarni ko'rish
\dt

# Aksiyalarni ko'rish
SELECT * FROM promotions LIMIT 10;

# Chiqish
\q
```

---

## 📋 KUNLIK WORKFLOW

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  ERTALAB:                                                          │
│  1. Loglarni tekshirish: docker compose logs --tail=50 app         │
│  2. Telegram kanalni tekshirish: @mirbazar_uz                      │
│                                                                     │
│  YANGI FEATURE QO'SHISH:                                           │
│  1. Local da VS Code oching                                        │
│  2. Claude Code bilan kod yozing                                   │
│  3. git add . && git commit -m "feat: ..." && git push             │
│  4. GitHub Actions deploy qilishini kuting                         │
│  5. Serverda loglarni tekshiring                                   │
│                                                                     │
│  XATO BO'LSA:                                                      │
│  1. docker compose logs -f app — xatoni toping                     │
│  2. Claude Code ga xatoni ko'rsating                               │
│  3. Tuzatib, qayta push qiling                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ KO'P UCHRAYDIGAN XATOLAR

### 1. "Permission denied" (SSH)
```bash
# Serverda
chmod 600 ~/.ssh/mirbazar_deploy
chmod 700 ~/.ssh
```

### 2. "Database connection failed"
```bash
# .env da DATABASE_URL to'g'riligini tekshiring
# db container ishlaganini tekshiring
docker compose ps
docker compose logs db
```

### 3. "Groq API error"
```bash
# .env da GROQ_API_KEY to'g'riligini tekshiring
# Rate limit bo'lishi mumkin — biroz kuting
```

### 4. "Telegram post failed"
```bash
# Bot tokenni tekshiring
# Bot kanalga admin qilinganini tekshiring
# Channel ID to'g'riligini tekshiring (@mirbazar_uz)
```

### 5. "Instagram login failed"
```bash
# 2FA o'chirilganligini tekshiring
# Username/password to'g'riligini tekshiring
# Instagram yangi qurilmani bloklagan bo'lishi mumkin
```

---

## 🎯 CHECKLIST

### Tayyorgarlik:
- [ ] Groq API key olindi
- [ ] Telegram bot yaratildi
- [ ] Telegram kanal yaratildi
- [ ] Bot kanalga admin qilindi
- [ ] GitHub repo yaratildi
- [ ] GitHub Secrets qo'shildi
- [ ] Server sozlandi
- [ ] .env serverda yaratildi
- [ ] Shriftlar yuklandi

### Birinchi deploy:
- [ ] Claude Code o'rnatildi
- [ ] Prompt yuborildi
- [ ] Kod yozildi
- [ ] Git push qilindi
- [ ] GitHub Actions muvaffaqiyatli
- [ ] Container ishlamoqda
- [ ] Birinchi post Telegram da chiqdi

---

## 📝 QISQACHA XULOSA

Bu loyiha:
- ✅ Telegram kanallardan aksiyalarni avtomatik yig'adi
- ✅ Groq AI bilan matnni parse qiladi
- ✅ Aktuallikni tekshiradi (30 kun saqlash)
- ✅ Chiroyli rasm yaratadi (Pillow)
- ✅ Telegram va Instagram ga avtomatik post qiladi
- ✅ Haftalik/Oylik reyting chiqaradi
- ✅ Mirbazar branding va CTA qo'shadi
- ✅ Chiroyli kreativ website

Barcha kodlarni yozib ber, test qilib ishga tushir!

---

## 🌐 WEBSITE DIZAYNI (CHIROYLI VA KREATIV)

### DIZAYN KONSEPTI

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   🎨 MIRBAZAR.UZ — PREMIUM DARK THEME DIZAYN                                 ║
║                                                                               ║
║   Asosiy ranglar:                                                            ║
║   • Background:     #0a0a1a (qora-ko'k)                                      ║
║   • Card BG:        #12122a (quyuq ko'k)                                     ║
║   • Primary:        #7c3aed (binafsha)                                       ║
║   • Secondary:      #00d4ff (cyan)                                           ║
║   • Accent:         #f97316 (orange)                                         ║
║   • Success:        #10b981 (yashil)                                         ║
║   • Danger:         #ef4444 (qizil)                                          ║
║   • Text:           #ffffff / #9ca3af                                        ║
║                                                                               ║
║   Effektlar:                                                                 ║
║   • Glassmorphism kartalar                                                   ║
║   • Gradient borderlar                                                       ║
║   • Hover animatsiyalar                                                      ║
║   • Glow effektlar                                                           ║
║   • Smooth scroll                                                            ║
║   • Skeleton loading                                                         ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

### 📁 FRONTEND STRUKTURA

```
frontend/
├── index.html              # Asosiy sahifa
├── css/
│   ├── style.css           # Asosiy stillar
│   ├── components.css      # Komponentlar
│   └── animations.css      # Animatsiyalar
├── js/
│   ├── app.js              # Asosiy JS
│   ├── api.js              # API calls
│   └── filters.js          # Filter funksiyalar
└── assets/
    ├── icons/              # SVG ikonlar
    └── images/             # Rasmlar
```

---

### 🎨 ASOSIY CSS (style.css)

```css
/* ═══════════════════════════════════════════════════════════════════════
   MIRBAZAR.UZ — Premium Dark Theme
   ═══════════════════════════════════════════════════════════════════════ */

/* ─────────────────────────────────────
   CSS Variables
   ───────────────────────────────────── */
:root {
  /* Colors */
  --bg-primary: #0a0a1a;
  --bg-secondary: #12122a;
  --bg-card: rgba(18, 18, 42, 0.8);
  --bg-card-hover: rgba(28, 28, 62, 0.9);
  
  --color-primary: #7c3aed;
  --color-secondary: #00d4ff;
  --color-accent: #f97316;
  --color-success: #10b981;
  --color-danger: #ef4444;
  --color-warning: #eab308;
  
  --text-primary: #ffffff;
  --text-secondary: #9ca3af;
  --text-muted: #6b7280;
  
  /* Gradients */
  --gradient-primary: linear-gradient(135deg, #7c3aed 0%, #00d4ff 100%);
  --gradient-hot: linear-gradient(135deg, #ef4444 0%, #f97316 100%);
  --gradient-card: linear-gradient(145deg, rgba(124, 58, 237, 0.1) 0%, rgba(0, 212, 255, 0.1) 100%);
  
  /* Shadows */
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 20px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 8px 40px rgba(0, 0, 0, 0.5);
  --shadow-glow: 0 0 30px rgba(124, 58, 237, 0.3);
  --shadow-glow-cyan: 0 0 30px rgba(0, 212, 255, 0.3);
  
  /* Borders */
  --border-color: rgba(124, 58, 237, 0.2);
  --border-radius: 16px;
  --border-radius-lg: 24px;
  
  /* Transitions */
  --transition-fast: 0.15s ease;
  --transition-normal: 0.3s ease;
  --transition-slow: 0.5s ease;
  
  /* Fonts */
  --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ─────────────────────────────────────
   Reset & Base
   ───────────────────────────────────── */
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-primary);
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
  overflow-x: hidden;
}

/* Background animated gradient */
body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 20% 20%, rgba(124, 58, 237, 0.15) 0%, transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(0, 212, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(249, 115, 22, 0.05) 0%, transparent 50%);
  pointer-events: none;
  z-index: -1;
  animation: bgPulse 10s ease-in-out infinite;
}

@keyframes bgPulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}

/* ─────────────────────────────────────
   Typography
   ───────────────────────────────────── */
h1, h2, h3, h4, h5, h6 {
  font-weight: 700;
  line-height: 1.2;
}

h1 { font-size: clamp(2rem, 5vw, 3.5rem); }
h2 { font-size: clamp(1.5rem, 4vw, 2.5rem); }
h3 { font-size: clamp(1.25rem, 3vw, 1.75rem); }

.gradient-text {
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* ─────────────────────────────────────
   Container
   ───────────────────────────────────── */
.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 20px;
}

/* ─────────────────────────────────────
   Header / Navbar
   ───────────────────────────────────── */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  padding: 15px 0;
  background: rgba(10, 10, 26, 0.8);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-color);
  transition: var(--transition-normal);
}

.navbar.scrolled {
  padding: 10px 0;
  background: rgba(10, 10, 26, 0.95);
}

.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}

.logo-icon {
  width: 48px;
  height: 48px;
  background: var(--gradient-primary);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  box-shadow: var(--shadow-glow);
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 800;
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-links {
  display: flex;
  gap: 30px;
  list-style: none;
}

.nav-links a {
  color: var(--text-secondary);
  text-decoration: none;
  font-weight: 500;
  transition: var(--transition-fast);
  position: relative;
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--gradient-primary);
  transition: var(--transition-normal);
}

.nav-links a:hover {
  color: var(--text-primary);
}

.nav-links a:hover::after {
  width: 100%;
}

.nav-cta {
  display: flex;
  align-items: center;
  gap: 15px;
}

/* ─────────────────────────────────────
   Buttons
   ───────────────────────────────────── */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  border: none;
  cursor: pointer;
  transition: var(--transition-normal);
}

.btn-primary {
  background: var(--gradient-primary);
  color: white;
  box-shadow: var(--shadow-glow);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 40px rgba(124, 58, 237, 0.5);
}

.btn-secondary {
  background: var(--bg-card);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
}

.btn-secondary:hover {
  background: var(--bg-card-hover);
  border-color: var(--color-primary);
}

.btn-telegram {
  background: linear-gradient(135deg, #0088cc 0%, #00aced 100%);
  color: white;
}

.btn-telegram:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 30px rgba(0, 136, 204, 0.4);
}

/* ─────────────────────────────────────
   Hero Section
   ───────────────────────────────────── */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 120px 0 60px;
  position: relative;
  overflow: hidden;
}

.hero-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.hero-text h1 {
  margin-bottom: 20px;
}

.hero-text h1 span {
  display: block;
  color: var(--text-secondary);
  font-size: 0.5em;
  margin-top: 10px;
}

.hero-description {
  font-size: 1.2rem;
  color: var(--text-secondary);
  margin-bottom: 30px;
  max-width: 500px;
}

.hero-stats {
  display: flex;
  gap: 40px;
  margin-bottom: 40px;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.stat-label {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.hero-cta {
  display: flex;
  gap: 15px;
}

.hero-visual {
  position: relative;
}

.hero-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius-lg);
  padding: 30px;
  box-shadow: var(--shadow-lg);
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.hero-card-badge {
  position: absolute;
  top: -15px;
  right: -15px;
  background: var(--gradient-hot);
  padding: 10px 20px;
  border-radius: 30px;
  font-weight: 700;
  font-size: 1.2rem;
  box-shadow: 0 0 30px rgba(239, 68, 68, 0.5);
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

/* ─────────────────────────────────────
   Filter Section
   ───────────────────────────────────── */
.filters {
  padding: 40px 0;
  position: sticky;
  top: 70px;
  z-index: 100;
  background: rgba(10, 10, 26, 0.9);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-color);
}

.filters-content {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  align-items: center;
}

.filter-group {
  display: flex;
  gap: 10px;
}

.filter-btn {
  padding: 10px 20px;
  border-radius: 30px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition-normal);
}

.filter-btn:hover {
  border-color: var(--color-primary);
  color: var(--text-primary);
}

.filter-btn.active {
  background: var(--gradient-primary);
  border-color: transparent;
  color: white;
}

.search-box {
  flex: 1;
  min-width: 250px;
  position: relative;
}

.search-box input {
  width: 100%;
  padding: 12px 20px 12px 50px;
  border-radius: 30px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  font-size: 1rem;
  outline: none;
  transition: var(--transition-normal);
}

.search-box input:focus {
  border-color: var(--color-primary);
  box-shadow: var(--shadow-glow);
}

.search-box input::placeholder {
  color: var(--text-muted);
}

.search-box svg {
  position: absolute;
  left: 18px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
}

/* ─────────────────────────────────────
   Promotions Grid
   ───────────────────────────────────── */
.promotions {
  padding: 60px 0;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 40px;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 15px;
}

.section-title h2 {
  margin: 0;
}

.live-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: rgba(16, 185, 129, 0.2);
  border: 1px solid var(--color-success);
  border-radius: 30px;
  font-size: 0.85rem;
  color: var(--color-success);
}

.live-dot {
  width: 8px;
  height: 8px;
  background: var(--color-success);
  border-radius: 50%;
  animation: blink 1s ease-in-out infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}

.promo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 25px;
}

/* ─────────────────────────────────────
   Promotion Card
   ───────────────────────────────────── */
.promo-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  overflow: hidden;
  transition: var(--transition-normal);
  position: relative;
}

.promo-card:hover {
  transform: translateY(-8px);
  border-color: var(--color-primary);
  box-shadow: var(--shadow-glow);
}

.promo-card.expired {
  opacity: 0.6;
}

.promo-card.expired::after {
  content: 'TUGAGAN';
  position: absolute;
  top: 20px;
  right: -35px;
  background: var(--color-danger);
  color: white;
  padding: 5px 40px;
  font-size: 0.75rem;
  font-weight: 700;
  transform: rotate(45deg);
}

.promo-image {
  position: relative;
  height: 200px;
  overflow: hidden;
}

.promo-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: var(--transition-slow);
}

.promo-card:hover .promo-image img {
  transform: scale(1.1);
}

.promo-discount {
  position: absolute;
  top: 15px;
  left: 15px;
  background: var(--gradient-hot);
  padding: 8px 16px;
  border-radius: 8px;
  font-weight: 800;
  font-size: 1.1rem;
  box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4);
}

.promo-store {
  position: absolute;
  bottom: 15px;
  left: 15px;
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(10px);
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
}

.promo-store-logo {
  width: 20px;
  height: 20px;
  border-radius: 4px;
}

.promo-content {
  padding: 20px;
}

.promo-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 15px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.promo-prices {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 15px;
}

.price-old {
  color: var(--text-muted);
  text-decoration: line-through;
  font-size: 0.95rem;
}

.price-new {
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--color-success);
}

.price-currency {
  font-size: 0.9rem;
  color: var(--text-secondary);
}

.promo-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 15px;
  border-top: 1px solid var(--border-color);
}

.promo-deadline {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--color-accent);
  font-size: 0.9rem;
}

.promo-deadline.urgent {
  color: var(--color-danger);
  animation: urgentPulse 1s ease-in-out infinite;
}

@keyframes urgentPulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}

.promo-link {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--color-primary);
  text-decoration: none;
  font-weight: 600;
  transition: var(--transition-fast);
}

.promo-link:hover {
  color: var(--color-secondary);
}

/* ─────────────────────────────────────
   Store Rating Section
   ───────────────────────────────────── */
.rating-section {
  padding: 80px 0;
  background: var(--gradient-card);
}

.rating-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
}

.rating-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  padding: 25px;
  display: flex;
  align-items: center;
  gap: 20px;
  transition: var(--transition-normal);
}

.rating-card:hover {
  transform: translateX(10px);
  border-color: var(--color-primary);
}

.rating-position {
  font-size: 2rem;
  font-weight: 800;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  background: var(--gradient-primary);
}

.rating-position.gold {
  background: linear-gradient(135deg, #ffd700 0%, #ffb300 100%);
  color: #1a1a1a;
}

.rating-position.silver {
  background: linear-gradient(135deg, #c0c0c0 0%, #a0a0a0 100%);
  color: #1a1a1a;
}

.rating-position.bronze {
  background: linear-gradient(135deg, #cd7f32 0%, #b8860b 100%);
  color: #1a1a1a;
}

.rating-info {
  flex: 1;
}

.rating-store-name {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 5px;
}

.rating-stats {
  display: flex;
  gap: 20px;
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.rating-stats span {
  display: flex;
  align-items: center;
  gap: 5px;
}

.rating-discount {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--color-success);
}

/* ─────────────────────────────────────
   Footer
   ───────────────────────────────────── */
.footer {
  padding: 60px 0 30px;
  background: var(--bg-secondary);
  border-top: 1px solid var(--border-color);
}

.footer-content {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 40px;
}

.footer-brand p {
  color: var(--text-secondary);
  margin: 15px 0 25px;
  max-width: 300px;
}

.footer-social {
  display: flex;
  gap: 15px;
}

.social-link {
  width: 45px;
  height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  color: var(--text-secondary);
  transition: var(--transition-normal);
}

.social-link:hover {
  background: var(--gradient-primary);
  border-color: transparent;
  color: white;
  transform: translateY(-3px);
}

.footer-links h4 {
  margin-bottom: 20px;
  color: var(--text-primary);
}

.footer-links ul {
  list-style: none;
}

.footer-links li {
  margin-bottom: 12px;
}

.footer-links a {
  color: var(--text-secondary);
  text-decoration: none;
  transition: var(--transition-fast);
}

.footer-links a:hover {
  color: var(--color-primary);
}

.footer-bottom {
  padding-top: 30px;
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--text-muted);
  font-size: 0.9rem;
}

/* ─────────────────────────────────────
   Responsive
   ───────────────────────────────────── */
@media (max-width: 1024px) {
  .hero-content {
    grid-template-columns: 1fr;
    text-align: center;
  }
  
  .hero-text {
    order: 1;
  }
  
  .hero-visual {
    order: 2;
  }
  
  .hero-stats {
    justify-content: center;
  }
  
  .hero-cta {
    justify-content: center;
  }
  
  .footer-content {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
  }
  
  .promo-grid {
    grid-template-columns: 1fr;
  }
  
  .filters-content {
    flex-direction: column;
  }
  
  .filter-group {
    width: 100%;
    overflow-x: auto;
    padding-bottom: 10px;
  }
  
  .search-box {
    width: 100%;
  }
  
  .footer-content {
    grid-template-columns: 1fr;
    text-align: center;
  }
  
  .footer-social {
    justify-content: center;
  }
  
  .footer-bottom {
    flex-direction: column;
    gap: 15px;
  }
}

/* ─────────────────────────────────────
   Skeleton Loading
   ───────────────────────────────────── */
.skeleton {
  background: linear-gradient(90deg, var(--bg-card) 25%, var(--bg-card-hover) 50%, var(--bg-card) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
  border-radius: 8px;
}

@keyframes skeleton-loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.skeleton-card {
  height: 400px;
}

.skeleton-text {
  height: 20px;
  margin-bottom: 10px;
}

.skeleton-text.short {
  width: 60%;
}

/* ─────────────────────────────────────
   Scrollbar
   ───────────────────────────────────── */
::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: var(--bg-primary);
}

::-webkit-scrollbar-thumb {
  background: var(--color-primary);
  border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--color-secondary);
}
```

---

### 📄 ASOSIY HTML (index.html)

```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mirbazar.uz — Barcha chegirmalar bir joyda!</title>
  <meta name="description" content="O'zbekistondagi barcha do'konlarning eng yaxshi chegirmalari va aksiyalari. Texnomart, Asaxiy, Mediapark, Korzinka va boshqalar.">
  
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- CSS -->
  <link rel="stylesheet" href="/css/style.css">
  
  <!-- Open Graph -->
  <meta property="og:title" content="Mirbazar.uz — Barcha chegirmalar bir joyda!">
  <meta property="og:description" content="O'zbekistondagi eng yaxshi chegirmalar va aksiyalar">
  <meta property="og:image" content="/assets/og-image.png">
  <meta property="og:type" content="website">
</head>
<body>
  <!-- Navbar -->
  <nav class="navbar" id="navbar">
    <div class="container navbar-content">
      <a href="/" class="logo">
        <div class="logo-icon">🛒</div>
        <span class="logo-text">MIRBAZAR</span>
      </a>
      
      <ul class="nav-links">
        <li><a href="#promotions">Aksiyalar</a></li>
        <li><a href="#rating">Reyting</a></li>
        <li><a href="#stores">Do'konlar</a></li>
        <li><a href="#about">Haqida</a></li>
      </ul>
      
      <div class="nav-cta">
        <a href="https://t.me/mirbazar_uz" target="_blank" class="btn btn-telegram">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
          </svg>
          Obuna bo'ling
        </a>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <div class="hero-content">
        <div class="hero-text">
          <h1>
            <span class="gradient-text">Barcha chegirmalar</span>
            <span>bir joyda!</span>
          </h1>
          <p class="hero-description">
            O'zbekistondagi 10+ do'konning eng yaxshi aksiyalari va chegirmalari. 
            Kunlik yangilanish, chiroyli dizayn, bepul obuna.
          </p>
          
          <div class="hero-stats">
            <div class="stat-item">
              <div class="stat-number" id="totalPromos">150+</div>
              <div class="stat-label">Aktual aksiyalar</div>
            </div>
            <div class="stat-item">
              <div class="stat-number">10+</div>
              <div class="stat-label">Do'konlar</div>
            </div>
            <div class="stat-item">
              <div class="stat-number">70%</div>
              <div class="stat-label">Gacha chegirma</div>
            </div>
          </div>
          
          <div class="hero-cta">
            <a href="#promotions" class="btn btn-primary">
              🔥 Aksiyalarni ko'rish
            </a>
            <a href="https://t.me/mirbazar_uz" target="_blank" class="btn btn-secondary">
              📢 Telegram kanal
            </a>
          </div>
        </div>
        
        <div class="hero-visual">
          <div class="hero-card">
            <div class="hero-card-badge">-70%</div>
            <div style="text-align: center; padding: 20px;">
              <div style="font-size: 4rem; margin-bottom: 15px;">📱</div>
              <h3 style="margin-bottom: 10px;">iPhone 15 Pro Max</h3>
              <p style="color: var(--text-muted); text-decoration: line-through;">18 500 000 so'm</p>
              <p style="font-size: 1.8rem; font-weight: 800; color: var(--color-success);">5 550 000 so'm</p>
              <p style="color: var(--color-accent); margin-top: 15px;">⏰ 28-fevral gacha</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Filters -->
  <section class="filters" id="filters">
    <div class="container">
      <div class="filters-content">
        <div class="filter-group" id="categoryFilters">
          <button class="filter-btn active" data-category="all">Hammasi</button>
          <button class="filter-btn" data-category="electronics">📱 Elektronika</button>
          <button class="filter-btn" data-category="appliances">🏠 Maishiy texnika</button>
          <button class="filter-btn" data-category="grocery">🛒 Oziq-ovqat</button>
          <button class="filter-btn" data-category="fashion">👕 Kiyim-kechak</button>
        </div>
        
        <div class="filter-group" id="storeFilters">
          <button class="filter-btn" data-store="texnomart">Texnomart</button>
          <button class="filter-btn" data-store="asaxiy">Asaxiy</button>
          <button class="filter-btn" data-store="mediapark">Mediapark</button>
          <button class="filter-btn" data-store="korzinka">Korzinka</button>
        </div>
        
        <div class="search-box">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"/>
            <path d="m21 21-4.35-4.35"/>
          </svg>
          <input type="text" placeholder="Mahsulot qidirish..." id="searchInput">
        </div>
      </div>
    </div>
  </section>

  <!-- Promotions Grid -->
  <section class="promotions" id="promotions">
    <div class="container">
      <div class="section-header">
        <div class="section-title">
          <h2>🔥 Joriy aksiyalar</h2>
          <div class="live-badge">
            <span class="live-dot"></span>
            Yangilanmoqda
          </div>
        </div>
        <a href="#" class="btn btn-secondary">Barchasini ko'rish →</a>
      </div>
      
      <div class="promo-grid" id="promoGrid">
        <!-- Promotions will be loaded dynamically -->
        <div class="promo-card skeleton skeleton-card"></div>
        <div class="promo-card skeleton skeleton-card"></div>
        <div class="promo-card skeleton skeleton-card"></div>
        <div class="promo-card skeleton skeleton-card"></div>
        <div class="promo-card skeleton skeleton-card"></div>
        <div class="promo-card skeleton skeleton-card"></div>
      </div>
    </div>
  </section>

  <!-- Rating Section -->
  <section class="rating-section" id="rating">
    <div class="container">
      <div class="section-header">
        <div class="section-title">
          <h2>🏆 Haftalik reyting</h2>
        </div>
        <span style="color: var(--text-secondary);">Eng ko'p chegirma bergan do'konlar</span>
      </div>
      
      <div class="rating-grid" id="ratingGrid">
        <!-- Rating will be loaded dynamically -->
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-brand">
          <a href="/" class="logo">
            <div class="logo-icon">🛒</div>
            <span class="logo-text">MIRBAZAR</span>
          </a>
          <p>O'zbekistondagi barcha chegirmalar bir joyda. Kunlik yangilanish, eng yaxshi narxlar.</p>
          <div class="footer-social">
            <a href="https://t.me/mirbazar_uz" class="social-link" target="_blank">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
              </svg>
            </a>
            <a href="https://instagram.com/mirbazar.uz" class="social-link" target="_blank">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>
            </a>
          </div>
        </div>
        
        <div class="footer-links">
          <h4>Do'konlar</h4>
          <ul>
            <li><a href="#">Texnomart</a></li>
            <li><a href="#">Asaxiy</a></li>
            <li><a href="#">Mediapark</a></li>
            <li><a href="#">Korzinka</a></li>
            <li><a href="#">Makro</a></li>
          </ul>
        </div>
        
        <div class="footer-links">
          <h4>Kategoriyalar</h4>
          <ul>
            <li><a href="#">Smartfonlar</a></li>
            <li><a href="#">Televizorlar</a></li>
            <li><a href="#">Noutbuklar</a></li>
            <li><a href="#">Maishiy texnika</a></li>
            <li><a href="#">Oziq-ovqat</a></li>
          </ul>
        </div>
        
        <div class="footer-links">
          <h4>Bog'lanish</h4>
          <ul>
            <li><a href="https://t.me/mirbazar_uz">Telegram kanal</a></li>
            <li><a href="https://t.me/mirbazar_bot">Telegram bot</a></li>
            <li><a href="https://instagram.com/mirbazar.uz">Instagram</a></li>
            <li><a href="mailto:info@mirbazar.uz">info@mirbazar.uz</a></li>
          </ul>
        </div>
      </div>
      
      <div class="footer-bottom">
        <p>© 2026 Mirbazar.uz — Barcha huquqlar himoyalangan</p>
        <p>O'zbekistondagi eng yaxshi chegirmalar aggregatori</p>
      </div>
    </div>
  </footer>

  <!-- JavaScript -->
  <script src="/js/app.js"></script>
</body>
</html>
```

---

### 🔧 JAVASCRIPT (app.js)

```javascript
// ═══════════════════════════════════════════════════════════════════════
// MIRBAZAR.UZ — Main JavaScript
// ═══════════════════════════════════════════════════════════════════════

const API_URL = '/api';

// ─────────────────────────────────────
// Navbar scroll effect
// ─────────────────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// ─────────────────────────────────────
// Load promotions
// ─────────────────────────────────────
async function loadPromotions(filters = {}) {
  const grid = document.getElementById('promoGrid');
  
  try {
    const params = new URLSearchParams(filters);
    const response = await fetch(`${API_URL}/promotions?${params}`);
    const data = await response.json();
    
    grid.innerHTML = data.promotions.map(promo => createPromoCard(promo)).join('');
    
    // Update total count
    document.getElementById('totalPromos').textContent = data.total + '+';
    
  } catch (error) {
    console.error('Error loading promotions:', error);
    grid.innerHTML = '<p style="text-align: center; color: var(--text-muted);">Xatolik yuz berdi. Qayta urinib ko\'ring.</p>';
  }
}

function createPromoCard(promo) {
  const isExpired = promo.status === 'expired';
  const isUrgent = promo.days_left <= 2;
  
  return `
    <div class="promo-card ${isExpired ? 'expired' : ''}">
      <div class="promo-image">
        <img src="${promo.image_url || '/assets/placeholder.jpg'}" alt="${promo.title}" loading="lazy">
        <div class="promo-discount">${promo.discount_text}</div>
        <div class="promo-store">
          <img src="/assets/logos/${promo.store_slug}.png" alt="${promo.store}" class="promo-store-logo">
          ${promo.store}
        </div>
      </div>
      <div class="promo-content">
        <h3 class="promo-title">${promo.title}</h3>
        <div class="promo-prices">
          ${promo.old_price ? `<span class="price-old">${formatPrice(promo.old_price)}</span>` : ''}
          <span class="price-new">${formatPrice(promo.new_price)}</span>
          <span class="price-currency">so'm</span>
        </div>
        <div class="promo-meta">
          <span class="promo-deadline ${isUrgent ? 'urgent' : ''}">
            ⏰ ${promo.deadline_text || 'Muddat ko\'rsatilmagan'}
          </span>
          <a href="${promo.source_url}" target="_blank" class="promo-link">
            Xarid →
          </a>
        </div>
      </div>
    </div>
  `;
}

function formatPrice(price) {
  return new Intl.NumberFormat('uz-UZ').format(price);
}

// ─────────────────────────────────────
// Load rating
// ─────────────────────────────────────
async function loadRating() {
  const grid = document.getElementById('ratingGrid');
  
  try {
    const response = await fetch(`${API_URL}/rating/weekly`);
    const data = await response.json();
    
    grid.innerHTML = data.stores.map((store, index) => createRatingCard(store, index)).join('');
    
  } catch (error) {
    console.error('Error loading rating:', error);
  }
}

function createRatingCard(store, index) {
  const medals = ['🥇', '🥈', '🥉'];
  const positionClass = index === 0 ? 'gold' : index === 1 ? 'silver' : index === 2 ? 'bronze' : '';
  
  return `
    <div class="rating-card">
      <div class="rating-position ${positionClass}">
        ${medals[index] || index + 1}
      </div>
      <div class="rating-info">
        <div class="rating-store-name">${store.name}</div>
        <div class="rating-stats">
          <span>📦 ${store.count} aksiya</span>
          <span>⭐ ${store.avg_discount.toFixed(0)}% o'rtacha</span>
        </div>
      </div>
      <div class="rating-discount">${store.max_discount}%</div>
    </div>
  `;
}

// ─────────────────────────────────────
// Filters
// ─────────────────────────────────────
document.querySelectorAll('.filter-btn[data-category]').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn[data-category]').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    loadPromotions({ category: btn.dataset.category });
  });
});

document.querySelectorAll('.filter-btn[data-store]').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.classList.toggle('active');
    const activeStores = [...document.querySelectorAll('.filter-btn[data-store].active')]
      .map(b => b.dataset.store);
    loadPromotions({ stores: activeStores.join(',') });
  });
});

// Search
let searchTimeout;
document.getElementById('searchInput').addEventListener('input', (e) => {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    loadPromotions({ search: e.target.value });
  }, 300);
});

// ─────────────────────────────────────
// Initialize
// ─────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  loadPromotions();
  loadRating();
});
```

---

### 🔌 API ENDPOINTS

Backend da quyidagi API endpointlar bo'lishi kerak:

```python
# src/api/routes.py

from fastapi import APIRouter, Query
from typing import Optional, List

router = APIRouter(prefix="/api")

@router.get("/promotions")
async def get_promotions(
    category: Optional[str] = None,
    stores: Optional[str] = None,
    search: Optional[str] = None,
    status: str = "active",
    limit: int = Query(default=20, le=100),
    offset: int = 0
):
    """Aksiyalar ro'yxatini olish"""
    # Filter logic here
    pass

@router.get("/promotions/{promo_id}")
async def get_promotion(promo_id: int):
    """Bitta aksiya ma'lumotlari"""
    pass

@router.get("/rating/weekly")
async def get_weekly_rating():
    """Haftalik reyting"""
    pass

@router.get("/rating/monthly")
async def get_monthly_rating():
    """Oylik reyting"""
    pass

@router.get("/stores")
async def get_stores():
    """Do'konlar ro'yxati"""
    pass

@router.get("/stats")
async def get_stats():
    """Umumiy statistika"""
    pass
```
