import request from '@/utils/request'
import { AUTH_API } from '@/constants/api'
import type { LoginParams, RegisterParams, TokenResponse, User } from '@/types'

export const authApi = {
  login(data: LoginParams) {
    // 转换为 FormData 格式，因为后端使用 OAuth2PasswordRequestForm
    const formData = new FormData()
    formData.append('username', data.username)
    formData.append('password', data.password)
    
    return request.post<any, TokenResponse>(AUTH_API.LOGIN, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  },

  register(data: RegisterParams) {
    return request.post<any, TokenResponse>(AUTH_API.REGISTER, data)
  },

  getCurrentUser() {
    return request.get<any, User>(AUTH_API.CURRENT_USER)
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