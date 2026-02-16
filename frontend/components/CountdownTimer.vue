<script setup lang="ts">
const props = defineProps<{
  daysLeft: number
}>()

const label = computed(() => {
  if (props.daysLeft <= 0) return 'Tugagan'
  if (props.daysLeft === 1) return '1 kun qoldi'
  return `${props.daysLeft} kun qoldi`
})

const isUrgent = computed(() => props.daysLeft <= 2)
</script>

<template>
  <span
    class="inline-flex items-center gap-1"
    :class="isUrgent ? 'text-red-400' : 'text-orange-400'"
  >
    <span v-if="isUrgent" style="animation: blink 1s ease-in-out infinite">
      {{ label }}
    </span>
    <span v-else>{{ label }}</span>
  </span>
</template>
