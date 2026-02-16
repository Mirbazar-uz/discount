<script setup lang="ts">
definePageMeta({ layout: false })

useHead({ title: 'Admin Login — Mirbazar' })

const { login, isAuthenticated } = useAuth()

if (isAuthenticated.value) {
  navigateTo('/admin')
}

const password = ref('')
const loading = ref(false)
const errorMsg = ref('')

async function handleLogin() {
  if (!password.value) return

  loading.value = true
  errorMsg.value = ''

  const success = await login(password.value)

  if (success) {
    navigateTo('/admin')
  } else {
    errorMsg.value = "Noto'g'ri parol"
  }

  loading.value = false
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center p-4">
    <div class="glass-card p-8 w-full max-w-sm">
      <!-- Logo -->
      <div class="text-center mb-8">
        <div class="w-16 h-16 mx-auto rounded-2xl flex items-center justify-center mb-4" style="background: var(--gradient-primary)">
          <span class="text-white font-bold text-2xl">M</span>
        </div>
        <h1 class="text-2xl font-bold text-white">Admin Panel</h1>
        <p class="text-sm text-gray-400 mt-1">Mirbazar.uz</p>
      </div>

      <!-- Form -->
      <form @submit.prevent="handleLogin">
        <div class="mb-6">
          <label class="block text-sm font-medium text-gray-400 mb-2">Parol</label>
          <input
            v-model="password"
            type="password"
            placeholder="Admin parolini kiriting"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500/50 transition-colors"
            :disabled="loading"
          />
        </div>

        <p v-if="errorMsg" class="text-red-400 text-sm mb-4">{{ errorMsg }}</p>

        <button
          type="submit"
          :disabled="loading || !password"
          class="w-full py-3 rounded-xl font-semibold text-white transition-all duration-300 disabled:opacity-50"
          style="background: var(--gradient-primary)"
        >
          {{ loading ? 'Kirish...' : 'Kirish' }}
        </button>
      </form>

      <!-- Back link -->
      <div class="text-center mt-6">
        <NuxtLink to="/" class="text-sm text-gray-500 hover:text-gray-300 transition-colors">
          Bosh sahifaga qaytish
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
