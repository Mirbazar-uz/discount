export function useApi() {
  const config = useRuntimeConfig()
  const baseURL = config.public.apiBase as string

  async function fetchApi<T>(endpoint: string, params?: Record<string, string>): Promise<T> {
    const url = new URL(endpoint, baseURL)

    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value) {
          url.searchParams.set(key, value)
        }
      })
    }

    try {
      const response = await $fetch<T>(url.toString())
      return response
    } catch (error) {
      throw new Error(`API request failed: ${endpoint}`)
    }
  }

  return { fetchApi, baseURL }
}
