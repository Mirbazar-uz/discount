export default defineNuxtConfig({
  devtools: { enabled: false },

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/google-fonts',
    '@vueuse/nuxt',
    'nuxt-icon',
  ],

  css: ['~/assets/css/main.css'],

  googleFonts: {
    families: {
      Inter: [400, 500, 600, 700, 800],
    },
  },

  app: {
    head: {
      title: 'Mirbazar — Barcha chegirmalar bir joyda',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            "O'zbekistondagi eng yaxshi aksiyalar va chegirmalar. Texnomart, Asaxiy, Mediapark va boshqa do'konlarning barcha aksiyalari.",
        },
        {
          property: 'og:title',
          content: 'Mirbazar — Barcha chegirmalar bir joyda',
        },
        { property: 'og:image', content: '/og-image.png' },
        { name: 'theme-color', content: '#0a0a0f' },
      ],
      link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    },
  },

  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE_URL || 'http://localhost:8000',
    },
  },

  ssr: true,

  nitro: {
    preset: 'node-server',
  },

  compatibilityDate: '2025-01-01',
})
