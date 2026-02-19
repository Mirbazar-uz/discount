<script setup lang="ts">
const { locale, locales } = useI18n()
const switchLocalePath = useSwitchLocalePath()

const availableLocales = computed(() =>
  locales.value.map((l) => ({
    code: typeof l === 'string' ? l : l.code,
    name: typeof l === 'string' ? l : l.name || l.code,
  }))
)
</script>

<template>
  <div class="flex items-center gap-1">
    <NuxtLink
      v-for="loc in availableLocales"
      :key="loc.code"
      :to="switchLocalePath(loc.code)"
      class="px-2.5 py-1.5 rounded-lg text-xs font-semibold uppercase tracking-wide transition-all duration-200"
      :class="
        locale === loc.code
          ? 'bg-gradient-to-r from-purple-500 to-cyan-500 text-white shadow-[0_0_12px_rgba(124,58,237,0.3)]'
          : 'text-gray-500 hover:text-white hover:bg-white/[0.06]'
      "
    >
      {{ loc.code }}
    </NuxtLink>
  </div>
</template>
