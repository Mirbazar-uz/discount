export function useAuth() {
  const token = useCookie('admin_token', {
    maxAge: 60 * 60 * 24,
    path: '/',
    sameSite: 'lax',
  })

  const isAuthenticated = computed(() => !!token.value)

  async function login(password: string): Promise<boolean> {
    const config = useRuntimeConfig()
    const baseURL = import.meta.server
      ? (config.apiBaseServer as string)
      : (config.public.apiBase as string)

    try {
      const response = await $fetch<{ access_token: string }>(`${baseURL}/admin/login`, {
        method: 'POST',
        body: { password },
      })
      token.value = response.access_token
      return true
    } catch {
      return false
    }
  }

  function logout() {
    token.value = null
    navigateTo('/admin/login')
  }

  function getToken(): string | null {
    return token.value || null
  }

  return {
    token,
    isAuthenticated,
    login,
    logout,
    getToken,
  }
}
