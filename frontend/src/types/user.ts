// 用户基本信息
export interface User {
  id: number
  username: string
  email: string
  created_at?: string
  updated_at?: string
}

// 登录参数
export interface LoginParams {
  username: string
  password: string
}

// 注册参数
export interface RegisterParams {
  username: string
  email: string
  password: string
}

// 用户更新参数
export interface UpdateUserParams {
  email?: string
  password?: string
  old_password?: string
} 