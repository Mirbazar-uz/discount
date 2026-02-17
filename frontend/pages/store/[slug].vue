<script setup lang="ts">
const route = useRoute()
const slug = route.params.slug as string

const { getPromotions } = usePromotion()

const { data, error, status } = await useAsyncData(
  `store-${slug}`,
  () => getPromotions({ stores: slug }),
)

const promotions = computed(() => data.value?.promotions ?? [])
const total = computed(() => data.value?.total ?? 0)
const storeName = computed(() => {
  if (promotions.value.length > 0) return promotions.value[0].store
  return slug
})

const storeTitle = computed(() => `${storeName.value} aksiyalari — Mirbazar`)
const storeDescription = computed(
  () => `${storeName.value} do'konining barcha aksiyalari va chegirmalari. Mirbazar.uz da eng yaxshi narxlar.`
)
const storeUrl = computed(() => `https://mirbazar.uz/store/${slug}`)

useSeoMeta({
  title: storeTitle,
  ogTitle: storeTitle,
  description: storeDescription,
  ogDescription: storeDescription,
  ogUrl: storeUrl,
  ogImage: 'https://mirbazar.uz/og-image.png',
  twitterCard: 'summary_large_image',
  twitterTitle: storeTitle,
  twitterDescription: storeDescription,
  twitterImage: 'https://mirbazar.uz/og-image.png',
})

useHead({
  link: [{ rel: 'canonical', href: storeUrl }],
})
</script>

<template>
  <div class="pt-24 pb-16">
    <div class="max-w-7xl mx-auto px-5">
      <!-- Header -->
      <div class="mb-10">
        <NuxtLink
          to="/"
          class="inline-flex items-center gap-2 text-gray-400 hover:text-purple-400 text-sm transition-colors mb-6 group"
        >
          <svg class="transition-transform group-hover:-translate-x-1" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M15 18l-6-6 6-6"/>
          </svg>
          Bosh sahifa
        </NuxtLink>

        <div class="flex items-center gap-4">
          <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-purple-500 to-cyan-500 flex items-center justify-center text-2xl font-bold text-white shadow-lg">
            {{ storeName.charAt(0) }}
          </div>
          <div>
            <h1 class="text-3xl md:text-4xl font-bold text-white">
              {{ storeName }}
            </h1>
            <p class="text-gray-500 mt-1">{{ total }} ta aksiya topildi</p>
          </div>
        </div>
      </div>

      <!-- Loading skeleton -->
      <div v-if="status === 'pending'" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <PromotionSkeleton v-for="i in 6" :key="i" />
      </div>

      <!-- Promotions -->
      <div
        v-else-if="promotions.length > 0"
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
            <path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>
          </svg>
        </div>
        <p class="text-lg text-gray-300 mb-2 font-medium">Hozircha bu do'konda aksiyalar yo'q</p>
        <p class="text-sm text-gray-500 mb-6">Tez orada yangi aksiyalar qo'shiladi</p>
        <NuxtLink to="/" class="inline-flex items-center gap-2 text-purple-400 hover:text-cyan-400 text-sm transition-colors font-medium">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
          Bosh sahifaga qaytish
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
