<script setup lang="ts">
const { t } = useI18n()

useHead({
  title: () => t('seo.terms_title'),
  meta: [
    { name: 'description', content: () => t('seo.terms_description') },
  ],
})
</script>

<template>
  <div class="pt-28 pb-20">
    <div class="max-w-4xl mx-auto px-5">
      <h1 class="section-title mb-4">{{ t('terms.title') }}</h1>
      <p class="text-gray-500 text-sm mb-12">{{ t('terms.last_updated') }}</p>

      <div class="space-y-10">
        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('terms.s1_title') }}</h2>
          <p class="text-gray-400 leading-relaxed">
            {{ t('terms.s1_text') }}
          </p>
        </section>

        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('terms.s2_title') }}</h2>
          <p class="text-gray-400 leading-relaxed mb-4">{{ t('terms.s2_intro') }}</p>
          <ul class="space-y-3 text-gray-400">
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s2_item1') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s2_item2') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s2_item3') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s2_item4') }}</span>
            </li>
          </ul>
        </section>

        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('terms.s3_title') }}</h2>
          <p class="text-gray-400 leading-relaxed mb-4">
            {{ t('terms.s3_intro') }}
          </p>
          <ul class="space-y-3 text-gray-400">
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-red-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s3_item1') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-red-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s3_item2') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-red-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s3_item3') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-red-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s3_item4') }}</span>
            </li>
          </ul>
        </section>

        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('terms.s4_title') }}</h2>
          <p class="text-gray-400 leading-relaxed">
            {{ t('terms.s4_text') }}
          </p>
        </section>

        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('terms.s5_title') }}</h2>
          <p class="text-gray-400 leading-relaxed mb-4">{{ t('terms.s5_intro') }}</p>
          <ul class="space-y-3 text-gray-400">
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s5_item1') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s5_item2') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-2 shrink-0"></span>
              <span>{{ t('terms.s5_item3') }}</span>
            </li>
          </ul>
        </section>

        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('terms.s6_title') }}</h2>
          <p class="text-gray-400 leading-relaxed">
            {{ t('terms.s6_text') }}
          </p>
        </section>

        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('terms.s7_title') }}</h2>
          <p class="text-gray-400 leading-relaxed">
            {{ t('terms.s7_text') }}
          </p>
        </section>

        <section class="glass-card p-8">
          <h2 class="text-xl font-semibold text-white mb-4">{{ t('terms.s8_title') }}</h2>
          <p class="text-gray-400 leading-relaxed">
            {{ t('terms.s8_text') }}
          </p>
          <div class="mt-4 flex flex-wrap gap-3">
            <a
              href="https://t.me/iportaluz_bot"
              target="_blank"
              rel="noopener"
              class="inline-flex items-center gap-2 px-5 py-2.5 bg-white/[0.05] border border-white/10 rounded-xl text-sm text-purple-400 hover:bg-purple-500/10 hover:border-purple-500/30 transition-all"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
              </svg>
              @iportaluz_bot
            </a>
            <a
              href="mailto:info@mirbazar.uz"
              class="inline-flex items-center gap-2 px-5 py-2.5 bg-white/[0.05] border border-white/10 rounded-xl text-sm text-cyan-400 hover:bg-cyan-500/10 hover:border-cyan-500/30 transition-all"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
              </svg>
              info@mirbazar.uz
            </a>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>
