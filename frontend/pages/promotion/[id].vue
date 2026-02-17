<script setup lang="ts">
const route = useRoute()
const id = Number(route.params.id)

const { getPromotion, formatPrice } = usePromotion()

const promotion = ref<any>(null)
const error = ref(false)
const loading = ref(true)
const activeImage = ref(0)
const lightboxOpen = ref(false)

const allImages = computed<string[]>(() => {
  if (!promotion.value) return []
  if (promotion.value.image_urls?.length) return promotion.value.image_urls
  if (promotion.value.image_url) return [promotion.value.image_url]
  return []
})

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

function prevImage() {
  activeImage.value = activeImage.value > 0
    ? activeImage.value - 1
    : allImages.value.length - 1
}

function nextImage() {
  activeImage.value = activeImage.value < allImages.value.length - 1
    ? activeImage.value + 1
    : 0
}

function openLightbox(index: number) {
  activeImage.value = index
  lightboxOpen.value = true
  document.body.style.overflow = 'hidden'
}

function closeLightbox() {
  lightboxOpen.value = false
  document.body.style.overflow = ''
}

onMounted(loadData)

onUnmounted(() => {
  document.body.style.overflow = ''
})

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
      <div v-else-if="loading" class="glass-card overflow-hidden">
        <div class="h-64 md:h-80 skeleton"></div>
        <div class="p-8 space-y-6">
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
      </div>

      <!-- Promotion detail -->
      <div v-else-if="promotion" class="animate-fade-in-up">
        <div class="glass-card overflow-hidden">
          <!-- Image Gallery -->
          <div v-if="allImages.length" class="relative">
            <!-- Main image -->
            <div
              class="relative h-72 md:h-96 overflow-hidden cursor-pointer"
              @click="openLightbox(activeImage)"
            >
              <img
                :src="allImages[activeImage]"
                :alt="promotion.title"
                class="w-full h-full object-cover transition-opacity duration-300"
              />
              <div class="absolute inset-0" style="background: linear-gradient(to bottom, transparent 60%, rgba(10,10,15,0.95))"></div>

              <!-- Image counter -->
              <div
                v-if="allImages.length > 1"
                class="absolute top-4 left-4 z-10 px-3 py-1.5 rounded-full bg-black/60 backdrop-blur-md text-xs text-gray-300 border border-white/10"
              >
                {{ activeImage + 1 }} / {{ allImages.length }}
              </div>

              <!-- Prev/Next arrows -->
              <template v-if="allImages.length > 1">
                <button
                  class="absolute left-3 top-1/2 -translate-y-1/2 z-10 w-10 h-10 rounded-full bg-black/50 backdrop-blur-md border border-white/10 flex items-center justify-center text-white/70 hover:text-white hover:bg-black/70 transition-all"
                  @click.stop="prevImage"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M15 18l-6-6 6-6"/>
                  </svg>
                </button>
                <button
                  class="absolute right-3 top-1/2 -translate-y-1/2 z-10 w-10 h-10 rounded-full bg-black/50 backdrop-blur-md border border-white/10 flex items-center justify-center text-white/70 hover:text-white hover:bg-black/70 transition-all"
                  @click.stop="nextImage"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M9 18l6-6-6-6"/>
                  </svg>
                </button>
              </template>
            </div>

            <!-- Thumbnails -->
            <div
              v-if="allImages.length > 1"
              class="flex gap-2 p-4 overflow-x-auto"
              style="scrollbar-width: thin; scrollbar-color: rgba(255,255,255,0.1) transparent"
            >
              <button
                v-for="(url, i) in allImages"
                :key="i"
                class="shrink-0 w-16 h-16 md:w-20 md:h-20 rounded-lg overflow-hidden border-2 transition-all duration-200"
                :class="activeImage === i
                  ? 'border-purple-500 shadow-[0_0_12px_rgba(124,58,237,0.3)]'
                  : 'border-white/10 hover:border-white/30 opacity-60 hover:opacity-100'
                "
                @click="activeImage = i"
              >
                <img :src="url" :alt="`Rasm ${i + 1}`" class="w-full h-full object-cover" />
              </button>
            </div>
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

  <!-- Lightbox -->
  <Teleport to="body">
    <Transition
      enter-active-class="transition-opacity duration-200"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-opacity duration-150"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="lightboxOpen && allImages.length"
        class="fixed inset-0 z-[80] bg-black/95 flex items-center justify-center"
        @click.self="closeLightbox"
      >
        <!-- Close button -->
        <button
          class="absolute top-4 right-4 z-10 w-10 h-10 rounded-full bg-white/10 border border-white/20 flex items-center justify-center text-white hover:bg-white/20 transition-all"
          @click="closeLightbox"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 6L6 18M6 6l12 12"/>
          </svg>
        </button>

        <!-- Counter -->
        <div
          v-if="allImages.length > 1"
          class="absolute top-4 left-4 z-10 px-3 py-1.5 rounded-full bg-white/10 text-sm text-white/80"
        >
          {{ activeImage + 1 }} / {{ allImages.length }}
        </div>

        <!-- Image -->
        <img
          :src="allImages[activeImage]"
          :alt="promotion?.title"
          class="max-w-[90vw] max-h-[85vh] object-contain rounded-lg"
        />

        <!-- Navigation -->
        <template v-if="allImages.length > 1">
          <button
            class="absolute left-4 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/10 border border-white/20 flex items-center justify-center text-white hover:bg-white/20 transition-all"
            @click="prevImage"
          >
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M15 18l-6-6 6-6"/>
            </svg>
          </button>
          <button
            class="absolute right-4 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/10 border border-white/20 flex items-center justify-center text-white hover:bg-white/20 transition-all"
            @click="nextImage"
          >
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 18l6-6-6-6"/>
            </svg>
          </button>
        </template>
      </div>
    </Transition>
  </Teleport>
</template>
