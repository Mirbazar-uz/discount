export function useApi() {
  const config = useRuntimeConfig()

  const baseURL = import.meta.server
    ? (config.apiBaseServer as string)
    : (config.public.apiBase as string)

  async function fetchApi<T>(endpoint: string, params?: Record<string, string>): Promise<T> {
    const path = endpoint.startsWith('/') ? endpoint : `/${endpoint}`
    let url = `${baseURL}${path}`

    if (params) {
      const searchParams = new URLSearchParams()

      Object.entries(params).forEach(([key, value]) => {
        if (value) {
          searchParams.set(key, value)
        }
      })

      const qs = searchParams.toString()

      if (qs) {
        url += `?${qs}`
      }
    }

    try {
      const response = await $fetch<T>(url)
      return response
    } catch (error) {
      throw new Error(`API request failed: ${endpoint}`)
    }
  }

  return { fetchApi, baseURL }
}
