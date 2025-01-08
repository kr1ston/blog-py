// API 版本前缀
export const API_VERSION = ''

// 认证相关接口
export const AUTH_API = {
  LOGIN: `${API_VERSION}/auth/login`,
  REGISTER: `${API_VERSION}/auth/register`,
  CURRENT_USER: `${API_VERSION}/auth/me`
}

// 用户相关接口
export const USER_API = {
  LIST: `${API_VERSION}/users`,
  DETAIL: (id: number) => `${API_VERSION}/users/${id}`,
  CREATE: `${API_VERSION}/users`,
  UPDATE: (id: number) => `${API_VERSION}/users/${id}`,
  DELETE: (id: number) => `${API_VERSION}/users/${id}`,
}

// 其他 API 路径常量
export const API_ROUTES = {
  AUTH: AUTH_API,
  USER: USER_API
} 