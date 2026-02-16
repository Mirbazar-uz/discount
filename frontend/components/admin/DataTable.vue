<script setup lang="ts">
interface Column {
  key: string
  label: string
  sortable?: boolean
}

const props = defineProps<{
  columns: Column[]
  rows: Record<string, unknown>[]
  total: number
  page: number
  limit: number
  loading?: boolean
}>()

const emit = defineEmits<{
  (e: 'page-change', page: number): void
  (e: 'row-click', row: Record<string, unknown>): void
}>()

const totalPages = computed(() => Math.ceil(props.total / props.limit))

const sortKey = ref('')
const sortDir = ref<'asc' | 'desc'>('desc')

function toggleSort(key: string) {
  if (sortKey.value === key) {
    sortDir.value = sortDir.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortDir.value = 'desc'
  }
}

const sortedRows = computed(() => {
  if (!sortKey.value) return props.rows

  return [...props.rows].sort((a, b) => {
    const aVal = a[sortKey.value]
    const bVal = b[sortKey.value]

    if (aVal == null) return 1
    if (bVal == null) return -1

    if (typeof aVal === 'number' && typeof bVal === 'number') {
      return sortDir.value === 'asc' ? aVal - bVal : bVal - aVal
    }

    const aStr = String(aVal)
    const bStr = String(bVal)
    return sortDir.value === 'asc'
      ? aStr.localeCompare(bStr)
      : bStr.localeCompare(aStr)
  })
})

function goToPage(page: number) {
  if (page >= 1 && page <= totalPages.value) {
    emit('page-change', page)
  }
}
</script>

<template>
  <div class="glass-card overflow-hidden">
    <!-- Loading overlay -->
    <div v-if="loading" class="p-8 text-center">
      <div class="inline-block w-8 h-8 border-2 border-purple-500 border-t-transparent rounded-full animate-spin" />
      <p class="text-gray-400 mt-2 text-sm">Yuklanmoqda...</p>
    </div>

    <!-- Table -->
    <div v-else class="overflow-x-auto">
      <table class="w-full">
        <thead>
          <tr class="border-b border-white/10">
            <th
              v-for="col in columns"
              :key="col.key"
              class="px-6 py-4 text-left text-xs font-medium text-gray-400 uppercase tracking-wider"
              :class="{ 'cursor-pointer hover:text-white': col.sortable }"
              @click="col.sortable ? toggleSort(col.key) : undefined"
            >
              <div class="flex items-center gap-1">
                {{ col.label }}
                <span v-if="col.sortable && sortKey === col.key" class="text-purple-400">
                  {{ sortDir === 'asc' ? '&#9650;' : '&#9660;' }}
                </span>
              </div>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(row, idx) in sortedRows"
            :key="idx"
            class="border-b border-white/5 hover:bg-white/[0.03] transition-colors cursor-pointer"
            @click="$emit('row-click', row)"
          >
            <td
              v-for="col in columns"
              :key="col.key"
              class="px-6 py-4 text-sm text-gray-300 whitespace-nowrap"
            >
              <slot :name="`cell-${col.key}`" :row="row" :value="row[col.key]">
                {{ row[col.key] ?? '-' }}
              </slot>
            </td>
          </tr>
          <tr v-if="sortedRows.length === 0">
            <td :colspan="columns.length" class="px-6 py-12 text-center text-gray-500">
              Ma'lumot topilmadi
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pagination -->
    <div v-if="totalPages > 1" class="flex items-center justify-between px-6 py-4 border-t border-white/10">
      <p class="text-sm text-gray-400">
        Jami: <span class="text-white">{{ total }}</span>
      </p>
      <div class="flex items-center gap-2">
        <button
          :disabled="page <= 1"
          class="px-3 py-1 rounded-lg text-sm transition-colors"
          :class="page <= 1 ? 'text-gray-600 cursor-not-allowed' : 'text-gray-400 hover:text-white hover:bg-white/10'"
          @click="goToPage(page - 1)"
        >
          Oldingi
        </button>
        <span class="text-sm text-gray-400">
          {{ page }} / {{ totalPages }}
        </span>
        <button
          :disabled="page >= totalPages"
          class="px-3 py-1 rounded-lg text-sm transition-colors"
          :class="page >= totalPages ? 'text-gray-600 cursor-not-allowed' : 'text-gray-400 hover:text-white hover:bg-white/10'"
          @click="goToPage(page + 1)"
        >
          Keyingi
        </button>
      </div>
    </div>
  </div>
</template>
