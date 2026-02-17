<script setup lang="ts">
useHead({
  script: [
    {
      type: 'application/ld+json',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@graph': [
          {
            '@type': 'Organization',
            name: 'Mirbazar',
            url: 'https://mirbazar.uz',
            logo: 'https://mirbazar.uz/og-image.png',
            sameAs: [
              'https://t.me/mirbazar_uz',
              'https://instagram.com/mirbazar.uz',
            ],
          },
          {
            '@type': 'WebSite',
            name: 'Mirbazar',
            url: 'https://mirbazar.uz',
            potentialAction: {
              '@type': 'SearchAction',
              target: 'https://mirbazar.uz/?search={search_term_string}',
              'query-input': 'required name=search_term_string',
            },
          },
        ],
      }),
    },
  ],
})
</script>

<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
