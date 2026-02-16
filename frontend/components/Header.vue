<script setup lang="ts">
const scrolled = ref(false)
const mobileMenuOpen = ref(false)

onMounted(() => {
  window.addEventListener('scroll', () => {
    scrolled.value = window.scrollY > 50
  })
})

function closeMobile() {
  mobileMenuOpen.value = false
}
</script>

<template>
  <nav
    class="fixed top-0 left-0 right-0 z-50 transition-all duration-500 border-b"
    :class="[
      scrolled
        ? 'py-2 bg-[#0a0a0f]/95 backdrop-blur-2xl border-white/10 shadow-lg shadow-black/20'
        : 'py-4 bg-transparent backdrop-blur-sm border-transparent',
    ]"
  >
    <div class="max-w-7xl mx-auto px-5 flex items-center justify-between">
      <NuxtLink to="/" class="flex items-center gap-3 group">
        <div
          class="w-11 h-11 bg-gradient-to-br from-purple-500 to-cyan-500 rounded-xl flex items-center justify-center text-xl shadow-lg transition-all duration-300 group-hover:shadow-[0_0_25px_rgba(124,58,237,0.4)] group-hover:scale-110"
        >
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
          </svg>
        </div>
        <span
          class="text-xl font-extrabold bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent tracking-tight"
        >
          MIRBAZAR
        </span>
      </NuxtLink>

      <ul class="hidden md:flex gap-8 list-none">
        <li>
          <a
            href="#promotions"
            class="text-gray-400 hover:text-white transition-all duration-300 font-medium relative after:content-[''] after:absolute after:-bottom-1 after:left-0 after:w-0 after:h-0.5 after:bg-gradient-to-r after:from-purple-500 after:to-cyan-500 after:transition-all after:duration-300 hover:after:w-full"
          >
            Aksiyalar
          </a>
        </li>
        <li>
          <a
            href="#rating"
            class="text-gray-400 hover:text-white transition-all duration-300 font-medium relative after:content-[''] after:absolute after:-bottom-1 after:left-0 after:w-0 after:h-0.5 after:bg-gradient-to-r after:from-purple-500 after:to-cyan-500 after:transition-all after:duration-300 hover:after:w-full"
          >
            Reyting
          </a>
        </li>
        <li>
          <a
            href="#stores"
            class="text-gray-400 hover:text-white transition-all duration-300 font-medium relative after:content-[''] after:absolute after:-bottom-1 after:left-0 after:w-0 after:h-0.5 after:bg-gradient-to-r after:from-purple-500 after:to-cyan-500 after:transition-all after:duration-300 hover:after:w-full"
          >
            Do'konlar
          </a>
        </li>
      </ul>

      <div class="flex items-center gap-3">
        <a
          href="https://t.me/mirbazar_uz"
          target="_blank"
          class="hidden sm:flex items-center gap-2 px-5 py-2.5 rounded-full bg-gradient-to-r from-[#0088cc] to-[#00aced] text-white font-semibold text-sm hover:scale-105 hover:shadow-[0_0_20px_rgba(0,136,204,0.4)] transition-all duration-300"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
          </svg>
          Obuna bo'ling
        </a>

        <!-- Mobile menu button -->
        <button
          class="md:hidden w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 border border-white/10 text-gray-400"
          @click="mobileMenuOpen = !mobileMenuOpen"
        >
          <svg v-if="!mobileMenuOpen" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 12h18M3 6h18M3 18h18"/>
          </svg>
          <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 6L6 18M6 6l12 12"/>
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile menu -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-4"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-4"
    >
      <div
        v-if="mobileMenuOpen"
        class="md:hidden absolute top-full left-0 right-0 bg-[#0a0a0f]/98 backdrop-blur-2xl border-b border-white/10 px-5 py-6 space-y-4"
      >
        <a href="#promotions" class="block text-gray-300 hover:text-white font-medium py-2" @click="closeMobile">Aksiyalar</a>
        <a href="#rating" class="block text-gray-300 hover:text-white font-medium py-2" @click="closeMobile">Reyting</a>
        <a href="#stores" class="block text-gray-300 hover:text-white font-medium py-2" @click="closeMobile">Do'konlar</a>
        <a
          href="https://t.me/mirbazar_uz"
          target="_blank"
          class="flex items-center justify-center gap-2 px-5 py-3 rounded-full bg-gradient-to-r from-[#0088cc] to-[#00aced] text-white font-semibold text-sm"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
          </svg>
          Telegram kanal
        </a>
      </div>
    </Transition>
  </nav>
</template>
