<script setup lang="ts">
interface Category {
  slug: string
  label: string
  icon: string
}

const categories: Category[] = [
  { slug: 'all', label: 'Hammasi', icon: 'fire' },
  { slug: 'electronics', label: 'Elektronika', icon: 'phone' },
  { slug: 'grocery', label: 'Oziq-ovqat', icon: 'cart' },
  { slug: 'marketplace', label: 'Marketplace', icon: 'store' },
  { slug: 'fashion', label: 'Kiyim-kechak', icon: 'shirt' },
  { slug: 'phones', label: 'Telefonlar', icon: 'smartphone' },
]

const icons: Record<string, string> = {
  fire: 'M17.09 4.86c-.1-.17-.27-.3-.47-.35s-.41-.02-.59.09a4.87 4.87 0 01-2.4.7c-.09-1.3-.56-2.54-1.36-3.56a1.03 1.03 0 00-.73-.4.98.98 0 00-.78.3 7.61 7.61 0 00-1.93 4.16c-.46-.16-.89-.4-1.27-.7a.91.91 0 00-.58-.13c-.2.03-.39.14-.51.3C4.66 7.86 3.5 10.6 3.5 12.5 3.5 17.19 7.31 21 12 21s8.5-3.81 8.5-8.5c0-2.82-1.33-6.19-3.41-7.64z',
  phone: 'M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z',
  cart: 'M1 1h4l2.68 13.39a2 2 0 002 1.61h9.72a2 2 0 002-1.61L23 6H6',
  shirt: 'M20.38 3.46L16 2 12 5 8 2l-4.38 1.46a2 2 0 00-1.34 1.68L1 18a2 2 0 002 2h18a2 2 0 002-2l-1.28-12.86a2 2 0 00-1.34-1.68z',
  store: 'M3 3h18l-2 13H5L3 3zm0 0l-1-1M7 16v5M17 16v5M2 21h20',
  smartphone: 'M12 18h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z',
}

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
  <div class="flex gap-2.5 flex-wrap">
    <button
      v-for="cat in categories"
      :key="cat.slug"
      class="flex items-center gap-2 px-4 py-2.5 rounded-full font-medium text-sm transition-all duration-300 border whitespace-nowrap"
      :class="
        modelValue === cat.slug
          ? 'bg-gradient-to-r from-purple-500 to-cyan-500 border-transparent text-white shadow-[0_0_20px_rgba(124,58,237,0.3)]'
          : 'bg-white/[0.03] border-white/10 text-gray-400 hover:border-purple-500/40 hover:text-white hover:bg-white/[0.06]'
      "
      @click="selectCategory(cat.slug)"
    >
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path :d="icons[cat.icon]"/>
      </svg>
      {{ cat.label }}
    </button>
  </div>
</template>
