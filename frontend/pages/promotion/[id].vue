<script setup lang="ts">
const route = useRoute()
const id = Number(route.params.id)

const { getPromotion, formatPrice } = usePromotion()

const { data: promotion, error, status } = await useAsyncData(
  `promotion-${id}`,
  () => getPromotion(id),
)

const activeImage = ref(0)
const lightboxOpen = ref(false)

const allImages = computed<string[]>(() => {
  if (!promotion.value) return []
  if (promotion.value.image_urls?.length) return promotion.value.image_urls
  if (promotion.value.image_url) return [promotion.value.image_url]
  return []
})

const hasPrices = computed(() => {
  if (!promotion.value) return false
  return promotion.value.old_price || promotion.value.new_price
})

const pageTitle = computed(() =>
  promotion.value ? `${promotion.value.title} — Mirbazar` : 'Aksiya — Mirbazar'
)

const pageDescription = computed(() => {
  if (!promotion.value) return "O'zbekistondagi eng yaxshi aksiyalar va chegirmalar"
  const parts = [promotion.value.title]
  if (promotion.value.store) parts.push(`${promotion.value.store} do'konida`)
  if (promotion.value.discount_text) parts.push(`${promotion.value.discount_text} chegirma`)
  else if (promotion.value.discount_percent) parts.push(`${promotion.value.discount_percent}% chegirma`)
  return parts.join(' — ')
})

const pageImage = computed(() => {
  if (allImages.value.length) return allImages.value[0]
  return 'https://mirbazar.uz/og-image.png'
})

const pageUrl = computed(() => `https://mirbazar.uz/promotion/${id}`)

useSeoMeta({
  title: pageTitle,
  ogTitle: pageTitle,
  description: pageDescription,
  ogDescription: pageDescription,
  ogImage: pageImage,
  ogUrl: pageUrl,
  ogType: 'product',
  twitterCard: 'summary_large_image',
  twitterTitle: pageTitle,
  twitterDescription: pageDescription,
  twitterImage: pageImage,
})

useHead({
  link: [{ rel: 'canonical', href: pageUrl }],
  script: computed(() => {
    if (!promotion.value) return []
    const schema: Record<string, any> = {
      '@context': 'https://schema.org',
      '@type': 'Product',
      name: promotion.value.title,
      image: pageImage.value,
      brand: { '@type': 'Brand', name: promotion.value.store || 'Mirbazar' },
    }
    if (promotion.value.new_price) {
      schema.offers = {
        '@type': 'Offer',
        price: promotion.value.new_price,
        priceCurrency: 'UZS',
        availability: 'https://schema.org/InStock',
        url: pageUrl.value,
      }
    }
    return [{ type: 'application/ld+json', innerHTML: JSON.stringify(schema) }]
  }),
})

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

onUnmounted(() => {
  document.body.style.overflow = ''
})
</script>

<template>
  <div class="pt-24 pb-16">
    <div class="max-w-6xl mx-auto px-5">
      <!-- Breadcrumb -->
      <div class="flex items-center gap-2 text-sm mb-8">
        <NuxtLink
          to="/"
          class="text-gray-500 hover:text-purple-400 transition-colors"
        >
          Bosh sahifa
        </NuxtLink>
        <svg class="text-gray-600" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M9 18l6-6-6-6"/>
        </svg>
        <NuxtLink
          to="/#promotions"
          class="text-gray-500 hover:text-purple-400 transition-colors"
        >
          Aksiyalar
        </NuxtLink>
        <svg class="text-gray-600" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M9 18l6-6-6-6"/>
        </svg>
        <span class="text-gray-400 truncate max-w-[200px]">
          {{ promotion?.title || '...' }}
        </span>
      </div>

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
      <div v-else-if="status === 'pending'" class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div class="space-y-3">
          <div class="aspect-square skeleton rounded-2xl"></div>
          <div class="flex gap-3">
            <div v-for="i in 3" :key="i" class="w-20 h-20 skeleton rounded-xl"></div>
          </div>
        </div>
        <div class="space-y-6 py-2">
          <div class="h-6 w-24 skeleton rounded-full"></div>
          <div class="h-10 w-3/4 skeleton rounded"></div>
          <div class="h-5 w-full skeleton rounded"></div>
          <div class="h-16 w-48 skeleton rounded-xl"></div>
          <div class="h-14 w-full skeleton rounded-xl"></div>
        </div>
      </div>

      <!-- Promotion detail -->
      <div v-else-if="promotion" class="animate-fade-in-up">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">

          <!-- LEFT: Images -->
          <div class="space-y-3">
            <!-- Main image -->
            <div
              v-if="allImages.length"
              class="relative aspect-square rounded-2xl overflow-hidden border border-white/[0.08] group cursor-zoom-in"
              style="background: linear-gradient(135deg, rgba(124,58,237,0.06) 0%, rgba(0,212,255,0.04) 100%)"
              @click="openLightbox(activeImage)"
            >
              <img
                :src="allImages[activeImage]"
                :alt="promotion.title"
                class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-105"
              />

              <!-- Zoom hint -->
              <div class="absolute bottom-4 right-4 flex items-center gap-2 px-3 py-2 rounded-lg bg-black/50 backdrop-blur-md border border-white/10 text-xs text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/><path d="M11 8v6M8 11h6"/>
                </svg>
                Kattalashtirish
              </div>

              <!-- Image counter badge -->
              <div
                v-if="allImages.length > 1"
                class="absolute top-4 right-4 px-3 py-1.5 rounded-full bg-black/50 backdrop-blur-md text-xs text-white/80 border border-white/10"
              >
                {{ activeImage + 1 }} / {{ allImages.length }}
              </div>

              <!-- Prev/Next for main image -->
              <template v-if="allImages.length > 1">
                <button
                  class="absolute left-3 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-black/40 backdrop-blur-md border border-white/10 flex items-center justify-center text-white/60 hover:text-white hover:bg-black/60 transition-all opacity-0 group-hover:opacity-100"
                  @click.stop="prevImage"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
                </button>
                <button
                  class="absolute right-3 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-black/40 backdrop-blur-md border border-white/10 flex items-center justify-center text-white/60 hover:text-white hover:bg-black/60 transition-all opacity-0 group-hover:opacity-100"
                  @click.stop="nextImage"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
                </button>
              </template>
            </div>

            <!-- No image placeholder -->
            <div
              v-else
              class="aspect-square rounded-2xl overflow-hidden border border-white/[0.08] flex items-center justify-center"
              style="background: linear-gradient(135deg, rgba(124,58,237,0.08) 0%, rgba(0,212,255,0.05) 100%)"
            >
              <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/>
              </svg>
            </div>

            <!-- Thumbnails row -->
            <div
              v-if="allImages.length > 1"
              class="flex gap-3 overflow-x-auto pb-1"
              style="scrollbar-width: thin; scrollbar-color: rgba(255,255,255,0.08) transparent"
            >
              <button
                v-for="(url, i) in allImages"
                :key="i"
                class="shrink-0 w-20 h-20 rounded-xl overflow-hidden border-2 transition-all duration-200 hover:scale-105"
                :class="activeImage === i
                  ? 'border-purple-500 shadow-[0_0_15px_rgba(124,58,237,0.25)] ring-1 ring-purple-500/30'
                  : 'border-white/[0.08] hover:border-white/20 opacity-50 hover:opacity-90'
                "
                @click="activeImage = i"
              >
                <img :src="url" :alt="`Rasm ${i + 1}`" class="w-full h-full object-cover" />
              </button>
            </div>
          </div>

          <!-- RIGHT: Info -->
          <div class="flex flex-col py-1">
            <!-- Store + deadline row -->
            <div class="flex flex-wrap items-center gap-3 mb-5">
              <NuxtLink
                v-if="promotion.store_slug"
                :to="`/store/${promotion.store_slug}`"
                class="flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 text-gray-400 text-sm hover:border-purple-500/40 hover:text-white transition-all"
              >
                <div class="w-5 h-5 rounded bg-gradient-to-br from-purple-500/50 to-cyan-500/50 flex items-center justify-center text-[10px] font-bold text-white">
                  {{ promotion.store?.charAt(0) }}
                </div>
                {{ promotion.store }}
              </NuxtLink>
              <span
                v-if="promotion.deadline_text"
                class="flex items-center gap-1.5 px-3 py-1.5 rounded-full text-sm border"
                :class="promotion.days_left !== undefined && promotion.days_left <= 2
                  ? 'text-red-400 bg-red-500/[0.06] border-red-500/20'
                  : 'text-orange-400 bg-orange-500/[0.06] border-orange-500/20'
                "
              >
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>
                </svg>
                {{ promotion.deadline_text }}
              </span>
            </div>

            <!-- Title -->
            <h1 class="text-2xl md:text-3xl lg:text-4xl font-bold text-white mb-4 leading-tight">
              {{ promotion.title }}
            </h1>

            <!-- Description -->
            <p v-if="promotion.description" class="text-gray-400 text-base leading-relaxed mb-6">
              {{ promotion.description }}
            </p>

            <!-- Discount badge large -->
            <div v-if="promotion.discount_text || promotion.discount_percent" class="mb-6">
              <span class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-red-500/10 to-orange-500/10 border border-red-500/20 text-red-400 font-bold text-lg">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>
                </svg>
                {{ promotion.discount_text || `-${promotion.discount_percent}%` }}
              </span>
            </div>

            <!-- Prices -->
            <div v-if="hasPrices" class="mb-8 p-5 rounded-2xl bg-white/[0.03] border border-white/[0.06]">
              <div class="flex items-end gap-3 flex-wrap">
                <div v-if="promotion.new_price">
                  <span class="block text-gray-500 text-xs mb-1 uppercase tracking-wider">Yangi narx</span>
                  <span class="text-green-400 font-bold text-3xl md:text-4xl leading-none">
                    {{ formatPrice(promotion.new_price) }}
                    <span class="text-base font-normal text-gray-500 ml-1">so'm</span>
                  </span>
                </div>
                <div v-if="promotion.old_price" class="pb-1">
                  <span class="block text-gray-600 text-xs mb-1 uppercase tracking-wider">Oldingi narx</span>
                  <span class="text-gray-500 line-through text-lg">
                    {{ formatPrice(promotion.old_price) }} so'm
                  </span>
                </div>
              </div>
            </div>

            <!-- CTA button -->
            <a
              v-if="promotion.source_url"
              :href="promotion.source_url"
              target="_blank"
              class="inline-flex items-center justify-center gap-3 w-full px-8 py-4 rounded-xl bg-gradient-to-r from-purple-600 to-cyan-600 text-white font-semibold text-lg hover:shadow-[0_0_30px_rgba(124,58,237,0.3)] hover:scale-[1.02] active:scale-[0.98] transition-all duration-300"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
                <path d="M1 1h4l2.68 13.39a2 2 0 002 1.61h9.72a2 2 0 002-1.61L23 6H6"/>
              </svg>
              Xarid qilish
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/>
              </svg>
            </a>

            <!-- Source link -->
            <div v-if="promotion.source_url" class="mt-4 flex items-center justify-center gap-2 text-gray-500 text-sm">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71"/>
                <path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"/>
              </svg>
              Telegram postdan olingan
            </div>
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
        class="fixed inset-0 z-[80] bg-black/95 backdrop-blur-sm flex items-center justify-center"
        @click.self="closeLightbox"
      >
        <!-- Top bar -->
        <div class="absolute top-0 left-0 right-0 flex items-center justify-between p-4 z-10">
          <div
            v-if="allImages.length > 1"
            class="px-4 py-2 rounded-full bg-white/10 backdrop-blur-md text-sm text-white/80"
          >
            {{ activeImage + 1 }} / {{ allImages.length }}
          </div>
          <div v-else></div>
          <button
            class="w-10 h-10 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center text-white hover:bg-white/20 transition-all"
            @click="closeLightbox"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 6L6 18M6 6l12 12"/>
            </svg>
          </button>
        </div>

        <!-- Image -->
        <img
          :src="allImages[activeImage]"
          :alt="promotion?.title"
          class="max-w-[92vw] max-h-[85vh] object-contain select-none"
        />

        <!-- Navigation -->
        <template v-if="allImages.length > 1">
          <button
            class="absolute left-4 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center text-white hover:bg-white/20 transition-all"
            @click="prevImage"
          >
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
          </button>
          <button
            class="absolute right-4 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center text-white hover:bg-white/20 transition-all"
            @click="nextImage"
          >
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
          </button>
        </template>

        <!-- Bottom thumbnails in lightbox -->
        <div
          v-if="allImages.length > 1"
          class="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2 p-2 rounded-xl bg-black/40 backdrop-blur-md border border-white/10"
        >
          <button
            v-for="(url, i) in allImages"
            :key="i"
            class="w-12 h-12 rounded-lg overflow-hidden border-2 transition-all duration-200"
            :class="activeImage === i
              ? 'border-white shadow-[0_0_10px_rgba(255,255,255,0.2)]'
              : 'border-transparent opacity-40 hover:opacity-80'
            "
            @click="activeImage = i"
          >
            <img :src="url" :alt="`Rasm ${i + 1}`" class="w-full h-full object-cover" />
          </button>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>
