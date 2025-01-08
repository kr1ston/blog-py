<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Navigation -->
    <el-menu
      mode="horizontal"
      class="border-b"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between">
        <el-menu-item index="1">
          <h1 class="text-xl font-bold">Blog System</h1>
        </el-menu-item>
        <el-menu-item index="2">
          <el-dropdown trigger="click">
            <el-button>
              <el-icon class="mr-1"><User /></el-icon>
              {{ authStore.user?.username }}
              <el-icon class="ml-1"><ArrowDown /></el-icon>
            </el-button>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="logout">
                  <el-icon><SwitchButton /></el-icon>
                  Sign out
                </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </el-menu-item>
      </div>
    </el-menu>

    <!-- Main content -->
    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 py-6 sm:px-0">
        <el-card v-if="authStore.user" class="mb-6">
          <template #header>
            <div class="flex items-center">
              <el-avatar :size="32" class="mr-3">
                {{ authStore.user.username.charAt(0).toUpperCase() }}
              </el-avatar>
              <h2 class="text-xl font-bold">Welcome, {{ authStore.user.username }}!</h2>
            </div>
          </template>
          <el-descriptions :column="2" border>
            <el-descriptions-item label="Username">
              {{ authStore.user.username }}
            </el-descriptions-item>
            <el-descriptions-item label="Email">
              {{ authStore.user.email }}
            </el-descriptions-item>
          </el-descriptions>
        </el-card>
        <el-empty v-else description="Loading user information..." />
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { User, ArrowDown, SwitchButton } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

const router = useRouter()
const authStore = useAuthStore()

const logout = async () => {
  try {
    await authStore.logout()
    router.push({ name: 'login' })
    ElMessage.success('Logged out successfully')
  } catch (error) {
    console.error('Logout error:', error)
    ElMessage.error('An error occurred during logout')
  }
}
</script>

<style>
.el-menu {
  --el-menu-bg-color: white !important;
}
</style> 