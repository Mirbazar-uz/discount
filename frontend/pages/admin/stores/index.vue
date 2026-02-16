<script setup lang="ts">
definePageMeta({ layout: 'admin', middleware: 'admin' })
useHead({ title: "Do'konlar — Mirbazar Admin" })

const { getStores, toggleStore } = useAdmin()
const { success: showSuccess, error: showError } = useToast()

const loading = ref(true)
const stores = ref<Record<string, unknown>[]>([])

const columns = [
  { key: 'id', label: 'ID', sortable: true },
  { key: 'name', label: 'Nomi', sortable: true },
  { key: 'slug', label: 'Slug' },
  { key: 'category', label: 'Kategoriya' },
  { key: 'promotion_count', label: 'Aksiyalar', sortable: true },
  { key: 'is_active', label: 'Status' },
  { key: 'actions', label: '' },
]

async function loadStores() {
  loading.value = true
  try {
    const data = await getStores()
    stores.value = data.stores as unknown as Record<string, unknown>[]
  } catch {
    showError("Do'konlarni yuklashda xatolik")
  } finally {
    loading.value = false
  }
}

async function handleToggle(id: number) {
  try {
    await toggleStore(id)
    showSuccess('Status yangilandi')
    await loadStores()
  } catch {
    showError('Status yangilashda xatolik')
  }
}

onMounted(loadStores)
</script>

<template>
  <div>
    <h2 class="text-2xl font-bold text-white mb-6">Do'konlar</h2>

    <AdminDataTable
      :columns="columns"
      :rows="stores"
      :total="stores.length"
      :page="1"
      :limit="100"
      :loading="loading"
      @row-click="navigateTo(`/admin/stores/${($event as Record<string, unknown>).id}`)"
    >
      <template #cell-name="{ row }">
        <div class="flex items-center gap-2">
          <div
            class="w-3 h-3 rounded-full"
            :style="{ background: (row as Record<string, unknown>).color as string || '#7c3aed' }"
          />
          <span class="text-white font-medium">{{ (row as Record<string, unknown>).name }}</span>
        </div>
      </template>
      <template #cell-promotion_count="{ value }">
        <span class="text-purple-400 font-semibold">{{ value }}</span>
      </template>
      <template #cell-is_active="{ value }">
        <span
          :class="[
            'px-2 py-1 rounded-lg text-xs font-medium',
            value ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400',
          ]"
        >
          {{ value ? 'Faol' : 'Nofaol' }}
        </span>
      </template>
      <template #cell-actions="{ row }">
        <div @click.stop>
          <button
            :class="[
              'text-xs font-medium transition-colors',
              (row as Record<string, unknown>).is_active
                ? 'text-red-400 hover:text-red-300'
                : 'text-green-400 hover:text-green-300',
            ]"
            @click="handleToggle((row as Record<string, unknown>).id as number)"
          >
            {{ (row as Record<string, unknown>).is_active ? "O'chirish" : 'Yoqish' }}
          </button>
        </div>
      </template>
    </AdminDataTable>
  </div>
</template>
