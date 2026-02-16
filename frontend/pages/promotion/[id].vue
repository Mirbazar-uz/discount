<script setup lang="ts">
const route = useRoute()
const id = Number(route.params.id)

const { getPromotion, formatPrice } = usePromotion()

const promotion = ref<any>(null)
const error = ref(false)

async function loadData() {
  try {
    promotion.value = await getPromotion(id)
  } catch {
    error.value = true
  }
}

onMounted(loadData)

useHead({
  title: computed(() =>
    promotion.value ? `${promotion.value.title} — Mirbazar` : 'Aksiya — Mirbazar'
  ),
})
</script>

<template>
  <div class="pt-24 pb-16">
    <div class="max-w-4xl mx-auto px-5">
      <NuxtLink to="/" class="text-purple-400 hover:text-cyan-400 text-sm no-underline">
        &larr; Bosh sahifa
      </NuxtLink>

      <div v-if="error" class="text-center py-20 text-gray-500">
        <p class="text-xl">Aksiya topilmadi</p>
      </div>

      <div v-else-if="promotion" class="mt-8">
        <div class="glass-card p-8">
          <div class="flex items-center gap-3 mb-6">
            <span
              class="px-4 py-1.5 rounded-full bg-gradient-to-r from-red-500 to-orange-500 font-bold text-white"
            >
              {{ promotion.discount_text || `-${promotion.discount_percent}%` }}
            </span>
            <span class="text-gray-400 text-sm">
              {{ promotion.store }}
            </span>
          </div>

          <h1 class="text-3xl md:text-4xl font-bold text-white mb-6">
            {{ promotion.title }}
          </h1>

          <p v-if="promotion.description" class="text-gray-400 text-lg mb-8">
            {{ promotion.description }}
          </p>

          <div class="flex items-center gap-4 mb-8">
            <span
              v-if="promotion.old_price"
              class="text-gray-500 line-through text-xl"
            >
              {{ formatPrice(promotion.old_price) }} so'm
            </span>
            <span v-if="promotion.new_price" class="text-green-400 font-bold text-3xl">
              {{ formatPrice(promotion.new_price) }} so'm
            </span>
          </div>

          <div
            v-if="promotion.deadline_text"
            class="flex items-center gap-2 text-orange-400 mb-8"
          >
            {{ promotion.deadline_text }}
          </div>

          <a
            v-if="promotion.source_url"
            :href="promotion.source_url"
            target="_blank"
            class="inline-flex items-center gap-2 px-8 py-4 rounded-full bg-gradient-to-r from-purple-500 to-cyan-500 text-white font-semibold text-lg hover:shadow-[0_0_30px_rgba(124,58,237,0.5)] transition-all no-underline"
          >
            Xarid qilish &rarr;
          </a>
        </div>
      </div>

      <div v-else class="text-center py-20">
        <div class="w-10 h-10 border-2 border-purple-500 border-t-transparent rounded-full animate-spin mx-auto"></div>
      </div>
    </div>
  </div>
</template>
