<script setup lang="ts">
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

useHead({
  title: 'Mirbazar — Barcha chegirmalar bir joyda',
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
            <h2 class="section-title">Haftalik reyting</h2>
            <p class="text-gray-500 text-sm mt-2">Eng ko'p chegirma bergan do'konlar</p>
          </div>
          <div class="badge-live">
            <span class="w-2 h-2 bg-green-400 rounded-full" style="animation: blink 1.5s ease-in-out infinite"></span>
            Yangilanmoqda
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
          <p class="text-gray-500 text-sm">Hali reyting ma'lumotlari yo'q</p>
        </div>
      </div>
    </section>

    <!-- Filters -->
    <section
      id="promotions"
      class="py-6 sticky top-[56px] z-40 border-b border-white/[0.06] transition-all duration-300"
      style="background: rgba(10, 10, 15, 0.92); backdrop-filter: blur(20px) saturate(180%)"
    >
      <div class="max-w-7xl mx-auto px-5 flex flex-col md:flex-row gap-4 items-start md:items-center">
        <CategoryFilter v-model="selectedCategory" />
        <SearchBar v-model="searchQuery" />
      </div>
    </section>

    <!-- Promotions Grid -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-5">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-10">
          <div class="flex items-center gap-4">
            <h2 class="section-title">Joriy aksiyalar</h2>
            <span class="text-gray-500 text-sm">{{ totalPromotions }} ta</span>
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
          <p class="text-lg text-gray-300 mb-2 font-medium">Aksiyalar topilmadi</p>
          <p class="text-sm text-gray-500">Boshqa kategoriyani tanlang yoki qidiruv so'zini o'zgartiring</p>
        </div>
      </div>
    </section>

    <!-- Stores Section -->
    <section id="stores" class="py-16 relative">
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-cyan-500/[0.02] to-transparent pointer-events-none"></div>
      <div class="max-w-7xl mx-auto px-5 relative">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-10">
          <div>
            <h2 class="section-title">Do'konlar</h2>
            <p class="text-gray-500 text-sm mt-2">Barcha do'konlar va ularning aksiyalari</p>
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
          <p class="text-gray-500 text-sm">Hali do'konlar ma'lumotlari yo'q</p>
        </div>
      </div>
    </section>

    <TelegramCTA />
  </div>
</template>
