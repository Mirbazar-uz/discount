<script setup lang="ts">
const props = defineProps<{
  modelValue: string
}>()

const emit = defineEmits<{
  'update:modelValue': [value: string]
}>()

const focused = ref(false)

function onInput(event: Event) {
  const target = event.target as HTMLInputElement
  emit('update:modelValue', target.value)
}
</script>

<template>
  <div
    class="relative flex-1 min-w-0 sm:min-w-[250px] transition-all duration-300"
    :class="focused ? 'scale-[1.01]' : ''"
  >
    <svg
      class="absolute left-4 top-1/2 -translate-y-1/2 transition-colors duration-300"
      :class="focused ? 'text-purple-400' : 'text-gray-500'"
      width="18"
      height="18"
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
      class="w-full py-3 pl-11 pr-5 rounded-full bg-white/[0.03] border border-white/10 text-white text-sm placeholder-gray-500 outline-none transition-all duration-300 focus:border-purple-500/60 focus:shadow-[0_0_25px_rgba(124,58,237,0.2)] focus:bg-white/[0.05]"
      @input="onInput"
      @focus="focused = true"
      @blur="focused = false"
    />
  </div>
</template>
