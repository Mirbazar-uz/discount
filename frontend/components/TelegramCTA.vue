<template>
  <section class="py-20">
    <div class="max-w-3xl mx-auto px-5">
      <div
        class="relative overflow-hidden rounded-3xl border border-white/10"
        style="background: linear-gradient(135deg, rgba(124,58,237,0.1) 0%, rgba(0,212,255,0.05) 100%)"
      >
        <!-- Background orbs -->
        <div class="absolute -top-20 -right-20 w-60 h-60 bg-purple-500/10 rounded-full blur-[80px]"></div>
        <div class="absolute -bottom-20 -left-20 w-60 h-60 bg-cyan-500/10 rounded-full blur-[80px]"></div>

        <div class="relative z-10 p-10 md:p-14 text-center">
          <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-purple-500 to-cyan-500 rounded-2xl flex items-center justify-center shadow-lg">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="white">
              <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
            </svg>
          </div>

          <h2 class="text-3xl md:text-4xl font-bold text-white mb-4">
            Chegirmalarni birinchi bo'lib bilmoqchimisiz?
          </h2>
          <p class="text-gray-400 text-lg mb-8 max-w-lg mx-auto">
            Telegram kanalimizga obuna bo'ling va eng yaxshi aksiyalarni o'tkazib yubormang!
          </p>

          <a
            href="https://t.me/mirbazar_uz"
            target="_blank"
            class="btn-primary text-lg px-10 py-5 mb-8"
          >
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
            </svg>
            @mirbazar_uz ga obuna bo'ling
          </a>

          <div class="flex flex-col sm:flex-row justify-center gap-6 text-gray-400 text-sm">
            <span class="flex items-center gap-2">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              Kunlik yangi aksiyalar
            </span>
            <span class="flex items-center gap-2">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              Eng arzon narxlar
            </span>
            <span class="flex items-center gap-2">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              Haftalik reyting
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
