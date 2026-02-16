<template>
  <div class="min-h-screen">
    <AdminSidebar />
    <AdminToast />
    <main class="lg:ml-64 min-h-screen">
      <div class="max-w-7xl mx-auto px-5 py-8">
        <slot />
      </div>
    </main>
  </div>
</template>
