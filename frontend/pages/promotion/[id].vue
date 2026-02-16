<script setup lang="ts">
const route = useRoute()
const id = Number(route.params.id)

const { getPromotion, formatPrice } = usePromotion()

const promotion = ref<any>(null)
const error = ref(false)
const loading = ref(true)

async function loadData() {
  loading.value = true
  try {
    promotion.value = await getPromotion(id)
  } catch {
    error.value = true
  } finally {
    loading.value = false
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
      <NuxtLink
        to="/"
        class="inline-flex items-center gap-2 text-gray-400 hover:text-purple-400 text-sm transition-colors mb-8 group"
      >
        <svg class="transition-transform group-hover:-translate-x-1" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M15 18l-6-6 6-6"/>
        </svg>
        Bosh sahifa
      </NuxtLink>

      <!-- Error state -->
      <div v-if="error" class="glass-card p-16 text-center">
        <svg class="mx-auto mb-4 text-gray-600" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/>
        </svg>
        <p class="text-xl text-gray-400 mb-2">Aksiya topilmadi</p>
        <NuxtLink to="/" class="text-purple-400 hover:text-cyan-400 text-sm transition-colors">
          Bosh sahifaga qaytish
        </NuxtLink>
      </div>

      <!-- Loading skeleton -->
      <div v-else-if="loading" class="glass-card p-8 space-y-6">
        <div class="flex items-center gap-3">
          <div class="h-8 w-20 skeleton rounded-full"></div>
          <div class="h-4 w-24 skeleton rounded"></div>
        </div>
        <div class="h-8 w-3/4 skeleton rounded"></div>
        <div class="h-5 w-full skeleton rounded"></div>
        <div class="flex gap-4">
          <div class="h-8 w-32 skeleton rounded"></div>
          <div class="h-8 w-40 skeleton rounded"></div>
        </div>
        <div class="h-14 w-48 skeleton rounded-full"></div>
      </div>

      <!-- Promotion detail -->
      <div v-else-if="promotion" class="animate-fade-in-up">
        <div class="glass-card overflow-hidden">
          <!-- Image -->
          <div v-if="promotion.image_url" class="relative h-64 md:h-80 overflow-hidden">
            <img
              :src="promotion.image_url"
              :alt="promotion.title"
              class="w-full h-full object-cover"
            />
            <div class="absolute inset-0" style="background: linear-gradient(to bottom, transparent 50%, rgba(10,10,15,0.95))"></div>
          </div>

          <div class="p-8 md:p-10">
            <div class="flex flex-wrap items-center gap-3 mb-6">
              <span class="badge-discount">
                {{ promotion.discount_text || `-${promotion.discount_percent}%` }}
              </span>
              <NuxtLink
                v-if="promotion.store_slug"
                :to="`/store/${promotion.store_slug}`"
                class="flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 text-gray-400 text-sm hover:border-purple-500/40 transition-colors"
              >
                <div class="w-5 h-5 rounded bg-gradient-to-br from-purple-500/50 to-cyan-500/50 flex items-center justify-center text-[10px] font-bold text-white">
                  {{ promotion.store?.charAt(0) }}
                </div>
                {{ promotion.store }}
              </NuxtLink>
              <span
                v-if="promotion.deadline_text"
                class="flex items-center gap-1.5 text-sm"
                :class="promotion.days_left <= 2 ? 'text-red-400' : 'text-orange-400'"
              >
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>
                </svg>
                {{ promotion.deadline_text }}
              </span>
            </div>

            <h1 class="text-3xl md:text-4xl font-bold text-white mb-6 leading-tight">
              {{ promotion.title }}
            </h1>

            <p v-if="promotion.description" class="text-gray-400 text-lg mb-8 leading-relaxed">
              {{ promotion.description }}
            </p>

            <!-- Prices -->
            <div class="flex items-baseline gap-4 mb-8 p-6 rounded-2xl bg-white/[0.03] border border-white/[0.06]">
              <div v-if="promotion.old_price" class="text-center">
                <span class="block text-gray-500 text-xs mb-1">Oldingi narx</span>
                <span class="text-gray-500 line-through text-xl">
                  {{ formatPrice(promotion.old_price) }} so'm
                </span>
              </div>
              <svg v-if="promotion.old_price && promotion.new_price" class="text-gray-600 shrink-0" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M5 12h14M12 5l7 7-7 7"/>
              </svg>
              <div v-if="promotion.new_price" class="text-center">
                <span class="block text-green-400 text-xs mb-1">Yangi narx</span>
                <span class="text-green-400 font-bold text-3xl">
                  {{ formatPrice(promotion.new_price) }} so'm
                </span>
              </div>
            </div>

            <a
              v-if="promotion.source_url"
              :href="promotion.source_url"
              target="_blank"
              class="btn-primary text-lg"
            >
              Xarid qilish
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
