<script setup lang="ts">
const head = useLocaleHead({
  addDirAttribute: true,
  addSeoAttributes: true,
})

useHead({
  htmlAttrs: computed(() => head.value.htmlAttrs || {}),
  link: computed(() => (head.value.link || []) as any[]),
  meta: computed(() => (head.value.meta || []) as any[]),
})
</script>

<template>
  <div class="min-h-screen">
    <Header />
    <main>
      <slot />
    </main>
    <Footer />
    <CookieConsent />
  </div>
</template>
