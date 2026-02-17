<script setup lang="ts">
definePageMeta({ layout: 'admin', middleware: 'admin' })
useHead({ title: 'Scheduler — Mirbazar Admin' })

const { getSchedulerJobs, triggerJob } = useAdmin()
const { success: showSuccess, error: showError } = useToast()

const loading = ref(true)
const jobs = ref<Record<string, unknown>[]>([])
const triggeringId = ref<string | null>(null)

const showConfirmModal = ref(false)
const confirmJobId = ref('')
const confirmJobName = ref('')

const utilityJobs = [
  { id: 'regenerate_images', name: 'Rasmsiz e\'lonlarga rasm yaratish', description: 'Image_url bo\'sh bo\'lgan barcha aktiv e\'lonlarga brendli rasm generatsiya qiladi' },
  { id: 'regenerate_all_images', name: 'Barcha rasmlarni qayta yaratish', description: 'Barcha aktiv e\'lonlar uchun professional rasmlarni qayta generatsiya qiladi' },
]
const triggeringUtility = ref<string | null>(null)

async function handleUtilityTrigger(jobId: string) {
  triggeringUtility.value = jobId
  try {
    const result = await triggerJob(jobId)
    showSuccess(result.message)
  } catch {
    showError('Job ishga tushirishda xatolik')
  } finally {
    triggeringUtility.value = null
  }
}

const columns = [
  { key: 'id', label: 'ID' },
  { key: 'name', label: 'Nomi' },
  { key: 'trigger', label: 'Trigger' },
  { key: 'next_run_time', label: 'Keyingi ishga tushish' },
  { key: 'actions', label: '' },
]

async function loadJobs() {
  loading.value = true
  try {
    const data = await getSchedulerJobs()
    jobs.value = data.jobs as unknown as Record<string, unknown>[]
  } catch {
    showError('Joblarni yuklashda xatolik')
  } finally {
    loading.value = false
  }
}

function confirmTrigger(jobId: string, jobName: string) {
  confirmJobId.value = jobId
  confirmJobName.value = jobName
  showConfirmModal.value = true
}

async function handleTrigger() {
  const jobId = confirmJobId.value
  showConfirmModal.value = false
  triggeringId.value = jobId

  try {
    const result = await triggerJob(jobId)
    showSuccess(result.message)
  } catch {
    showError('Job ishga tushirishda xatolik')
  } finally {
    triggeringId.value = null
  }
}

onMounted(loadJobs)
</script>

<template>
  <div>
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-2xl font-bold text-white">Scheduler</h2>
      <button
        class="px-4 py-2 rounded-xl text-sm font-medium text-purple-400 hover:text-white hover:bg-purple-500/20 border border-purple-500/30 transition-colors"
        @click="loadJobs"
      >
        Yangilash
      </button>
    </div>

    <AdminDataTable
      :columns="columns"
      :rows="jobs"
      :total="jobs.length"
      :page="1"
      :limit="100"
      :loading="loading"
    >
      <template #cell-name="{ value }">
        <span class="text-white font-medium">{{ value }}</span>
      </template>
      <template #cell-trigger="{ value }">
        <span class="text-gray-400 text-xs font-mono">{{ value }}</span>
      </template>
      <template #cell-next_run_time="{ value }">
        <span class="text-cyan-400 text-sm">
          {{ value || 'Noma\'lum' }}
        </span>
      </template>
      <template #cell-actions="{ row }">
        <div @click.stop>
          <button
            :disabled="triggeringId === (row as Record<string, unknown>).id"
            class="px-3 py-1.5 rounded-lg text-xs font-medium bg-purple-500/20 text-purple-400 border border-purple-500/30 hover:bg-purple-500/30 transition-colors disabled:opacity-50"
            @click="confirmTrigger((row as Record<string, unknown>).id as string, (row as Record<string, unknown>).name as string)"
          >
            {{ triggeringId === (row as Record<string, unknown>).id ? 'Ishlamoqda...' : 'Ishga tushirish' }}
          </button>
        </div>
      </template>
    </AdminDataTable>

    <!-- Utility Jobs -->
    <div class="mt-10">
      <h3 class="text-lg font-bold text-white mb-4">Qo'shimcha amallar</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div
          v-for="job in utilityJobs"
          :key="job.id"
          class="glass-card p-5 flex items-center justify-between gap-4"
        >
          <div>
            <p class="text-white font-medium">{{ job.name }}</p>
            <p class="text-gray-500 text-sm mt-1">{{ job.description }}</p>
          </div>
          <button
            :disabled="triggeringUtility === job.id"
            class="shrink-0 px-4 py-2 rounded-xl text-sm font-medium bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 hover:bg-cyan-500/30 transition-colors disabled:opacity-50"
            @click="handleUtilityTrigger(job.id)"
          >
            {{ triggeringUtility === job.id ? 'Ishlamoqda...' : 'Ishga tushirish' }}
          </button>
        </div>
      </div>
    </div>

    <AdminModal
      :show="showConfirmModal"
      :title="`'${confirmJobName}' ni ishga tushirish`"
      confirm-text="Ishga tushirish"
      @confirm="handleTrigger"
      @cancel="showConfirmModal = false"
    >
      <p class="text-gray-300">Bu jobni hozir ishga tushirmoqchimisiz?</p>
    </AdminModal>
  </div>
</template>
