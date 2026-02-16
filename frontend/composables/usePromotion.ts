interface Promotion {
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
  store: string
  store_slug: string
  days_left?: number
  created_at?: string
}

interface PromotionListResponse {
  promotions: Promotion[]
  total: number
  page: number
  limit: number
}

interface RatingStore {
  name: string
  slug: string
  color?: string
  count: number
  max_discount: number
  avg_discount: number
}

interface RatingResponse {
  stores: RatingStore[]
  period: string
}

interface StatsResponse {
  total_promotions: number
  active_promotions: number
  total_stores: number
  max_discount: number
}

export function usePromotion() {
  const { fetchApi } = useApi()

  async function getPromotions(params?: Record<string, string>): Promise<PromotionListResponse> {
    return fetchApi<PromotionListResponse>('/promotions', params)
  }

  async function getPromotion(id: number): Promise<Promotion> {
    return fetchApi<Promotion>(`/promotions/${id}`)
  }

  async function getWeeklyRating(): Promise<RatingResponse> {
    return fetchApi<RatingResponse>('/rating/weekly')
  }

  async function getStats(): Promise<StatsResponse> {
    return fetchApi<StatsResponse>('/stats')
  }

  function formatPrice(price: number): string {
    return new Intl.NumberFormat('uz-UZ').format(price)
  }

  return {
    getPromotions,
    getPromotion,
    getWeeklyRating,
    getStats,
    formatPrice,
  }
}
