<script setup lang="ts">
const { t } = useI18n()
const localePath = useLocalePath()
const { getPromotions, getWeeklyRating, getStats } = usePromotion()
const { fetchApi } = useApi()

const selectedCategory = ref('all')
const searchQuery = ref('')
const promotions = ref<any[]>([])
const totalPromotions = ref(0)
const rating = ref<any[]>([])
const stores = ref<any[]>([])
const stats = ref({ total_promotions: 0, active_promotions: 0, total_stores: 0, max_discount: 0 })

const loading = ref(true)
const loadingRating = ref(true)
const loadingStores = ref(true)
const mobileSearchOpen = ref(false)
const mobileSearchInput = ref<HTMLInputElement | null>(null)

function openMobileSearch() {
  mobileSearchOpen.value = true
  nextTick(() => {
    mobileSearchInput.value?.focus()
  })
}

function closeMobileSearch() {
  mobileSearchOpen.value = false
  searchQuery.value = ''
}

let searchTimeout: ReturnType<typeof setTimeout> | null = null

async function loadPromotions() {
  loading.value = true
  try {
    const params: Record<string, string> = {}
    if (selectedCategory.value !== 'all') {
      params.category = selectedCategory.value
    }
    if (searchQuery.value) {
      params.search = searchQuery.value
    }
    const data = await getPromotions(params)
    promotions.value = data.promotions
    totalPromotions.value = data.total
  } catch {
    promotions.value = []
  } finally {
    loading.value = false
  }
}

async function loadRating() {
  loadingRating.value = true
  try {
    const data = await getWeeklyRating()
    rating.value = data.stores
  } catch {
    rating.value = []
  } finally {
    loadingRating.value = false
  }
}

async function loadStores() {
  loadingStores.value = true
  try {
    stores.value = await fetchApi<any[]>('/stores')
  } catch {
    stores.value = []
  } finally {
    loadingStores.value = false
  }
}

async function loadStats() {
  try {
    stats.value = await getStats()
  } catch {
    // keep defaults
  }
}

watch(selectedCategory, () => {
  loadPromotions()
})

watch(searchQuery, () => {
  if (searchTimeout) clearTimeout(searchTimeout)
  searchTimeout = setTimeout(() => {
    loadPromotions()
  }, 300)
})

onMounted(() => {
  loadPromotions()
  loadRating()
  loadStats()
  loadStores()
})

useSeoMeta({
  title: () => t('seo.home_title'),
  ogTitle: () => t('seo.home_title'),
  description: () => t('seo.home_description'),
  ogDescription: () => t('seo.home_description'),
  ogUrl: 'https://mirbazar.uz',
  ogImage: 'https://mirbazar.uz/og-image.png',
  twitterCard: 'summary_large_image',
  twitterTitle: () => t('seo.home_title'),
  twitterDescription: () => t('seo.home_description'),
  twitterImage: 'https://mirbazar.uz/og-image.png',
})

useHead({
  link: [{ rel: 'canonical', href: 'https://mirbazar.uz' }],
})
</script>

<template>
  <div>
    <HeroSection
      :total-promotions="stats.active_promotions || totalPromotions"
      :total-stores="stats.total_stores || 10"
      :max-discount="stats.max_discount || 70"
    />

    <!-- Rating Section -->
    <section id="rating" class="py-20 relative">
      <div class="absolute inset-0 bg-gradient-to-b from-purple-500/[0.03] to-transparent pointer-events-none"></div>
      <div class="max-w-7xl mx-auto px-5 relative">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-10">
          <div>
            <h2 class="section-title">{{ t('home.weekly_rating') }}</h2>
            <p class="text-gray-500 text-sm mt-2">{{ t('home.top_discount_stores') }}</p>
          </div>
          <div class="badge-live">
            <span class="w-2 h-2 bg-green-400 rounded-full" style="animation: blink 1.5s ease-in-out infinite"></span>
            {{ t('home.updating') }}
          </div>
        </div>

        <!-- Rating skeleton -->
        <div v-if="loadingRating" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div v-for="i in 4" :key="i" class="glass-card p-5 flex items-center gap-4">
            <div class="w-12 h-12 rounded-xl skeleton"></div>
            <div class="flex-1 space-y-2">
              <div class="h-4 w-24 skeleton rounded"></div>
              <div class="h-3 w-16 skeleton rounded"></div>
            </div>
          </div>
        </div>

        <div v-else-if="rating.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <RatingBadge
            v-for="(store, index) in rating"
            :key="store.slug"
            :store="store"
            :position="index"
          />
        </div>

        <div v-else class="glass-card p-10 text-center">
          <svg class="mx-auto mb-3 text-gray-600" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
          </svg>
          <p class="text-gray-500 text-sm">{{ t('home.no_rating_data') }}</p>
        </div>
      </div>
    </section>

    <!-- Filters -->
    <section
      id="promotions"
      class="py-3 md:py-6 sticky top-[56px] z-40 border-b border-white/[0.06] transition-all duration-300"
      style="background: rgba(10, 10, 15, 0.92); backdrop-filter: blur(20px) saturate(180%)"
    >
      <div class="max-w-7xl mx-auto px-4 md:px-5">
        <!-- Desktop: categories + search side by side -->
        <div class="hidden md:flex gap-4 items-center">
          <CategoryFilter v-model="selectedCategory" />
          <SearchBar v-model="searchQuery" />
        </div>

        <!-- Mobile: compact single row -->
        <div class="flex md:hidden items-center gap-2">
          <!-- Search expanded state -->
          <template v-if="mobileSearchOpen">
            <div class="flex-1 relative">
              <svg
                class="absolute left-3 top-1/2 -translate-y-1/2 text-purple-400"
                width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              >
                <circle cx="11" cy="11" r="8" /><path d="m21 21-4.35-4.35" />
              </svg>
              <input
                ref="mobileSearchInput"
                type="text"
                :value="searchQuery"
                :placeholder="t('search.placeholder')"
                class="w-full py-2.5 pl-9 pr-4 rounded-xl bg-white/[0.05] border border-purple-500/40 text-white text-sm placeholder-gray-500 outline-none transition-all duration-300 focus:border-purple-500/60 focus:shadow-[0_0_20px_rgba(124,58,237,0.15)]"
                @input="(e: Event) => searchQuery = (e.target as HTMLInputElement).value"
              />
            </div>
            <button
              class="w-9 h-9 shrink-0 flex items-center justify-center rounded-xl bg-white/[0.05] border border-white/10 text-gray-400 hover:text-white transition-all"
              @click="closeMobileSearch"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 6L6 18M6 6l12 12"/>
              </svg>
            </button>
          </template>

          <!-- Default state: categories + search icon -->
          <template v-else>
            <CategoryFilter v-model="selectedCategory" class="flex-1 min-w-0" />
            <button
              class="w-9 h-9 shrink-0 flex items-center justify-center rounded-xl bg-white/[0.05] border border-white/10 text-gray-400 hover:text-purple-400 hover:border-purple-500/40 transition-all duration-200"
              @click="openMobileSearch"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8" /><path d="m21 21-4.35-4.35" />
              </svg>
            </button>
          </template>
        </div>
      </div>
    </section>

    <!-- Promotions Grid -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-5">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-10">
          <div class="flex items-center gap-4">
            <h2 class="section-title">{{ t('home.current_promotions') }}</h2>
            <span class="text-gray-500 text-sm">{{ t('home.count_promotions', { count: totalPromotions }) }}</span>
          </div>
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

        <!-- Empty state -->
        <div v-else class="glass-card p-16 text-center">
          <div
            class="w-16 h-16 mx-auto mb-5 rounded-2xl flex items-center justify-center"
            style="background: linear-gradient(135deg, rgba(124,58,237,0.15) 0%, rgba(0,212,255,0.1) 100%)"
          >
            <svg class="text-purple-400" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
            </svg>
          </div>
          <p class="text-lg text-gray-300 mb-2 font-medium">{{ t('home.no_promotions_found') }}</p>
          <p class="text-sm text-gray-500">{{ t('home.try_other_category') }}</p>
        </div>
      </div>
    </section>

    <!-- Stores Section -->
    <section id="stores" class="py-16 relative">
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-cyan-500/[0.02] to-transparent pointer-events-none"></div>
      <div class="max-w-7xl mx-auto px-5 relative">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-10">
          <div>
            <h2 class="section-title">{{ t('home.stores') }}</h2>
            <p class="text-gray-500 text-sm mt-2">{{ t('home.all_stores_promotions') }}</p>
          </div>
        </div>

        <!-- Stores skeleton -->
        <div v-if="loadingStores" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div v-for="i in 6" :key="i" class="glass-card p-5 flex items-center gap-4">
            <div class="w-12 h-12 rounded-xl skeleton"></div>
            <div class="flex-1 space-y-2">
              <div class="h-4 w-28 skeleton rounded"></div>
              <div class="h-3 w-16 skeleton rounded"></div>
            </div>
          </div>
        </div>

        <div v-else-if="stores.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <StoreCard
            v-for="store in stores"
            :key="store.id"
            :store="store"
          />
        </div>

        <div v-else class="glass-card p-10 text-center">
          <svg class="mx-auto mb-3 text-gray-600" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M3 3h18l-2 13H5L3 3zm0 0l-1-1M7 16v5M17 16v5M2 21h20"/>
          </svg>
          <p class="text-gray-500 text-sm">{{ t('home.no_stores_data') }}</p>
        </div>
      </div>
    </section>

    <TelegramCTA />
  </div>
</template>
