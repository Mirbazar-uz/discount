interface AdminPromotion {
  id: number
  title: string
  description?: string
  old_price?: number
  new_price?: number
  discount_percent?: number
  discount_text?: string
  category?: string
  deadline_text?: string
  source_url?: string
  image_url?: string
  status: string
  store_name: string
  store_slug: string
  posted_telegram: boolean
  posted_instagram: boolean
  created_at?: string
}

interface AdminPromotionList {
  promotions: AdminPromotion[]
  total: number
  page: number
  limit: number
}

interface DashboardStats {
  total_promotions: number
  active_promotions: number
  expired_promotions: number
  total_stores: number
  active_stores: number
  total_posts: number
  successful_posts: number
  failed_posts: number
}

interface DashboardResponse {
  stats: DashboardStats
  recent_promotions: AdminPromotion[]
}

interface AdminStore {
  id: number
  name: string
  slug: string
  telegram_channel?: string
  website?: string
  color?: string
  category?: string
  is_active: boolean
  promotion_count: number
  created_at?: string
}

interface AdminStoreList {
  stores: AdminStore[]
  total: number
}

interface SchedulerJob {
  id: string
  name: string
  next_run_time?: string
  trigger: string
}

interface PostLogEntry {
  id: number
  promotion_id?: number
  promotion_title?: string
  platform?: string
  post_type?: string
  post_id?: string
  success: boolean
  error_message?: string
  posted_at?: string
}

interface PostLogList {
  logs: PostLogEntry[]
  total: number
  page: number
  limit: number
}

export function useAdmin() {
  const config = useRuntimeConfig()
  const { getToken } = useAuth()

  const baseURL = import.meta.server
    ? (config.apiBaseServer as string)
    : (config.public.apiBase as string)

  async function fetchAdminApi<T>(
    endpoint: string,
    options: {
      method?: string
      body?: Record<string, unknown>
      params?: Record<string, string>
    } = {},
  ): Promise<T> {
    const path = endpoint.startsWith('/') ? endpoint : `/${endpoint}`
    let url = `${baseURL}${path}`

    if (options.params) {
      const searchParams = new URLSearchParams()
      Object.entries(options.params).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== '') {
          searchParams.set(key, value)
        }
      })
      const qs = searchParams.toString()
      if (qs) url += `?${qs}`
    }

    const token = getToken()
    const headers: Record<string, string> = {}
    if (token) {
      headers['Authorization'] = `Bearer ${token}`
    }

    try {
      const response = await $fetch<T>(url, {
        method: (options.method || 'GET') as 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE',
        headers,
        body: options.body,
      })
      return response
    } catch (error: unknown) {
      const fetchError = error as { status?: number }
      if (fetchError.status === 401) {
        const { logout } = useAuth()
        logout()
      }
      throw error
    }
  }

  async function getDashboard(): Promise<DashboardResponse> {
    return fetchAdminApi<DashboardResponse>('/admin/dashboard/stats')
  }

  async function getPromotions(params?: Record<string, string>): Promise<AdminPromotionList> {
    return fetchAdminApi<AdminPromotionList>('/admin/promotions', { params })
  }

  async function updatePromotion(id: number, data: Record<string, unknown>): Promise<AdminPromotion> {
    return fetchAdminApi<AdminPromotion>(`/admin/promotions/${id}`, {
      method: 'PUT',
      body: data,
    })
  }

  async function deletePromotion(id: number): Promise<void> {
    await fetchAdminApi(`/admin/promotions/${id}`, { method: 'DELETE' })
  }

  async function changePromotionStatus(id: number, status: string): Promise<AdminPromotion> {
    return fetchAdminApi<AdminPromotion>(`/admin/promotions/${id}/status`, {
      method: 'PATCH',
      body: { status },
    })
  }

  async function getStores(): Promise<AdminStoreList> {
    return fetchAdminApi<AdminStoreList>('/admin/stores')
  }

  async function updateStore(id: number, data: Record<string, unknown>): Promise<AdminStore> {
    return fetchAdminApi<AdminStore>(`/admin/stores/${id}`, {
      method: 'PUT',
      body: data,
    })
  }

  async function toggleStore(id: number): Promise<AdminStore> {
    return fetchAdminApi<AdminStore>(`/admin/stores/${id}/toggle`, {
      method: 'PATCH',
    })
  }

  async function getSchedulerJobs(): Promise<{ jobs: SchedulerJob[] }> {
    return fetchAdminApi<{ jobs: SchedulerJob[] }>('/admin/scheduler/jobs')
  }

  async function triggerJob(jobId: string): Promise<{ success: boolean; message: string }> {
    return fetchAdminApi<{ success: boolean; message: string }>(
      `/admin/scheduler/trigger/${jobId}`,
      { method: 'POST' },
    )
  }

  async function getLogs(params?: Record<string, string>): Promise<PostLogList> {
    return fetchAdminApi<PostLogList>('/admin/logs', { params })
  }

  return {
    fetchAdminApi,
    getDashboard,
    getPromotions,
    updatePromotion,
    deletePromotion,
    changePromotionStatus,
    getStores,
    updateStore,
    toggleStore,
    getSchedulerJobs,
    triggerJob,
    getLogs,
  }
}
