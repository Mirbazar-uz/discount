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
    class="glass-card glow-hover p-6 flex items-center gap-4 no-underline group"
  >
    <div
      class="w-14 h-14 rounded-xl flex items-center justify-center text-2xl font-bold text-white"
      :style="{ background: store.color || '#7c3aed' }"
    >
      {{ store.name.charAt(0) }}
    </div>
    <div class="flex-1">
      <h3 class="text-white font-semibold text-lg group-hover:text-purple-400 transition-colors">
        {{ store.name }}
      </h3>
      <p class="text-gray-400 text-sm">
        {{ store.promotion_count }} ta aksiya
      </p>
    </div>
    <span class="text-gray-500 group-hover:text-purple-400 transition-colors">
      &rarr;
    </span>
  </NuxtLink>
</template>
