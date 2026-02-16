<script setup lang="ts">
useHead({
  title: 'Bog\'lanish — Mirbazar.uz',
  meta: [
    { name: 'description', content: 'Mirbazar.uz bilan bog\'lanish. Telegram bot, kanal, Instagram va email orqali murojaat qiling.' },
  ],
})
</script>

<template>
  <div class="pt-28 pb-20">
    <div class="max-w-4xl mx-auto px-5">
      <!-- Hero -->
      <div class="text-center mb-16">
        <h1 class="section-title mb-4">Biz bilan bog'lanish</h1>
        <p class="text-gray-400 text-lg max-w-2xl mx-auto leading-relaxed">
          Savollaringiz, takliflaringiz yoki hamkorlik uchun biz bilan bog'laning
        </p>
      </div>

      <div class="space-y-10">
        <!-- Aloqa kanallari -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Telegram Bot -->
          <a
            href="https://t.me/iportaluz_bot"
            target="_blank"
            rel="noopener"
            class="glass-card p-8 group hover:border-purple-500/30 transition-all duration-300"
          >
            <div class="w-14 h-14 bg-purple-500/20 border border-purple-500/30 rounded-2xl flex items-center justify-center mb-5 group-hover:bg-purple-500/30 transition-colors">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" stroke-width="2">
                <path d="M12 8V4H8"/><rect x="4" y="8" width="16" height="12" rx="2"/>
                <path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>
              </svg>
            </div>
            <h3 class="text-white font-semibold text-lg mb-2">Telegram Bot</h3>
            <p class="text-gray-400 text-sm mb-4 leading-relaxed">
              Asosiy murojaat kanali. Savollaringizga tezkor javob oling.
            </p>
            <span class="text-purple-400 text-sm font-medium">@iportaluz_bot</span>
          </a>

          <!-- Telegram Kanal -->
          <a
            href="https://t.me/mirbazar_uz"
            target="_blank"
            rel="noopener"
            class="glass-card p-8 group hover:border-cyan-500/30 transition-all duration-300"
          >
            <div class="w-14 h-14 bg-cyan-500/20 border border-cyan-500/30 rounded-2xl flex items-center justify-center mb-5 group-hover:bg-cyan-500/30 transition-colors">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="#67e8f9">
                <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
              </svg>
            </div>
            <h3 class="text-white font-semibold text-lg mb-2">Telegram kanal</h3>
            <p class="text-gray-400 text-sm mb-4 leading-relaxed">
              Kunlik chegirmalar va aksiyalar. Obuna bo'ling, o'tkazib yubormang.
            </p>
            <span class="text-cyan-400 text-sm font-medium">@mirbazar_uz</span>
          </a>

          <!-- Instagram -->
          <a
            href="https://instagram.com/mirbazar.uz"
            target="_blank"
            rel="noopener"
            class="glass-card p-8 group hover:border-pink-500/30 transition-all duration-300"
          >
            <div class="w-14 h-14 bg-pink-500/20 border border-pink-500/30 rounded-2xl flex items-center justify-center mb-5 group-hover:bg-pink-500/30 transition-colors">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="#f472b6">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>
            </div>
            <h3 class="text-white font-semibold text-lg mb-2">Instagram</h3>
            <p class="text-gray-400 text-sm mb-4 leading-relaxed">
              Chegirmalar rasmiy sahifasi. Chiroyli postlar va stories.
            </p>
            <span class="text-pink-400 text-sm font-medium">@mirbazar.uz</span>
          </a>

          <!-- Email -->
          <a
            href="mailto:info@mirbazar.uz"
            class="glass-card p-8 group hover:border-green-500/30 transition-all duration-300"
          >
            <div class="w-14 h-14 bg-green-500/20 border border-green-500/30 rounded-2xl flex items-center justify-center mb-5 group-hover:bg-green-500/30 transition-colors">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#4ade80" stroke-width="2">
                <rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
              </svg>
            </div>
            <h3 class="text-white font-semibold text-lg mb-2">Email</h3>
            <p class="text-gray-400 text-sm mb-4 leading-relaxed">
              Rasmiy yozishmalar va hamkorlik takliflari uchun.
            </p>
            <span class="text-green-400 text-sm font-medium">info@mirbazar.uz</span>
          </a>
        </div>

        <!-- FAQ -->
        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-6">Ko'p so'raladigan savollar</h2>
          <div class="space-y-6">
            <div>
              <h3 class="text-white font-medium mb-2">Chegirma ma'lumotlari qayerdan olinadi?</h3>
              <p class="text-gray-400 text-sm leading-relaxed">
                Barcha ma'lumotlar do'konlarning rasmiy Telegram kanallaridan avtomatik ravishda yig'iladi
                va sun'iy intellekt yordamida qayta ishlanadi.
              </p>
            </div>
            <div class="border-t border-white/[0.06] pt-6">
              <h3 class="text-white font-medium mb-2">Xizmat bepulmi?</h3>
              <p class="text-gray-400 text-sm leading-relaxed">
                Ha, Mirbazar.uz to'liq bepul xizmat. Barcha chegirmalarni sayt, Telegram va Instagram
                orqali bepul ko'rishingiz mumkin.
              </p>
            </div>
            <div class="border-t border-white/[0.06] pt-6">
              <h3 class="text-white font-medium mb-2">Hamkorlik qanday amalga oshiriladi?</h3>
              <p class="text-gray-400 text-sm leading-relaxed">
                Hamkorlik takliflari uchun
                <a href="https://t.me/iportaluz_bot" target="_blank" rel="noopener" class="text-purple-400 hover:text-purple-300 transition-colors">@iportaluz_bot</a>
                ga murojaat qiling.
              </p>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>
