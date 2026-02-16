<template>
  <div class="rounded-2xl border border-white/10 overflow-hidden" style="background: rgba(255,255,255,0.02)">
    <!-- Image skeleton -->
    <div class="h-48 skeleton"></div>
    <!-- Content skeleton -->
    <div class="p-5 space-y-4">
      <div class="h-4 w-3/4 skeleton rounded"></div>
      <div class="h-4 w-1/2 skeleton rounded"></div>
      <div class="flex items-center gap-3">
        <div class="h-6 w-24 skeleton rounded"></div>
        <div class="h-6 w-32 skeleton rounded"></div>
      </div>
      <div class="pt-3 border-t border-white/[0.05] flex justify-between">
        <div class="h-3 w-20 skeleton rounded"></div>
        <div class="h-3 w-16 skeleton rounded"></div>
      </div>
    </div>
  </div>
</template>
