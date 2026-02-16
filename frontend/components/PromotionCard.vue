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
  <div
    class="group relative bg-white/5 backdrop-blur-xl rounded-2xl overflow-hidden border border-white/10 transition-all duration-500 hover:border-purple-500/50 hover:scale-[1.02] hover:shadow-[0_0_40px_rgba(124,58,237,0.2)]"
    :class="{ 'opacity-60': promotion.status === 'expired' }"
  >
    <div class="relative h-48 overflow-hidden">
      <img
        v-if="promotion.image_url"
        :src="promotion.image_url"
        :alt="promotion.title"
        class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
        loading="lazy"
      />
      <div
        v-else
        class="w-full h-full bg-gradient-to-br from-purple-500/20 to-cyan-500/20 flex items-center justify-center text-4xl"
      >
        🛍️
      </div>
      <div
        class="absolute inset-0"
        style="
          background: linear-gradient(
            to bottom,
            transparent 50%,
            rgba(10, 10, 15, 0.9)
          );
        "
      ></div>

      <div
        class="absolute top-4 right-4 z-10 bg-gradient-to-r from-red-500 to-orange-500 px-4 py-2 rounded-full font-bold text-white text-lg shadow-[0_0_20px_rgba(239,68,68,0.5)]"
        style="animation: pulse 2s infinite"
      >
        {{ promotion.discount_text || `-${promotion.discount_percent}%` }}
      </div>

      <div
        class="absolute bottom-3 left-3 flex items-center gap-2 bg-black/70 backdrop-blur-sm px-3 py-1.5 rounded-full text-sm text-gray-300"
      >
        {{ promotion.store }}
      </div>
    </div>

    <div class="p-5 space-y-3">
      <h3
        class="text-white font-semibold text-lg line-clamp-2 group-hover:text-transparent group-hover:bg-clip-text group-hover:bg-gradient-to-r group-hover:from-purple-400 group-hover:to-cyan-400"
      >
        {{ promotion.title }}
      </h3>

      <div class="flex items-center gap-2">
        <span v-if="promotion.old_price" class="text-gray-500 line-through text-sm">
          {{ formatPrice(promotion.old_price) }}
        </span>
        <span class="text-gray-500" v-if="promotion.old_price">&rarr;</span>
        <span v-if="promotion.new_price" class="text-green-400 font-bold text-xl">
          {{ formatPrice(promotion.new_price) }}
          <span class="text-sm text-gray-400 font-normal">so'm</span>
        </span>
      </div>

      <div class="flex items-center justify-between pt-3 border-t border-white/10">
        <div
          v-if="promotion.deadline_text"
          class="flex items-center gap-2 text-sm"
          :class="
            promotion.days_left !== undefined && promotion.days_left <= 2
              ? 'text-red-400'
              : 'text-orange-400'
          "
        >
          <CountdownTimer
            v-if="promotion.days_left !== undefined"
            :days-left="promotion.days_left"
          />
          <span v-else>{{ promotion.deadline_text }}</span>
        </div>
        <a
          v-if="promotion.source_url"
          :href="promotion.source_url"
          target="_blank"
          class="text-purple-400 hover:text-cyan-400 font-semibold text-sm transition-colors no-underline"
        >
          Xarid &rarr;
        </a>
      </div>
    </div>

    <div
      class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"
      style="
        background: radial-gradient(
          circle at 50% 50%,
          rgba(124, 58, 237, 0.1),
          transparent 70%
        );
      "
    ></div>
  </div>
</template>
