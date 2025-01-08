import request from '@/utils/request'
import { USER_API } from '@/constants/api'
import type { User } from '@/types'

export const userApi = {
  getUsers(params?: { skip?: number; limit?: number }) {
    return request.get<any, User[]>(USER_API.LIST, { params })
  },

  getUser(id: number) {
    return request.get<any, User>(USER_API.DETAIL(id))
  },

  createUser(data: Omit<User, 'id'>) {
    return request.post<any, User>(USER_API.CREATE, data)
  },

  updateUser(id: number, data: Partial<User>) {
    return request.put<any, User>(USER_API.UPDATE(id), data)
  },

  deleteUser(id: number) {
    return request.delete(USER_API.DELETE(id))
  }
} 