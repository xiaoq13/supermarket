// src/api/index.js
import { createApp } from 'vue'
import axios from 'axios'

// 创建 axios 实例
const api = axios.create({
  baseURL: '/api', // 所有请求都会自动加上 /api 前缀
  timeout: 10000,
})

// 请求拦截器（可选）
api.interceptors.request.use(config => {
  // 可以添加 token
  const token = localStorage.getItem('token')
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`
  }
  return config
})

api.interceptors.response.use((response)=>{
    return response.data
},(err)=>{
    return Promise.reject(err)
})

export default api