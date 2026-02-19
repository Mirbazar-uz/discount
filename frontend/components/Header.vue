<script setup lang="ts">
const { t } = useI18n()
const route = useRoute()
const router = useRouter()
const localePath = useLocalePath()
const scrolled = ref(false)
const mobileMenuOpen = ref(false)

const navItems = computed(() => [
  { label: t('nav.promotions'), to: '/#promotions', icon: 'tag' },
  { label: t('nav.rating'), to: '/#rating', icon: 'trophy' },
  { label: t('nav.stores'), to: '/#stores', icon: 'store' },
])

function handleScroll() {
  scrolled.value = window.scrollY > 50
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  document.body.style.overflow = ''
})

watch(() => route.fullPath, () => {
  mobileMenuOpen.value = false
})

watch(mobileMenuOpen, (open) => {
  document.body.style.overflow = open ? 'hidden' : ''
})

function closeMobile() {
  mobileMenuOpen.value = false
}

function handleNavClick(to: string) {
  closeMobile()
  const [path, hash] = to.split('#')
  const homePath = localePath('/')
  if (route.path === homePath || route.path === path || (path === '/' && route.path === homePath)) {
    const el = hash ? document.getElementById(hash) : null
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' })
    }
  } else {
    router.push(localePath(to))
  }
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
      <NuxtLink :to="localePath('/')" class="flex items-center gap-3 group">
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
        <li v-for="item in navItems" :key="item.to">
          <a
            :href="item.to"
            class="text-gray-400 hover:text-white transition-all duration-300 font-medium relative after:content-[''] after:absolute after:-bottom-1 after:left-0 after:w-0 after:h-0.5 after:bg-gradient-to-r after:from-purple-500 after:to-cyan-500 after:transition-all after:duration-300 hover:after:w-full"
            @click.prevent="handleNavClick(item.to)"
          >
            {{ item.label }}
          </a>
        </li>
      </ul>

      <div class="flex items-center gap-3">
        <LanguageSwitcher class="hidden sm:flex" />

        <a
          href="https://t.me/mirbazar_uz"
          target="_blank"
          class="hidden sm:flex items-center gap-2 px-5 py-2.5 rounded-full bg-gradient-to-r from-[#0088cc] to-[#00aced] text-white font-semibold text-sm hover:scale-105 hover:shadow-[0_0_20px_rgba(0,136,204,0.4)] transition-all duration-300"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
          </svg>
          {{ t('nav.subscribe') }}
        </a>

        <!-- Mobile menu button -->
        <button
          class="md:hidden w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 border border-white/10 text-gray-400 hover:text-white hover:bg-white/10 transition-all duration-200"
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
  </nav>

  <!-- Mobile menu overlay + slide panel -->
  <Teleport to="body">
    <Transition
      enter-active-class="transition-opacity duration-300 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-opacity duration-200 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="mobileMenuOpen"
        class="fixed inset-0 z-[60] bg-black/60 backdrop-blur-sm md:hidden"
        @click="closeMobile"
      />
    </Transition>

    <Transition
      enter-active-class="transition-transform duration-300 ease-out"
      enter-from-class="translate-x-full"
      enter-to-class="translate-x-0"
      leave-active-class="transition-transform duration-200 ease-in"
      leave-from-class="translate-x-0"
      leave-to-class="translate-x-full"
    >
      <div
        v-if="mobileMenuOpen"
        class="fixed top-0 right-0 bottom-0 w-72 z-[70] bg-[#0f0f1a]/98 backdrop-blur-2xl border-l border-white/10 flex flex-col md:hidden"
      >
        <!-- Header -->
        <div class="flex items-center justify-between p-5 border-b border-white/[0.06]">
          <span class="text-sm font-semibold text-gray-400 uppercase tracking-wider">{{ t('nav.menu') }}</span>
          <button
            class="w-9 h-9 flex items-center justify-center rounded-lg bg-white/5 border border-white/10 text-gray-400 hover:text-white hover:bg-white/10 transition-all"
            @click="closeMobile"
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 6L6 18M6 6l12 12"/>
            </svg>
          </button>
        </div>

        <!-- Nav items -->
        <nav class="flex-1 p-4 space-y-1">
          <a
            v-for="item in navItems"
            :key="item.to"
            :href="item.to"
            class="flex items-center gap-3 px-4 py-3.5 rounded-xl text-gray-300 hover:text-white hover:bg-white/[0.06] transition-all duration-200 group"
            @click.prevent="handleNavClick(item.to)"
          >
            <div class="w-9 h-9 rounded-lg bg-white/[0.04] border border-white/[0.06] flex items-center justify-center group-hover:bg-purple-500/10 group-hover:border-purple-500/20 transition-all">
              <svg v-if="item.icon === 'tag'" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-gray-500 group-hover:text-purple-400 transition-colors">
                <path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>
              </svg>
              <svg v-else-if="item.icon === 'trophy'" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-gray-500 group-hover:text-purple-400 transition-colors">
                <path d="M6 9H4.5a2.5 2.5 0 010-5H6M18 9h1.5a2.5 2.5 0 000-5H18M4 22h16M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20 7 22M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20 17 22M18 2H6v7a6 6 0 1012 0V2z"/>
              </svg>
              <svg v-else-if="item.icon === 'store'" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-gray-500 group-hover:text-purple-400 transition-colors">
                <path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>
              </svg>
            </div>
            <span class="font-medium text-[15px]">{{ item.label }}</span>
          </a>

          <!-- Language switcher in mobile -->
          <div class="px-4 py-3.5">
            <LanguageSwitcher />
          </div>
        </nav>

        <!-- Telegram CTA -->
        <div class="p-4 border-t border-white/[0.06]">
          <a
            href="https://t.me/mirbazar_uz"
            target="_blank"
            class="flex items-center justify-center gap-2 w-full px-5 py-3 rounded-xl bg-gradient-to-r from-[#0088cc] to-[#00aced] text-white font-semibold text-sm hover:shadow-[0_0_20px_rgba(0,136,204,0.3)] transition-all duration-300"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
            </svg>
            {{ t('nav.telegram_channel') }}
          </a>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>
