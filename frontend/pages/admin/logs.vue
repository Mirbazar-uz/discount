<script setup lang="ts">
definePageMeta({ layout: 'admin', middleware: 'admin' })
useHead({ title: 'Loglar — Mirbazar Admin' })

const { getLogs } = useAdmin()
const { error: showError } = useToast()

const loading = ref(true)
const logs = ref<Record<string, unknown>[]>([])
const total = ref(0)
const page = ref(1)
const limit = 20

const platformFilter = ref('')
const successFilter = ref('')

const columns = [
  { key: 'id', label: 'ID', sortable: true },
  { key: 'promotion_title', label: 'Aksiya' },
  { key: 'platform', label: 'Platform' },
  { key: 'post_type', label: 'Tur' },
  { key: 'success', label: 'Natija' },
  { key: 'error_message', label: 'Xatolik' },
  { key: 'posted_at', label: 'Sana', sortable: true },
]

async function loadLogs() {
  loading.value = true
  try {
    const params: Record<string, string> = {
      limit: String(limit),
      offset: String((page.value - 1) * limit),
    }
    if (platformFilter.value) params.platform = platformFilter.value
    if (successFilter.value) params.success = successFilter.value

    const data = await getLogs(params)
    logs.value = data.logs as unknown as Record<string, unknown>[]
    total.value = data.total
  } catch {
    showError('Loglarni yuklashda xatolik')
  } finally {
    loading.value = false
  }
}

function onPageChange(newPage: number) {
  page.value = newPage
  loadLogs()
}

watch([platformFilter, successFilter], () => {
  page.value = 1
  loadLogs()
})

onMounted(loadLogs)
</script>

<template>
  <div>
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
      <h2 class="text-2xl font-bold text-white">Post Loglar</h2>
      <div class="flex items-center gap-3">
        <select
          v-model="platformFilter"
          class="px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-white text-sm focus:outline-none focus:border-purple-500/50 appearance-none"
        >
          <option value="">Barcha platformalar</option>
          <option value="telegram">Telegram</option>
          <option value="instagram">Instagram</option>
        </select>
        <select
          v-model="successFilter"
          class="px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-white text-sm focus:outline-none focus:border-purple-500/50 appearance-none"
        >
          <option value="">Barchasi</option>
          <option value="true">Muvaffaqiyatli</option>
          <option value="false">Xatolik</option>
        </select>
      </div>
    </div>

    <AdminDataTable
      :columns="columns"
      :rows="logs"
      :total="total"
      :page="page"
      :limit="limit"
      :loading="loading"
      @page-change="onPageChange"
    >
      <template #cell-promotion_title="{ value }">
        <span class="text-white max-w-[200px] truncate block">{{ value || '-' }}</span>
      </template>
      <template #cell-platform="{ value }">
        <span
          :class="[
            'px-2 py-1 rounded-lg text-xs font-medium',
            value === 'telegram' ? 'bg-blue-500/20 text-blue-400' : 'bg-pink-500/20 text-pink-400',
          ]"
        >
          {{ value === 'telegram' ? 'Telegram' : 'Instagram' }}
        </span>
      </template>
      <template #cell-success="{ value }">
        <span
          :class="[
            'px-2 py-1 rounded-lg text-xs font-medium',
            value ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400',
          ]"
        >
          {{ value ? 'OK' : 'Xatolik' }}
        </span>
      </template>
      <template #cell-error_message="{ value }">
        <span class="text-red-400 text-xs max-w-[150px] truncate block">{{ value || '-' }}</span>
      </template>
      <template #cell-posted_at="{ value }">
        <span class="text-gray-400 text-xs">
          {{ value ? new Date(value as string).toLocaleString('uz-UZ') : '-' }}
        </span>
      </template>
    </AdminDataTable>
  </div>
</template>
