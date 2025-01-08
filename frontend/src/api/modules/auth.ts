import request from '@/utils/request'
import type { LoginParams, RegisterParams, TokenResponse, User } from '@/types'

export const authApi = {
  login(data: LoginParams) {
    return request.post<any, TokenResponse>('/auth/login', data)
  },

  register(data: RegisterParams) {
    return request.post<any, TokenResponse>('/auth/register', data)
  },

  getCurrentUser() {
    return request.get<any, User>('/users/me')
  },

  updateProfile(data: Partial<User>) {
    return request.put<any, User>('/users/me', data)
  },

  changePassword(oldPassword: string, newPassword: string) {
    return request.put<any, void>('/users/me/password', {
      old_password: oldPassword,
      password: newPassword
    })
  }
} 