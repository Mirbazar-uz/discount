<script setup lang="ts">
const scrolled = ref(false)

onMounted(() => {
  window.addEventListener('scroll', () => {
    scrolled.value = window.scrollY > 50
  })
})
</script>

<template>
  <nav
    class="fixed top-0 left-0 right-0 z-50 transition-all duration-300 border-b border-white/10"
    :class="[
      scrolled
        ? 'py-2 bg-[#0a0a0f]/95 backdrop-blur-xl'
        : 'py-4 bg-[#0a0a0f]/80 backdrop-blur-xl',
    ]"
  >
    <div class="max-w-7xl mx-auto px-5 flex items-center justify-between">
      <NuxtLink to="/" class="flex items-center gap-3 no-underline">
        <div
          class="w-12 h-12 bg-gradient-to-br from-purple-500 to-cyan-500 rounded-xl flex items-center justify-center text-2xl shadow-[0_0_30px_rgba(124,58,237,0.3)]"
        >
          🛒
        </div>
        <span
          class="text-2xl font-extrabold bg-gradient-to-r from-purple-500 to-cyan-500 bg-clip-text text-transparent"
        >
          MIRBAZAR
        </span>
      </NuxtLink>

      <ul class="hidden md:flex gap-8 list-none">
        <li>
          <a
            href="#promotions"
            class="text-gray-400 hover:text-white transition-colors font-medium"
          >
            Aksiyalar
          </a>
        </li>
        <li>
          <a
            href="#rating"
            class="text-gray-400 hover:text-white transition-colors font-medium"
          >
            Reyting
          </a>
        </li>
        <li>
          <a
            href="#stores"
            class="text-gray-400 hover:text-white transition-colors font-medium"
          >
            Do'konlar
          </a>
        </li>
      </ul>

      <a
        href="https://t.me/mirbazar_uz"
        target="_blank"
        class="flex items-center gap-2 px-5 py-2.5 rounded-full bg-gradient-to-r from-[#0088cc] to-[#00aced] text-white font-semibold text-sm hover:scale-105 transition-transform no-underline"
      >
        <svg
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="currentColor"
        >
          <path
            d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"
          />
        </svg>
        Obuna bo'ling
      </a>
    </div>
  </nav>
</template>
