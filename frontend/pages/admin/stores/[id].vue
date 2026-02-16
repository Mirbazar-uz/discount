<script setup lang="ts">
definePageMeta({ layout: 'admin', middleware: 'admin' })

const route = useRoute()
const storeId = Number(route.params.id)

const { getStores, updateStore } = useAdmin()
const { success: showSuccess, error: showError } = useToast()

useHead({ title: `Do'kon #${storeId} — Mirbazar Admin` })

const loading = ref(true)
const saving = ref(false)

const form = ref({
  name: '',
  slug: '',
  telegram_channel: '',
  website: '',
  color: '#7c3aed',
  category: '',
})

async function loadStore() {
  loading.value = true
  try {
    const data = await getStores()
    const found = data.stores.find((s) => s.id === storeId)
    if (found) {
      form.value = {
        name: found.name || '',
        slug: found.slug || '',
        telegram_channel: found.telegram_channel || '',
        website: found.website || '',
        color: found.color || '#7c3aed',
        category: found.category || '',
      }
    }
  } catch {
    showError("Do'konni yuklashda xatolik")
  } finally {
    loading.value = false
  }
}

async function handleSave() {
  saving.value = true
  try {
    const updateData: Record<string, unknown> = {}
    if (form.value.name) updateData.name = form.value.name
    if (form.value.slug) updateData.slug = form.value.slug
    if (form.value.telegram_channel) updateData.telegram_channel = form.value.telegram_channel
    if (form.value.website) updateData.website = form.value.website
    if (form.value.color) updateData.color = form.value.color
    if (form.value.category) updateData.category = form.value.category

    await updateStore(storeId, updateData)
    showSuccess("Do'kon yangilandi")
    navigateTo('/admin/stores')
  } catch {
    showError('Saqlashda xatolik')
  } finally {
    saving.value = false
  }
}

onMounted(loadStore)
</script>

<template>
  <div>
    <div class="flex items-center gap-4 mb-6">
      <NuxtLink to="/admin/stores" class="text-gray-400 hover:text-white transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
      </NuxtLink>
      <h2 class="text-2xl font-bold text-white">Do'kon #{{ storeId }}</h2>
    </div>

    <div v-if="loading" class="glass-card p-8 text-center">
      <div class="inline-block w-8 h-8 border-2 border-purple-500 border-t-transparent rounded-full animate-spin" />
    </div>

    <form v-else class="glass-card p-6 space-y-6" @submit.prevent="handleSave">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Nomi</label>
          <input
            v-model="form.name"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Slug</label>
          <input
            v-model="form.slug"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
          />
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Telegram kanal</label>
          <input
            v-model="form.telegram_channel"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Veb-sayt</label>
          <input
            v-model="form.website"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
          />
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Rang</label>
          <div class="flex items-center gap-3">
            <input
              v-model="form.color"
              type="color"
              class="w-12 h-12 rounded-xl border border-white/10 cursor-pointer bg-transparent"
            />
            <input
              v-model="form.color"
              class="flex-1 px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
            />
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Kategoriya</label>
          <input
            v-model="form.category"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
          />
        </div>
      </div>

      <div class="flex justify-end gap-3 pt-4 border-t border-white/10">
        <NuxtLink
          to="/admin/stores"
          class="px-6 py-3 rounded-xl text-sm font-medium text-gray-400 hover:text-white hover:bg-white/10 transition-colors"
        >
          Bekor qilish
        </NuxtLink>
        <button
          type="submit"
          :disabled="saving"
          class="px-6 py-3 rounded-xl text-sm font-medium text-white transition-all duration-300 disabled:opacity-50"
          style="background: var(--gradient-primary)"
        >
          {{ saving ? 'Saqlanmoqda...' : 'Saqlash' }}
        </button>
      </div>
    </form>
  </div>
</template>
