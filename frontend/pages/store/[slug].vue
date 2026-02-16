<script setup lang="ts">
const route = useRoute()
const slug = route.params.slug as string

const { getPromotions } = usePromotion()
const { fetchApi } = useApi()

const promotions = ref<any[]>([])
const total = ref(0)
const storeName = ref(slug)

async function loadData() {
  try {
    const data = await getPromotions({ stores: slug })
    promotions.value = data.promotions
    total.value = data.total

    if (data.promotions.length > 0) {
      storeName.value = data.promotions[0].store
    }
  } catch {
    promotions.value = []
  }
}

onMounted(loadData)

useHead({
  title: computed(() => `${storeName.value} aksiyalari — Mirbazar`),
})
</script>

<template>
  <div class="pt-24 pb-16">
    <div class="max-w-7xl mx-auto px-5">
      <div class="mb-10">
        <NuxtLink to="/" class="text-purple-400 hover:text-cyan-400 text-sm no-underline">
          &larr; Bosh sahifa
        </NuxtLink>
        <h1 class="text-4xl font-bold text-white mt-4">
          {{ storeName }}
        </h1>
        <p class="text-gray-400 mt-2">{{ total }} ta aksiya topildi</p>
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
        <p class="text-xl">Bu do'konda aksiyalar topilmadi</p>
      </div>
    </div>
  </div>
</template>
