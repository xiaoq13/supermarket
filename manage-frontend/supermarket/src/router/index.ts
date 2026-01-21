// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/pages/home/index.vue'
import GoodsView from '@/pages/goods/index.vue'
import UsersView from '@/pages/users/index.vue'

const routes = [
  {
    path: '/',
    redirect: '/home' // 默认跳转到 home
  },
  {
    path: '/home',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/goods',
    name: 'Goods',
    component: GoodsView
  },
  {
    path: '/users',
    name: 'Users',
    component: UsersView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router