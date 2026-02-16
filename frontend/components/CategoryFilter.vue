<script setup lang="ts">
interface Category {
  slug: string
  label: string
  icon: string
}

const categories: Category[] = [
  { slug: 'all', label: 'Hammasi', icon: '🔥' },
  { slug: 'electronics', label: 'Elektronika', icon: '📱' },
  { slug: 'appliances', label: 'Maishiy texnika', icon: '🏠' },
  { slug: 'grocery', label: 'Oziq-ovqat', icon: '🛒' },
  { slug: 'fashion', label: 'Kiyim-kechak', icon: '👕' },
]

const props = defineProps<{
  modelValue: string
}>()

const emit = defineEmits<{
  'update:modelValue': [value: string]
}>()

function selectCategory(slug: string) {
  emit('update:modelValue', slug)
}
</script>

<template>
  <div class="flex gap-3 flex-wrap">
    <button
      v-for="cat in categories"
      :key="cat.slug"
      class="px-5 py-2.5 rounded-full font-medium text-sm transition-all duration-300 border"
      :class="
        modelValue === cat.slug
          ? 'bg-gradient-to-r from-purple-500 to-cyan-500 border-transparent text-white'
          : 'bg-white/5 border-white/10 text-gray-400 hover:border-purple-500/50 hover:text-white'
      "
      @click="selectCategory(cat.slug)"
    >
      {{ cat.icon }} {{ cat.label }}
    </button>
  </div>
</template>
