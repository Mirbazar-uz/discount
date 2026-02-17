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
      htmlAttrs: { lang: 'uz' },
      title: 'Mirbazar — Barcha chegirmalar bir joyda',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            "O'zbekistondagi eng yaxshi aksiyalar va chegirmalar. Texnomart, Asaxiy, Mediapark va boshqa do'konlarning barcha aksiyalari.",
        },
        { property: 'og:type', content: 'website' },
        { property: 'og:url', content: 'https://mirbazar.uz' },
        { property: 'og:title', content: 'Mirbazar — Barcha chegirmalar bir joyda' },
        {
          property: 'og:description',
          content: "O'zbekistondagi eng yaxshi aksiyalar va chegirmalar. Texnomart, Asaxiy, Mediapark va boshqa do'konlarning barcha aksiyalari.",
        },
        { property: 'og:image', content: 'https://mirbazar.uz/og-image.png' },
        { property: 'og:locale', content: 'uz_UZ' },
        { property: 'og:site_name', content: 'Mirbazar' },
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:title', content: 'Mirbazar — Barcha chegirmalar bir joyda' },
        {
          name: 'twitter:description',
          content: "O'zbekistondagi eng yaxshi aksiyalar va chegirmalar. Texnomart, Asaxiy, Mediapark va boshqa do'konlarning barcha aksiyalari.",
        },
        { name: 'twitter:image', content: 'https://mirbazar.uz/og-image.png' },
        { name: 'theme-color', content: '#0a0a0f' },
      ],
      link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
      script: [
        { src: 'https://www.googletagmanager.com/gtag/js?id=G-EGNW50GSQZ', async: true },
        { children: "window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-EGNW50GSQZ');" },
      ],
    },
  },

  runtimeConfig: {
    apiBaseServer: process.env.NUXT_API_BASE_SERVER || 'http://localhost:8000',
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000',
    },
  },

  ssr: true,

  nitro: {
    preset: 'node-server',
  },

  compatibilityDate: '2025-01-01',
})
