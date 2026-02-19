<script setup lang="ts">
const { t } = useI18n()
const localePath = useLocalePath()

interface RatingStore {
  name: string
  slug: string
  color?: string
  count: number
  max_discount: number
  avg_discount: number
}

defineProps<{
  store: RatingStore
  position: number
}>()

function getPositionStyle(pos: number) {
  if (pos === 0) return { bg: 'bg-gradient-to-br from-yellow-400 to-amber-500', text: 'text-black', shadow: 'shadow-[0_0_20px_rgba(245,158,11,0.3)]', icon: '1' }
  if (pos === 1) return { bg: 'bg-gradient-to-br from-slate-200 to-slate-300', text: 'text-slate-800', shadow: 'shadow-[0_0_15px_rgba(203,213,225,0.3)]', icon: '2' }
  if (pos === 2) return { bg: 'bg-gradient-to-br from-amber-600 to-amber-700', text: 'text-white', shadow: 'shadow-[0_0_15px_rgba(217,119,6,0.2)]', icon: '3' }
  return { bg: 'bg-gradient-to-br from-purple-500/50 to-cyan-500/50', text: 'text-white', shadow: '', icon: String(pos + 1) }
}
</script>

<template>
  <NuxtLink
    :to="localePath(`/store/${store.slug}`)"
    class="glass-card-hover p-5 flex items-center gap-4 group relative overflow-hidden"
    :class="position === 0 ? 'ring-1 ring-yellow-500/30' : ''"
  >
    <!-- Position badge -->
    <div
      class="w-12 h-12 rounded-xl flex items-center justify-center text-lg font-extrabold shrink-0 transition-transform duration-300 group-hover:scale-110"
      :class="[getPositionStyle(position).bg, getPositionStyle(position).text, getPositionStyle(position).shadow]"
    >
      {{ getPositionStyle(position).icon }}
    </div>

    <!-- Store info -->
    <div class="flex-1 min-w-0">
      <h3 class="text-white font-bold text-base mb-0.5 truncate group-hover:text-purple-400 transition-colors">
        {{ store.name }}
      </h3>
      <div class="flex gap-3 text-gray-500 text-xs">
        <span class="flex items-center gap-1">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>
          </svg>
          {{ t('rating.promotions', { count: store.count }) }}
        </span>
        <span>~{{ store.avg_discount.toFixed(0) }}%</span>
      </div>
    </div>

    <!-- Max discount -->
    <div class="text-right shrink-0">
      <span class="text-xl font-extrabold text-green-400">
        {{ store.max_discount }}%
      </span>
      <span class="block text-[10px] text-gray-500">{{ t('rating.max') }}</span>
    </div>

    <!-- Gold glow for 1st place -->
    <div
      v-if="position === 0"
      class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"
      style="background: radial-gradient(circle at 50% 50%, rgba(245, 158, 11, 0.06), transparent 70%)"
    ></div>
  </NuxtLink>
</template>
