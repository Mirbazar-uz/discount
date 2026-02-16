<script setup lang="ts">
interface Promotion {
  id: number
  title: string
  old_price?: number
  new_price?: number
  discount_text?: string
  discount_percent?: number
  store: string
  store_slug: string
  image_url?: string
  deadline_text?: string
  source_url?: string
  status: string
  days_left?: number
}

defineProps<{
  promotion: Promotion
}>()

function formatPrice(price: number): string {
  return new Intl.NumberFormat('uz-UZ').format(price)
}
</script>

<template>
  <NuxtLink
    :to="`/promotion/${promotion.id}`"
    class="group relative flex flex-col overflow-hidden rounded-2xl border border-white/10 transition-all duration-500 hover:border-purple-500/40 hover:shadow-[0_0_40px_rgba(124,58,237,0.15)] hover:-translate-y-1"
    :class="[
      promotion.status === 'expired'
        ? 'opacity-50 grayscale pointer-events-none'
        : ''
    ]"
    style="background: linear-gradient(135deg, rgba(255,255,255,0.04) 0%, rgba(255,255,255,0.01) 100%)"
  >
    <!-- Image -->
    <div class="relative h-48 overflow-hidden">
      <img
        v-if="promotion.image_url"
        :src="promotion.image_url"
        :alt="promotion.title"
        class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
        loading="lazy"
      />
      <div
        v-else
        class="w-full h-full flex items-center justify-center"
        style="background: linear-gradient(135deg, rgba(124,58,237,0.15) 0%, rgba(0,212,255,0.1) 100%)"
      >
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1.5">
          <path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>
        </svg>
      </div>

      <!-- Gradient overlay -->
      <div
        class="absolute inset-0"
        style="background: linear-gradient(to bottom, transparent 40%, rgba(10, 10, 15, 0.95))"
      ></div>

      <!-- Discount badge -->
      <div class="absolute top-3 right-3 z-10 badge-discount text-base">
        {{ promotion.discount_text || `-${promotion.discount_percent}%` }}
      </div>

      <!-- Store badge -->
      <div
        class="absolute bottom-3 left-3 z-10 flex items-center gap-2 bg-black/60 backdrop-blur-md px-3 py-1.5 rounded-full text-xs text-gray-300 border border-white/10"
      >
        <div class="w-5 h-5 rounded bg-gradient-to-br from-purple-500/50 to-cyan-500/50 flex items-center justify-center text-[10px] font-bold">
          {{ promotion.store.charAt(0) }}
        </div>
        {{ promotion.store }}
      </div>
    </div>

    <!-- Content -->
    <div class="flex-1 p-5 space-y-3">
      <h3
        class="text-white font-semibold text-base leading-snug line-clamp-2 transition-all duration-300 group-hover:text-transparent group-hover:bg-clip-text group-hover:bg-gradient-to-r group-hover:from-purple-400 group-hover:to-cyan-400"
      >
        {{ promotion.title }}
      </h3>

      <!-- Prices -->
      <div class="flex items-baseline gap-2">
        <span v-if="promotion.old_price" class="text-gray-500 line-through text-sm">
          {{ formatPrice(promotion.old_price) }}
        </span>
        <span v-if="promotion.new_price" class="text-green-400 font-bold text-xl">
          {{ formatPrice(promotion.new_price) }}
          <span class="text-xs text-gray-400 font-normal ml-1">so'm</span>
        </span>
      </div>

      <!-- Footer -->
      <div class="flex items-center justify-between pt-3 border-t border-white/[0.06]">
        <div
          v-if="promotion.deadline_text"
          class="flex items-center gap-1.5 text-xs"
          :class="
            promotion.days_left !== undefined && promotion.days_left <= 2
              ? 'text-red-400'
              : 'text-orange-400'
          "
        >
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>
          </svg>
          <CountdownTimer
            v-if="promotion.days_left !== undefined"
            :days-left="promotion.days_left"
          />
          <span v-else>{{ promotion.deadline_text }}</span>
        </div>
        <span class="text-purple-400 group-hover:text-cyan-400 font-semibold text-xs transition-colors ml-auto">
          Batafsil &rarr;
        </span>
      </div>
    </div>

    <!-- Hover glow overlay -->
    <div
      class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none rounded-2xl"
      style="background: radial-gradient(circle at 50% 50%, rgba(124, 58, 237, 0.08), transparent 70%)"
    ></div>
  </NuxtLink>
</template>
