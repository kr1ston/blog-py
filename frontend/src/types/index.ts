export * from './response'
export * from './user'

// 通用的请求参数类型
export interface QueryParams {
  page?: number
  size?: number
  sort?: string
  order?: 'asc' | 'desc'
  [key: string]: any
} 