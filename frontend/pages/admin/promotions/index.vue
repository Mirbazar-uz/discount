<script setup lang="ts">
definePageMeta({ layout: 'admin', middleware: 'admin' })
useHead({ title: 'Aksiyalar — Mirbazar Admin' })

const { getPromotions, deletePromotion, changePromotionStatus } = useAdmin()
const { success: showSuccess, error: showError } = useToast()

const loading = ref(true)
const promotions = ref<Record<string, unknown>[]>([])
const total = ref(0)
const page = ref(1)
const limit = 20

const statusFilter = ref('all')
const searchQuery = ref('')

const deleteTarget = ref<number | null>(null)
const showDeleteModal = ref(false)

const columns = [
  { key: 'id', label: 'ID', sortable: true },
  { key: 'title', label: 'Nomi', sortable: true },
  { key: 'store_name', label: "Do'kon" },
  { key: 'discount_percent', label: 'Chegirma', sortable: true },
  { key: 'status', label: 'Status' },
  { key: 'posted_telegram', label: 'TG' },
  { key: 'created_at', label: 'Sana', sortable: true },
  { key: 'actions', label: '' },
]

async function loadPromotions() {
  loading.value = true
  try {
    const params: Record<string, string> = {
      limit: String(limit),
      offset: String((page.value - 1) * limit),
    }
    if (statusFilter.value !== 'all') params.status = statusFilter.value
    if (searchQuery.value) params.search = searchQuery.value

    const data = await getPromotions(params)
    promotions.value = data.promotions as unknown as Record<string, unknown>[]
    total.value = data.total
  } catch {
    showError('Aksiyalarni yuklashda xatolik')
  } finally {
    loading.value = false
  }
}

function onPageChange(newPage: number) {
  page.value = newPage
  loadPromotions()
}

function confirmDelete(id: number) {
  deleteTarget.value = id
  showDeleteModal.value = true
}

async function handleDelete() {
  if (!deleteTarget.value) return
  try {
    await deletePromotion(deleteTarget.value)
    showSuccess("Aksiya o'chirildi")
    showDeleteModal.value = false
    deleteTarget.value = null
    await loadPromotions()
  } catch {
    showError("O'chirishda xatolik")
  }
}

async function handleStatusChange(id: number, status: string) {
  try {
    await changePromotionStatus(id, status)
    showSuccess('Status yangilandi')
    await loadPromotions()
  } catch {
    showError('Status yangilashda xatolik')
  }
}

watch([statusFilter, searchQuery], () => {
  page.value = 1
  loadPromotions()
})

onMounted(loadPromotions)
</script>

<template>
  <div>
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
      <h2 class="text-2xl font-bold text-white">Aksiyalar</h2>
      <div class="flex items-center gap-3">
        <input
          v-model="searchQuery"
          placeholder="Qidirish..."
          class="px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-white text-sm placeholder-gray-500 focus:outline-none focus:border-purple-500/50 transition-colors w-48"
        />
        <select
          v-model="statusFilter"
          class="px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-white text-sm focus:outline-none focus:border-purple-500/50 appearance-none"
        >
          <option value="all">Barchasi</option>
          <option value="active">Faol</option>
          <option value="expired">O'tgan</option>
          <option value="deleted">O'chirilgan</option>
        </select>
      </div>
    </div>

    <AdminDataTable
      :columns="columns"
      :rows="promotions"
      :total="total"
      :page="page"
      :limit="limit"
      :loading="loading"
      @page-change="onPageChange"
      @row-click="navigateTo(`/admin/promotions/${($event as Record<string, unknown>).id}`)"
    >
      <template #cell-title="{ value }">
        <span class="text-white max-w-[200px] truncate block">{{ value }}</span>
      </template>
      <template #cell-discount_percent="{ value }">
        <span v-if="value" class="text-purple-400 font-semibold">-{{ value }}%</span>
        <span v-else class="text-gray-500">-</span>
      </template>
      <template #cell-status="{ value }">
        <span
          :class="[
            'px-2 py-1 rounded-lg text-xs font-medium',
            value === 'active' ? 'bg-green-500/20 text-green-400' :
            value === 'expired' ? 'bg-yellow-500/20 text-yellow-400' :
            'bg-red-500/20 text-red-400',
          ]"
        >
          {{ value === 'active' ? 'Faol' : value === 'expired' ? "O'tgan" : "O'chirilgan" }}
        </span>
      </template>
      <template #cell-posted_telegram="{ value }">
        <span :class="value ? 'text-green-400' : 'text-gray-600'">
          {{ value ? '&#10003;' : '&#10005;' }}
        </span>
      </template>
      <template #cell-created_at="{ value }">
        <span class="text-gray-400 text-xs">
          {{ value ? new Date(value as string).toLocaleDateString('uz-UZ') : '-' }}
        </span>
      </template>
      <template #cell-actions="{ row }">
        <div class="flex items-center gap-2" @click.stop>
          <button
            v-if="(row as Record<string, unknown>).status === 'active'"
            class="text-yellow-400 hover:text-yellow-300 text-xs"
            title="Muddatini o'tkazish"
            @click="handleStatusChange((row as Record<string, unknown>).id as number, 'expired')"
          >
            Expire
          </button>
          <button
            v-if="(row as Record<string, unknown>).status === 'expired'"
            class="text-green-400 hover:text-green-300 text-xs"
            title="Faollashtirish"
            @click="handleStatusChange((row as Record<string, unknown>).id as number, 'active')"
          >
            Activate
          </button>
          <button
            class="text-red-400 hover:text-red-300 text-xs"
            title="O'chirish"
            @click="confirmDelete((row as Record<string, unknown>).id as number)"
          >
            Delete
          </button>
        </div>
      </template>
    </AdminDataTable>

    <!-- Delete Modal -->
    <AdminModal
      :show="showDeleteModal"
      title="Aksiyani o'chirish"
      confirm-text="O'chirish"
      :danger="true"
      @confirm="handleDelete"
      @cancel="showDeleteModal = false"
    >
      <p class="text-gray-300">Haqiqatan ham bu aksiyani o'chirmoqchimisiz?</p>
    </AdminModal>
  </div>
</template>
