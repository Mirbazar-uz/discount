<script setup lang="ts">
const { t } = useI18n()
const localePath = useLocalePath()
const route = useRoute()
const slug = route.params.slug as string

const { getPromotions } = usePromotion()

const promotions = ref<any[]>([])
const total = ref(0)
const loading = ref(true)

const categoryName = computed(() => t(`categories.${slug}`) !== `categories.${slug}` ? t(`categories.${slug}`) : slug)

async function loadData() {
  loading.value = true
  try {
    const data = await getPromotions({ category: slug })
    promotions.value = data.promotions
    total.value = data.total
  } catch {
    promotions.value = []
  } finally {
    loading.value = false
  }
}

onMounted(loadData)

const categoryTitle = computed(() => `${categoryName.value} — Mirbazar`)
const categoryDescription = computed(
  () => `${categoryName.value} — Mirbazar.uz`
)
const categoryUrl = computed(() => `https://mirbazar.uz/category/${slug}`)

useSeoMeta({
  title: categoryTitle,
  ogTitle: categoryTitle,
  description: categoryDescription,
  ogDescription: categoryDescription,
  ogUrl: categoryUrl,
  ogImage: 'https://mirbazar.uz/og-image.png',
  twitterCard: 'summary_large_image',
  twitterTitle: categoryTitle,
  twitterDescription: categoryDescription,
  twitterImage: 'https://mirbazar.uz/og-image.png',
})

useHead({
  link: [{ rel: 'canonical', href: categoryUrl }],
})
</script>

<template>
  <div class="pt-24 pb-16">
    <div class="max-w-7xl mx-auto px-5">
      <!-- Header -->
      <div class="mb-10">
        <NuxtLink
          :to="localePath('/')"
          class="inline-flex items-center gap-2 text-gray-400 hover:text-purple-400 text-sm transition-colors mb-6 group"
        >
          <svg class="transition-transform group-hover:-translate-x-1" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M15 18l-6-6 6-6"/>
          </svg>
          {{ t('category.home') }}
        </NuxtLink>

        <h1 class="text-3xl md:text-4xl font-bold text-white">
          {{ categoryName }}
        </h1>
        <p class="text-gray-500 mt-2">{{ t('category.promotions_found', { count: total }) }}</p>
      </div>

      <!-- Loading skeleton -->
      <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <PromotionSkeleton v-for="i in 6" :key="i" />
      </div>

      <!-- Promotions -->
      <div
        v-else-if="promotions.length"
        class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
      >
        <PromotionCard
          v-for="promo in promotions"
          :key="promo.id"
          :promotion="promo"
        />
      </div>

      <!-- Empty -->
      <div v-else class="glass-card p-16 text-center">
        <div
          class="w-16 h-16 mx-auto mb-5 rounded-2xl flex items-center justify-center"
          style="background: linear-gradient(135deg, rgba(124,58,237,0.15) 0%, rgba(0,212,255,0.1) 100%)"
        >
          <svg class="text-purple-400" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
          </svg>
        </div>
        <p class="text-lg text-gray-300 mb-2 font-medium">{{ t('category.no_promotions') }}</p>
        <p class="text-sm text-gray-500 mb-6">{{ t('category.try_other') }}</p>
        <NuxtLink :to="localePath('/')" class="inline-flex items-center gap-2 text-purple-400 hover:text-cyan-400 text-sm transition-colors font-medium">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
          {{ t('category.go_home') }}
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
