<script setup lang="ts">
interface Store {
  id: number
  name: string
  slug: string
  color?: string
  category?: string
  promotion_count: number
}

defineProps<{
  store: Store
}>()
</script>

<template>
  <NuxtLink
    :to="`/store/${store.slug}`"
    class="glass-card-hover p-5 flex items-center gap-4 group"
  >
    <div
      class="w-12 h-12 rounded-xl flex items-center justify-center text-xl font-bold text-white shrink-0 transition-all duration-300 group-hover:scale-110 group-hover:shadow-lg"
      :style="{ background: store.color || 'linear-gradient(135deg, #7c3aed, #00d4ff)' }"
    >
      {{ store.name.charAt(0) }}
    </div>
    <div class="flex-1 min-w-0">
      <h3 class="text-white font-semibold text-base group-hover:text-purple-400 transition-colors truncate">
        {{ store.name }}
      </h3>
      <p class="text-gray-500 text-xs mt-0.5">
        <span v-if="store.promotion_count > 0" class="text-green-400/80">{{ store.promotion_count }}</span>
        <span v-else class="text-gray-600">0</span>
        ta aksiya
      </p>
    </div>
    <div class="flex items-center gap-2 shrink-0">
      <span
        v-if="store.promotion_count > 0"
        class="hidden sm:inline-flex px-2 py-0.5 rounded-md bg-green-500/10 text-green-400 text-xs font-medium border border-green-500/20"
      >
        Aktiv
      </span>
      <svg class="text-gray-600 group-hover:text-purple-400 transition-all duration-300 group-hover:translate-x-1" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M9 18l6-6-6-6"/>
      </svg>
    </div>
  </NuxtLink>
</template>
