<script setup lang="ts">
definePageMeta({ layout: 'admin', middleware: 'admin' })
useHead({ title: 'Dashboard — Mirbazar Admin' })

const { getDashboard } = useAdmin()
const { error: showError } = useToast()

const loading = ref(true)
const stats = ref({
  total_promotions: 0,
  active_promotions: 0,
  expired_promotions: 0,
  total_stores: 0,
  active_stores: 0,
  total_posts: 0,
  successful_posts: 0,
  failed_posts: 0,
})
const recentPromotions = ref<Record<string, unknown>[]>([])

const recentColumns = [
  { key: 'title', label: 'Nomi' },
  { key: 'store_name', label: "Do'kon" },
  { key: 'status', label: 'Status' },
  { key: 'discount_percent', label: 'Chegirma %' },
  { key: 'created_at', label: 'Sana' },
]

async function loadDashboard() {
  loading.value = true
  try {
    const data = await getDashboard()
    stats.value = data.stats
    recentPromotions.value = data.recent_promotions as unknown as Record<string, unknown>[]
  } catch {
    showError("Dashboard ma'lumotlarini yuklashda xatolik")
  } finally {
    loading.value = false
  }
}

onMounted(loadDashboard)
</script>

<template>
  <div>
    <h2 class="text-2xl font-bold text-white mb-6">Dashboard</h2>

    <!-- Stats Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      <AdminStatCard title="Jami aksiyalar" :value="stats.total_promotions" icon="promotions" />
      <AdminStatCard title="Faol aksiyalar" :value="stats.active_promotions" icon="active" color="green" />
      <AdminStatCard title="Muddati o'tgan" :value="stats.expired_promotions" icon="expired" color="red" />
      <AdminStatCard title="Faol do'konlar" :value="stats.active_stores" icon="stores" color="cyan" />
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      <AdminStatCard title="Jami do'konlar" :value="stats.total_stores" icon="stores" color="cyan" />
      <AdminStatCard title="Jami postlar" :value="stats.total_posts" icon="posts" color="yellow" />
      <AdminStatCard title="Muvaffaqiyatli" :value="stats.successful_posts" icon="active" color="green" />
      <AdminStatCard title="Xatoliklar" :value="stats.failed_posts" icon="expired" color="red" />
    </div>

    <!-- Recent Promotions -->
    <h3 class="text-lg font-semibold text-white mb-4">So'nggi aksiyalar</h3>
    <AdminDataTable
      :columns="recentColumns"
      :rows="recentPromotions"
      :total="recentPromotions.length"
      :page="1"
      :limit="10"
      :loading="loading"
      @row-click="navigateTo(`/admin/promotions/${($event as Record<string, unknown>).id}`)"
    >
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
      <template #cell-discount_percent="{ value }">
        <span v-if="value" class="text-purple-400 font-semibold">-{{ value }}%</span>
        <span v-else class="text-gray-500">-</span>
      </template>
      <template #cell-created_at="{ value }">
        <span class="text-gray-400 text-xs">
          {{ value ? new Date(value as string).toLocaleDateString('uz-UZ') : '-' }}
        </span>
      </template>
    </AdminDataTable>
  </div>
</template>
