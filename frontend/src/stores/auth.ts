import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '@/api/auth'
import type { User, LoginParams, RegisterParams } from '@/types'

export const useAuthStore = defineStore('auth', () => {
  const token = ref<string | null>(localStorage.getItem('token'))
  const user = ref<User | null>(null)

  const isAuthenticated = computed(() => !!token.value)

  async function login(credentials: LoginParams) {
    try {
      const response = await authApi.login(credentials)
      token.value = response.token
      localStorage.setItem('token', response.token)
      await fetchUser()
      return true
    } catch (error) {
      return false
    }
  }

  async function register(data: RegisterParams) {
    try {
      const response = await authApi.register(data)
      token.value = response.token
      localStorage.setItem('token', response.token)
      await fetchUser()
      return true
    } catch (error) {
      return false
    }
  }

  async function logout() {
    token.value = null
    user.value = null
    localStorage.removeItem('token')
  }

  async function fetchUser() {
    if (!token.value) return

    try {
      user.value = await authApi.getCurrentUser()
    } catch (error) {
      logout()
    }
  }

  async function updateProfile(data: Partial<User>) {
    try {
      user.value = await authApi.updateProfile(data)
      return true
    } catch (error) {
      return false
    }
  }

  async function changePassword(oldPassword: string, newPassword: string) {
    try {
      await authApi.changePassword(oldPassword, newPassword)
      return true
    } catch (error) {
      return false
    }
  }

  // Initialize user if token exists
  if (token.value) {
    fetchUser()
  }

  return {
    user,
    token,
    isAuthenticated,
    login,
    register,
    logout,
    fetchUser,
    updateProfile,
    changePassword
  }
}) 