<script setup lang="ts">
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

function getPositionClass(pos: number): string {
  if (pos === 0) return 'bg-gradient-to-br from-yellow-400 to-yellow-600 text-black'
  if (pos === 1) return 'bg-gradient-to-br from-gray-300 to-gray-500 text-black'
  if (pos === 2) return 'bg-gradient-to-br from-amber-600 to-amber-800 text-white'
  return 'bg-gradient-to-br from-purple-500 to-cyan-500 text-white'
}
</script>

<template>
  <div
    class="glass-card glow-hover p-5 flex items-center gap-5 group cursor-pointer"
  >
    <div
      class="w-14 h-14 rounded-xl flex items-center justify-center text-xl font-extrabold shrink-0"
      :class="getPositionClass(position)"
    >
      {{ position + 1 }}
    </div>

    <div class="flex-1 min-w-0">
      <h3 class="text-white font-bold text-lg mb-1 truncate group-hover:text-purple-400 transition-colors">
        {{ store.name }}
      </h3>
      <div class="flex gap-4 text-gray-400 text-sm">
        <span>{{ store.count }} aksiya</span>
        <span>{{ store.avg_discount.toFixed(0) }}% o'rtacha</span>
      </div>
    </div>

    <div class="text-2xl font-extrabold text-green-400 shrink-0">
      {{ store.max_discount }}%
    </div>
  </div>
</template>
