<script setup lang="ts">
const { getPromotions, getWeeklyRating, getStats } = usePromotion()

const selectedCategory = ref('all')
const searchQuery = ref('')
const promotions = ref<any[]>([])
const totalPromotions = ref(0)
const rating = ref<any[]>([])
const stats = ref({ total_promotions: 0, active_promotions: 0, total_stores: 0, max_discount: 0 })

let searchTimeout: ReturnType<typeof setTimeout> | null = null

async function loadPromotions() {
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
  }
}

async function loadRating() {
  try {
    const data = await getWeeklyRating()
    rating.value = data.stores
  } catch {
    rating.value = []
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
    <section id="rating" class="py-20 bg-gradient-to-br from-purple-500/5 to-cyan-500/5">
      <div class="max-w-7xl mx-auto px-5">
        <div class="flex justify-between items-center mb-10">
          <h2 class="text-3xl font-bold text-white">Haftalik reyting</h2>
          <span class="text-gray-400">Eng ko'p chegirma bergan do'konlar</span>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
          <RatingBadge
            v-for="(store, index) in rating"
            :key="store.slug"
            :store="store"
            :position="index"
          />
        </div>
      </div>
    </section>

    <!-- Filters + Promotions -->
    <section
      id="promotions"
      class="py-10 sticky top-[70px] z-40 bg-[#0a0a0f]/90 backdrop-blur-xl border-b border-white/10"
    >
      <div class="max-w-7xl mx-auto px-5 flex flex-col md:flex-row gap-4 items-start md:items-center">
        <CategoryFilter v-model="selectedCategory" />
        <SearchBar v-model="searchQuery" />
      </div>
    </section>

    <section class="py-16">
      <div class="max-w-7xl mx-auto px-5">
        <div class="flex justify-between items-center mb-10">
          <div class="flex items-center gap-4">
            <h2 class="text-3xl font-bold text-white">Joriy aksiyalar</h2>
            <div
              class="flex items-center gap-2 px-4 py-2 bg-green-500/20 border border-green-500 rounded-full text-sm text-green-400"
            >
              <span
                class="w-2 h-2 bg-green-400 rounded-full"
                style="animation: blink 1s ease-in-out infinite"
              ></span>
              Yangilanmoqda
            </div>
          </div>
        </div>

        <div
          v-if="promotions.length"
          class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
        >
          <PromotionCard
            v-for="promo in promotions"
            :key="promo.id"
            :promotion="promo"
          />
        </div>
        <div v-else class="text-center py-20 text-gray-500">
          <p class="text-xl mb-2">Aksiyalar topilmadi</p>
          <p class="text-sm">Boshqa kategoriyani tanlang yoki qidiruv so'zini o'zgartiring</p>
        </div>
      </div>
    </section>

    <TelegramCTA />
  </div>
</template>
