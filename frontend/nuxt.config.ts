export default defineNuxtConfig({
  devtools: { enabled: false },

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/google-fonts',
    '@vueuse/nuxt',
    'nuxt-icon',
    '@nuxtjs/i18n',
  ],

  i18n: {
    locales: [
      { code: 'en', language: 'en', file: 'en.json', name: 'English' },
      { code: 'uz', language: 'uz', file: 'uz.json', name: "O'zbek" },
      { code: 'ru', language: 'ru', file: 'ru.json', name: 'Русский' },
    ],
    defaultLocale: 'en',
    strategy: 'prefix_except_default',
    langDir: 'locales',
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: 'i18n_redirected',
      redirectOn: 'root',
      fallbackLocale: 'en',
    },
    baseUrl: 'https://mirbazar.uz',
    bundle: {
      optimizeTranslationDirective: false,
    },
  },

  css: ['~/assets/css/main.css'],

  googleFonts: {
    families: {
      Inter: [400, 500, 600, 700, 800],
    },
  },

  app: {
    head: {
      title: 'Mirbazar — All discounts in one place',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            'The best promotions and discounts in Uzbekistan. All promotions from Texnomart, Asaxiy, Mediapark and other stores.',
        },
        { property: 'og:type', content: 'website' },
        { property: 'og:url', content: 'https://mirbazar.uz' },
        { property: 'og:title', content: 'Mirbazar — All discounts in one place' },
        {
          property: 'og:description',
          content: 'The best promotions and discounts in Uzbekistan. All promotions from Texnomart, Asaxiy, Mediapark and other stores.',
        },
        { property: 'og:image', content: 'https://mirbazar.uz/og-image.png' },
        { property: 'og:site_name', content: 'Mirbazar' },
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:title', content: 'Mirbazar — All discounts in one place' },
        {
          name: 'twitter:description',
          content: 'The best promotions and discounts in Uzbekistan. All promotions from Texnomart, Asaxiy, Mediapark and other stores.',
        },
        { name: 'twitter:image', content: 'https://mirbazar.uz/og-image.png' },
        { name: 'theme-color', content: '#0a0a0f' },
      ],
      link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
      script: [
        { src: 'https://www.googletagmanager.com/gtag/js?id=G-EGNW50GSQZ', async: true },
        { children: "window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-EGNW50GSQZ');" },
        { src: 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9769460570717063', async: true, crossorigin: 'anonymous' },
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
