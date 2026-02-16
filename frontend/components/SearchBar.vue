<script setup lang="ts">
const props = defineProps<{
  modelValue: string
}>()

const emit = defineEmits<{
  'update:modelValue': [value: string]
}>()

function onInput(event: Event) {
  const target = event.target as HTMLInputElement
  emit('update:modelValue', target.value)
}
</script>

<template>
  <div class="relative flex-1 min-w-[250px]">
    <svg
      class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-500"
      width="20"
      height="20"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
    >
      <circle cx="11" cy="11" r="8" />
      <path d="m21 21-4.35-4.35" />
    </svg>
    <input
      type="text"
      :value="modelValue"
      placeholder="Mahsulot qidirish..."
      class="w-full py-3 pl-12 pr-5 rounded-full bg-white/5 border border-white/10 text-white placeholder-gray-500 outline-none transition-all duration-300 focus:border-purple-500 focus:shadow-[0_0_30px_rgba(124,58,237,0.3)]"
      @input="onInput"
    />
  </div>
</template>
