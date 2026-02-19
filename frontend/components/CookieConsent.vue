<template>
  <Transition name="cookie-banner">
    <div
      v-if="showBanner"
      class="fixed bottom-0 left-0 right-0 z-50 p-4 md:p-6"
    >
      <div
        class="max-w-4xl mx-auto rounded-2xl border border-white/10 px-6 py-5 flex flex-col sm:flex-row items-start sm:items-center gap-4"
        style="background: rgba(13, 13, 20, 0.85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px)"
      >
        <div class="flex-1 text-sm text-gray-400 leading-relaxed">
          {{ t('cookie.text') }}
          <NuxtLink :to="localePath('/privacy')" class="text-purple-400 hover:text-purple-300 transition-colors underline underline-offset-2">
            {{ t('cookie.privacy_link') }}
          </NuxtLink>
        </div>
        <div class="flex gap-3 shrink-0">
          <button
            @click="handleConsent('essential')"
            class="px-4 py-2 text-sm text-gray-400 border border-white/10 rounded-xl hover:bg-white/5 transition-all duration-200"
          >
            {{ t('cookie.essential_only') }}
          </button>
          <button
            @click="handleConsent('all')"
            class="px-5 py-2 text-sm font-medium text-white bg-gradient-to-r from-purple-500 to-cyan-500 rounded-xl hover:shadow-[0_0_20px_rgba(124,58,237,0.3)] transition-all duration-200"
          >
            {{ t('cookie.accept_all') }}
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup lang="ts">
const { t } = useI18n()
const localePath = useLocalePath()
const showBanner = ref(false)

onMounted(() => {
  const consent = localStorage.getItem('cookie_consent')
  if (!consent) {
    showBanner.value = true
  }
})

function handleConsent(type: 'all' | 'essential') {
  localStorage.setItem('cookie_consent', type)
  showBanner.value = false
}
</script>

<style scoped>
.cookie-banner-enter-active,
.cookie-banner-leave-active {
  transition: transform 0.4s ease, opacity 0.4s ease;
}
.cookie-banner-enter-from,
.cookie-banner-leave-to {
  transform: translateY(100%);
  opacity: 0;
}
</style>
