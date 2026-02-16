<script setup lang="ts">
defineProps<{
  totalPromotions: number
  totalStores: number
  maxDiscount: number
}>()
</script>

<template>
  <section class="relative min-h-[80vh] flex items-center justify-center overflow-hidden pt-20">
    <div class="absolute inset-0">
      <div
        class="absolute w-96 h-96 bg-purple-500 rounded-full blur-3xl opacity-30 -top-20 -left-20 animate-float"
      ></div>
      <div
        class="absolute w-80 h-80 bg-cyan-500 rounded-full blur-3xl opacity-30 -bottom-20 -right-20"
        style="animation: float 15s ease-in-out infinite reverse"
      ></div>
      <div
        class="absolute inset-0 opacity-20"
        style="
          background-image: linear-gradient(
              rgba(255, 255, 255, 0.03) 1px,
              transparent 1px
            ),
            linear-gradient(
              90deg,
              rgba(255, 255, 255, 0.03) 1px,
              transparent 1px
            );
          background-size: 50px 50px;
        "
      ></div>
    </div>

    <div class="relative z-10 text-center max-w-4xl mx-auto px-6">
      <div
        class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/10 backdrop-blur-xl border border-white/20 text-sm text-gray-300 mb-8"
      >
        <span class="w-2 h-2 bg-green-400 rounded-full" style="animation: blink 1s ease-in-out infinite"></span>
        <span>{{ totalPromotions }} ta aktiv aksiya</span>
      </div>

      <h1 class="text-5xl md:text-7xl font-bold text-white mb-6" style="line-height: 1.1">
        <span class="gradient-text">Barcha chegirmalar</span>
        <br />
        bir joyda
      </h1>

      <p class="text-xl text-gray-400 mb-10 max-w-2xl mx-auto">
        O'zbekistondagi eng yaxshi aksiyalarni o'tkazib yubormang!
        <br />
        Texnomart, Asaxiy, Mediapark va boshqa do'konlar.
      </p>

      <div class="flex flex-wrap justify-center gap-4 mb-12">
        <a
          href="https://t.me/mirbazar_uz"
          target="_blank"
          class="flex items-center gap-2 px-8 py-4 rounded-full bg-gradient-to-r from-purple-500 to-cyan-500 text-white font-semibold text-lg hover:shadow-[0_0_30px_rgba(124,58,237,0.5)] transition-all duration-300 hover:scale-105 no-underline"
        >
          Telegram kanal
        </a>
        <a
          href="#promotions"
          class="flex items-center gap-2 px-8 py-4 rounded-full bg-white/10 backdrop-blur-xl border border-white/20 text-white font-semibold text-lg hover:bg-white/20 transition-all duration-300 no-underline"
        >
          Aksiyalarni ko'rish
        </a>
      </div>

      <div
        class="flex justify-center items-center gap-8 bg-white/5 backdrop-blur-xl rounded-2xl p-6 border border-white/10 max-w-lg mx-auto"
      >
        <div class="text-center">
          <span class="block text-3xl font-bold text-white">{{ totalPromotions }}</span>
          <span class="text-sm text-gray-400">Aksiyalar</span>
        </div>
        <div class="w-px h-12 bg-white/20"></div>
        <div class="text-center">
          <span class="block text-3xl font-bold text-white">{{ totalStores }}</span>
          <span class="text-sm text-gray-400">Do'konlar</span>
        </div>
        <div class="w-px h-12 bg-white/20"></div>
        <div class="text-center">
          <span class="block text-3xl font-bold text-white">{{ maxDiscount }}%</span>
          <span class="text-sm text-gray-400">Gacha chegirma</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@keyframes float {
  0%,
  100% {
    transform: translate(0, 0);
  }
  50% {
    transform: translate(30px, 30px);
  }
}
</style>
