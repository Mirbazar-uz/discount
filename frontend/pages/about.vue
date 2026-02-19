<script setup lang="ts">
const { t } = useI18n()
const { getStats } = usePromotion()

const stats = ref({ total_promotions: 0, active_promotions: 0, total_stores: 0, max_discount: 0 })

onMounted(async () => {
  try {
    stats.value = await getStats()
  } catch {
    // keep defaults
  }
})

useHead({
  title: () => t('seo.about_title'),
  meta: [
    { name: 'description', content: () => t('seo.about_description') },
  ],
})
</script>

<template>
  <div class="pt-28 pb-20">
    <div class="max-w-4xl mx-auto px-5">
      <!-- Hero -->
      <div class="text-center mb-16">
        <div
          class="w-20 h-20 mx-auto mb-6 bg-gradient-to-br from-purple-500 to-cyan-500 rounded-2xl flex items-center justify-center shadow-lg"
          style="box-shadow: 0 0 40px rgba(124, 58, 237, 0.3)"
        >
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
            <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
          </svg>
        </div>
        <h1 class="section-title mb-4">{{ t('about.title') }}</h1>
        <p class="text-gray-400 text-lg max-w-2xl mx-auto leading-relaxed">
          {{ t('about.subtitle') }}
        </p>
      </div>

      <div class="space-y-10">
        <!-- Stats -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div class="glass-card p-6 text-center">
            <p class="text-3xl font-bold gradient-text">{{ stats.total_stores || '10+' }}</p>
            <p class="text-gray-500 text-sm mt-1">{{ t('about.stats_stores') }}</p>
          </div>
          <div class="glass-card p-6 text-center">
            <p class="text-3xl font-bold gradient-text">{{ stats.active_promotions || '100+' }}</p>
            <p class="text-gray-500 text-sm mt-1">{{ t('about.stats_active') }}</p>
          </div>
          <div class="glass-card p-6 text-center">
            <p class="text-3xl font-bold gradient-text">{{ stats.max_discount || 70 }}%</p>
            <p class="text-gray-500 text-sm mt-1">{{ t('about.stats_max_discount') }}</p>
          </div>
          <div class="glass-card p-6 text-center">
            <p class="text-3xl font-bold gradient-text">24/7</p>
            <p class="text-gray-500 text-sm mt-1">{{ t('about.stats_updates') }}</p>
          </div>
        </div>

        <!-- Mission -->
        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('about.mission_title') }}</h2>
          <p class="text-gray-400 leading-relaxed">
            {{ t('about.mission_text') }}
          </p>
        </section>

        <!-- How it works -->
        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('about.how_title') }}</h2>
          <div class="space-y-6 mt-6">
            <div class="flex items-start gap-4">
              <div class="w-10 h-10 shrink-0 bg-purple-500/20 border border-purple-500/30 rounded-xl flex items-center justify-center text-purple-400 font-bold">
                1
              </div>
              <div>
                <h3 class="text-white font-medium mb-1">{{ t('about.step1_title') }}</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                  {{ t('about.step1_text') }}
                </p>
              </div>
            </div>
            <div class="flex items-start gap-4">
              <div class="w-10 h-10 shrink-0 bg-purple-500/20 border border-purple-500/30 rounded-xl flex items-center justify-center text-purple-400 font-bold">
                2
              </div>
              <div>
                <h3 class="text-white font-medium mb-1">{{ t('about.step2_title') }}</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                  {{ t('about.step2_text') }}
                </p>
              </div>
            </div>
            <div class="flex items-start gap-4">
              <div class="w-10 h-10 shrink-0 bg-cyan-500/20 border border-cyan-500/30 rounded-xl flex items-center justify-center text-cyan-400 font-bold">
                3
              </div>
              <div>
                <h3 class="text-white font-medium mb-1">{{ t('about.step3_title') }}</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                  {{ t('about.step3_text') }}
                </p>
              </div>
            </div>
            <div class="flex items-start gap-4">
              <div class="w-10 h-10 shrink-0 bg-cyan-500/20 border border-cyan-500/30 rounded-xl flex items-center justify-center text-cyan-400 font-bold">
                4
              </div>
              <div>
                <h3 class="text-white font-medium mb-1">{{ t('about.step4_title') }}</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                  {{ t('about.step4_text') }}
                </p>
              </div>
            </div>
          </div>
        </section>

        <!-- Stores -->
        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('about.stores_title') }}</h2>
          <p class="text-gray-400 leading-relaxed mb-4">
            {{ t('about.stores_text') }}
          </p>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="store in ['Texnomart', 'Asaxiy', 'Mediapark', 'Korzinka', 'Makro', 'Havas', 'Goodzone', 'Elmakon']"
              :key="store"
              class="px-4 py-2 bg-white/[0.05] border border-white/10 rounded-xl text-sm text-gray-300"
            >
              {{ store }}
            </span>
          </div>
        </section>

        <!-- CTA -->
        <section class="glass-card p-8 text-center">
          <h2 class="text-xl font-semibold text-white mb-3">{{ t('about.cta_title') }}</h2>
          <p class="text-gray-400 mb-6">{{ t('about.cta_text') }}</p>
          <a
            href="https://t.me/mirbazar_uz"
            target="_blank"
            rel="noopener"
            class="btn-primary"
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
            </svg>
            {{ t('about.cta_button') }}
          </a>
        </section>
      </div>
    </div>
  </div>
</template>
