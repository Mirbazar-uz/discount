<script setup lang="ts">
const props = defineProps<{
  totalPromotions: number
  totalStores: number
  maxDiscount: number
}>()

const animatedPromos = ref(0)
const animatedStores = ref(0)
const animatedDiscount = ref(0)
const mounted = ref(false)

function animateCount(target: number, current: Ref<number>, duration: number = 1500) {
  if (!import.meta.client) {
    current.value = target
    return
  }

  const start = 0
  const startTime = Date.now()

  function update() {
    const elapsed = Date.now() - startTime
    const progress = Math.min(elapsed / duration, 1)
    const eased = 1 - Math.pow(1 - progress, 3)
    current.value = Math.round(start + (target - start) * eased)

    if (progress < 1) {
      requestAnimationFrame(update)
    }
  }

  requestAnimationFrame(update)
}

onMounted(() => {
  mounted.value = true
  if (props.totalPromotions > 0) animateCount(props.totalPromotions, animatedPromos)
  if (props.totalStores > 0) animateCount(props.totalStores, animatedStores)
  if (props.maxDiscount > 0) animateCount(props.maxDiscount, animatedDiscount)
})

watch(() => props.totalPromotions, (val) => {
  if (val > 0 && mounted.value) animateCount(val, animatedPromos)
  else animatedPromos.value = val
})

watch(() => props.totalStores, (val) => {
  if (val > 0 && mounted.value) animateCount(val, animatedStores)
  else animatedStores.value = val
})

watch(() => props.maxDiscount, (val) => {
  if (val > 0 && mounted.value) animateCount(val, animatedDiscount)
  else animatedDiscount.value = val
})
</script>

<template>
  <section class="relative min-h-[90vh] flex items-center overflow-hidden pt-20 pb-10">
    <!-- Animated background orbs -->
    <div class="absolute inset-0 overflow-hidden">
      <div
        class="absolute w-[500px] h-[500px] bg-purple-600/20 rounded-full blur-[120px] -top-32 -left-32 animate-float"
      ></div>
      <div
        class="absolute w-[400px] h-[400px] bg-cyan-500/15 rounded-full blur-[100px] -bottom-20 -right-20 animate-float-reverse"
      ></div>
      <div
        class="absolute w-[300px] h-[300px] bg-purple-500/10 rounded-full blur-[80px] top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
        style="animation: float 30s ease-in-out infinite"
      ></div>
      <!-- Grid pattern -->
      <div
        class="absolute inset-0 opacity-[0.03]"
        style="
          background-image: linear-gradient(rgba(255, 255, 255, 0.5) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.5) 1px, transparent 1px);
          background-size: 60px 60px;
        "
      ></div>
    </div>

    <div class="relative z-10 max-w-7xl mx-auto px-5 w-full">
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <!-- Left: Text content -->
        <div class="animate-fade-in-up">
          <div
            class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/[0.07] backdrop-blur-xl border border-white/[0.15] text-sm text-gray-300 mb-8"
          >
            <span class="w-2 h-2 bg-green-400 rounded-full" style="animation: blink 1.5s ease-in-out infinite"></span>
            <span>{{ totalPromotions }} ta aktiv aksiya</span>
          </div>

          <h1 class="text-5xl md:text-6xl lg:text-7xl font-extrabold text-white mb-6 tracking-tight" style="line-height: 1.05">
            <span class="gradient-text">Barcha</span>
            <br />
            <span class="gradient-text">chegirmalar</span>
            <br />
            <span class="text-white">bir joyda</span>
          </h1>

          <p class="text-lg md:text-xl text-gray-400 mb-10 max-w-lg leading-relaxed">
            O'zbekistondagi eng yaxshi aksiyalarni o'tkazib yubormang!
            Texnomart, Asaxiy, Mediapark va boshqa do'konlar.
          </p>

          <div class="flex flex-wrap gap-4 mb-12">
            <a
              href="https://t.me/mirbazar_uz"
              target="_blank"
              class="btn-primary text-lg"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
              </svg>
              Telegram kanal
            </a>
            <a href="#promotions" class="btn-secondary text-lg">
              Aksiyalarni ko'rish
            </a>
          </div>
        </div>

        <!-- Right: Floating promo card visual -->
        <div class="hidden lg:block animate-fade-in-up" style="animation-delay: 0.2s">
          <div class="relative">
            <!-- Glow effect behind card -->
            <div class="absolute -inset-4 bg-gradient-to-br from-purple-500/20 to-cyan-500/20 rounded-3xl blur-2xl"></div>

            <!-- Floating card -->
            <div class="relative glass-card p-8 animate-glow-pulse">
              <div class="flex items-center justify-between mb-6">
                <span class="badge-discount">-70%</span>
                <span class="text-gray-400 text-sm">Bugungi eng yaxshi</span>
              </div>
              <div class="space-y-4">
                <div class="h-3 w-3/4 rounded-full bg-white/10"></div>
                <div class="h-3 w-1/2 rounded-full bg-white/5"></div>
              </div>
              <div class="mt-6 flex items-center gap-3">
                <span class="text-gray-500 line-through text-lg">3 990 000</span>
                <span class="text-green-400 font-bold text-2xl">1 990 000 so'm</span>
              </div>
              <div class="mt-4 flex items-center gap-2 text-orange-400 text-sm">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>
                </svg>
                2 kun qoldi
              </div>

              <!-- Small floating badges -->
              <div class="absolute -top-4 -right-4 w-16 h-16 bg-gradient-to-br from-purple-500 to-purple-700 rounded-2xl flex items-center justify-center text-2xl shadow-lg rotate-12" style="animation: float 8s ease-in-out infinite">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                  <path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>
                </svg>
              </div>
              <div class="absolute -bottom-3 -left-3 w-12 h-12 bg-gradient-to-br from-cyan-500 to-cyan-700 rounded-xl flex items-center justify-center text-lg shadow-lg -rotate-12" style="animation: float 10s ease-in-out infinite reverse">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Stats bar -->
      <div
        class="mt-12 lg:mt-16 glass-card p-6 md:p-8 max-w-3xl mx-auto lg:mx-0"
      >
        <div class="flex justify-between items-center hero-stats">
          <div class="text-center flex-1">
            <span class="block text-3xl md:text-4xl font-extrabold text-white">{{ animatedPromos }}</span>
            <span class="text-sm text-gray-400 mt-1">Aksiyalar</span>
          </div>
          <div class="w-px h-12 bg-white/10 stat-divider"></div>
          <div class="text-center flex-1">
            <span class="block text-3xl md:text-4xl font-extrabold text-white">{{ animatedStores }}</span>
            <span class="text-sm text-gray-400 mt-1">Do'konlar</span>
          </div>
          <div class="w-px h-12 bg-white/10 stat-divider"></div>
          <div class="text-center flex-1">
            <span class="block text-3xl md:text-4xl font-extrabold gradient-text">{{ animatedDiscount }}%</span>
            <span class="text-sm text-gray-400 mt-1">Gacha chegirma</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
