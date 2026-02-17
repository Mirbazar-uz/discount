<template>
  <footer class="pt-16 pb-8 border-t border-white/[0.06]" style="background: linear-gradient(180deg, var(--bg-primary) 0%, #0d0d14 100%)">
    <div class="max-w-7xl mx-auto px-5">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <!-- Brand -->
        <div>
          <NuxtLink to="/" class="flex items-center gap-3 mb-5 group">
            <div
              class="w-10 h-10 bg-gradient-to-br from-purple-500 to-cyan-500 rounded-xl flex items-center justify-center shadow-lg transition-all duration-300 group-hover:shadow-[0_0_20px_rgba(124,58,237,0.3)]"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
                <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
              </svg>
            </div>
            <span class="text-lg font-extrabold bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent">
              MIRBAZAR
            </span>
          </NuxtLink>
          <p class="text-gray-500 text-sm mb-6 max-w-xs leading-relaxed">
            O'zbekistondagi barcha chegirmalar bir joyda. Kunlik yangilanish, eng yaxshi narxlar.
          </p>
          <div class="flex gap-3">
            <a
              href="https://t.me/mirbazar_uz"
              target="_blank"
              class="w-10 h-10 flex items-center justify-center bg-white/[0.03] border border-white/10 rounded-xl text-gray-500 hover:text-white hover:bg-gradient-to-br hover:from-purple-500 hover:to-cyan-500 hover:border-transparent hover:-translate-y-1 transition-all duration-300"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.325.015.094.034.31.019.478z"/>
              </svg>
            </a>
            <a
              href="https://instagram.com/mirbazaruz"
              target="_blank"
              class="w-10 h-10 flex items-center justify-center bg-white/[0.03] border border-white/10 rounded-xl text-gray-500 hover:text-white hover:bg-gradient-to-br hover:from-purple-500 hover:to-pink-500 hover:border-transparent hover:-translate-y-1 transition-all duration-300"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>
            </a>
          </div>
        </div>

        <!-- Do'konlar -->
        <div>
          <h4 class="text-white font-semibold mb-5 text-sm uppercase tracking-wider">Do'konlar</h4>
          <ul class="list-none space-y-3">
            <li><NuxtLink to="/store/texnomart" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Texnomart</NuxtLink></li>
            <li><NuxtLink to="/store/asaxiy" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Asaxiy</NuxtLink></li>
            <li><NuxtLink to="/store/mediapark" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Mediapark</NuxtLink></li>
            <li><NuxtLink to="/store/uzum" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Uzum Market</NuxtLink></li>
            <li><NuxtLink to="/store/sello" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Sello</NuxtLink></li>
            <li><NuxtLink to="/store/korzinka" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Korzinka</NuxtLink></li>
          </ul>
        </div>

        <!-- Kategoriyalar -->
        <div>
          <h4 class="text-white font-semibold mb-5 text-sm uppercase tracking-wider">Kategoriyalar</h4>
          <ul class="list-none space-y-3">
            <li><NuxtLink to="/category/electronics" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Elektronika</NuxtLink></li>
            <li><NuxtLink to="/category/marketplace" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Marketplace</NuxtLink></li>
            <li><NuxtLink to="/category/grocery" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Oziq-ovqat</NuxtLink></li>
            <li><NuxtLink to="/category/fashion" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Kiyim-kechak</NuxtLink></li>
            <li><NuxtLink to="/category/phones" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Telefonlar</NuxtLink></li>
          </ul>
        </div>

        <!-- Ma'lumot -->
        <div>
          <h4 class="text-white font-semibold mb-5 text-sm uppercase tracking-wider">Ma'lumot</h4>
          <ul class="list-none space-y-3">
            <li><NuxtLink to="/about" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Biz haqimizda</NuxtLink></li>
            <li><NuxtLink to="/contact" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Bog'lanish</NuxtLink></li>
            <li><NuxtLink to="/privacy" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Maxfiylik siyosati</NuxtLink></li>
            <li><NuxtLink to="/terms" class="text-gray-500 hover:text-purple-400 transition-colors text-sm">Foydalanish shartlari</NuxtLink></li>
          </ul>
        </div>
      </div>

      <!-- Bottom -->
      <div class="pt-8 border-t border-white/[0.05] flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="text-gray-600 text-xs">&copy; 2026 Mirbazar.uz — Barcha huquqlar himoyalangan</p>
        <div class="flex items-center gap-3 text-gray-600 text-xs">
          <NuxtLink to="/privacy" class="hover:text-gray-400 transition-colors">Maxfiylik</NuxtLink>
          <span>|</span>
          <NuxtLink to="/terms" class="hover:text-gray-400 transition-colors">Shartlar</NuxtLink>
        </div>
      </div>
    </div>
  </footer>
</template>
