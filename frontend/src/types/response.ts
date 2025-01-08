// 通用的 API 响应类型
export interface ApiResponse<T = any> {
  data: T
  message?: string
  status?: number
}

// 分页响应类型
export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  size: number
  pages: number
}

// Token 响应类型
export interface TokenResponse {
  token: string
} 