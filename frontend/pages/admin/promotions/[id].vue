<script setup lang="ts">
definePageMeta({ layout: 'admin', middleware: 'admin' })

const route = useRoute()
const promoId = Number(route.params.id)

const { getPromotions, updatePromotion } = useAdmin()
const { success: showSuccess, error: showError } = useToast()

useHead({ title: `Aksiya #${promoId} — Mirbazar Admin` })

const loading = ref(true)
const saving = ref(false)

const form = ref({
  title: '',
  description: '',
  old_price: null as number | null,
  new_price: null as number | null,
  discount_percent: null as number | null,
  discount_text: '',
  category: '',
  deadline_text: '',
})

const promotion = ref<Record<string, unknown> | null>(null)

async function loadPromotion() {
  loading.value = true
  try {
    const data = await getPromotions({ limit: '1', offset: '0' })
    const allData = await getPromotions({ limit: '100', offset: '0', status: 'all' })
    const found = allData.promotions.find((p) => p.id === promoId)
    if (found) {
      promotion.value = found as unknown as Record<string, unknown>
      form.value = {
        title: found.title || '',
        description: found.description || '',
        old_price: found.old_price || null,
        new_price: found.new_price || null,
        discount_percent: found.discount_percent || null,
        discount_text: found.discount_text || '',
        category: found.category || '',
        deadline_text: found.deadline_text || '',
      }
    }
  } catch {
    showError('Aksiyani yuklashda xatolik')
  } finally {
    loading.value = false
  }
}

async function handleSave() {
  saving.value = true
  try {
    const updateData: Record<string, unknown> = {}
    if (form.value.title) updateData.title = form.value.title
    if (form.value.description) updateData.description = form.value.description
    if (form.value.old_price !== null) updateData.old_price = form.value.old_price
    if (form.value.new_price !== null) updateData.new_price = form.value.new_price
    if (form.value.discount_percent !== null) updateData.discount_percent = form.value.discount_percent
    if (form.value.discount_text) updateData.discount_text = form.value.discount_text
    if (form.value.category) updateData.category = form.value.category
    if (form.value.deadline_text) updateData.deadline_text = form.value.deadline_text

    await updatePromotion(promoId, updateData)
    showSuccess('Aksiya yangilandi')
    navigateTo('/admin/promotions')
  } catch {
    showError('Saqlashda xatolik')
  } finally {
    saving.value = false
  }
}

onMounted(loadPromotion)
</script>

<template>
  <div>
    <div class="flex items-center gap-4 mb-6">
      <NuxtLink to="/admin/promotions" class="text-gray-400 hover:text-white transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
      </NuxtLink>
      <h2 class="text-2xl font-bold text-white">Aksiya #{{ promoId }}</h2>
    </div>

    <div v-if="loading" class="glass-card p-8 text-center">
      <div class="inline-block w-8 h-8 border-2 border-purple-500 border-t-transparent rounded-full animate-spin" />
    </div>

    <form v-else class="glass-card p-6 space-y-6" @submit.prevent="handleSave">
      <!-- Title -->
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Nomi</label>
        <input
          v-model="form.title"
          class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500/50 transition-colors"
        />
      </div>

      <!-- Description -->
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Tavsif</label>
        <textarea
          v-model="form.description"
          rows="3"
          class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500/50 transition-colors resize-none"
        />
      </div>

      <!-- Prices -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Eski narx</label>
          <input
            v-model.number="form.old_price"
            type="number"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Yangi narx</label>
          <input
            v-model.number="form.new_price"
            type="number"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Chegirma %</label>
          <input
            v-model.number="form.discount_percent"
            type="number"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
          />
        </div>
      </div>

      <!-- Category & Discount Text -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Kategoriya</label>
          <input
            v-model="form.category"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">Chegirma matni</label>
          <input
            v-model="form.discount_text"
            class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
          />
        </div>
      </div>

      <!-- Deadline -->
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">Muddat matni</label>
        <input
          v-model="form.deadline_text"
          class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500/50 transition-colors"
        />
      </div>

      <!-- Actions -->
      <div class="flex justify-end gap-3 pt-4 border-t border-white/10">
        <NuxtLink
          to="/admin/promotions"
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
