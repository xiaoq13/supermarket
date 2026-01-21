<!-- src/App.vue -->
<template>
  <div class="app">
    <!-- 左侧菜单栏 -->
    <aside class="sidebar">
      <nav>
        <router-link to="/home" class="menu-item">首页</router-link>
        <router-link to="/goods" class="menu-item">商品管理</router-link>
        <router-link to="/users" class="menu-item">用户管理</router-link>
      </nav>
    </aside>

    <!-- 右侧内容区 -->
    <main class="content">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
// 可以在这里添加全局逻辑（如权限、主题等）
</script>

<style scoped>
.app {
  display: flex;
  min-height: calc(100vh - 24px);
  background-color: #f5f5f5;
  width: calc(100vw - 24px);
}

/* 左侧导航栏样式 */
.sidebar {
  width: 200px;
  height: 100%;
  background-color: #f5f7fa;
  /* 浅灰蓝背景 */
  border-right: 1px solid #e6e6e6;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
}

.sidebar-menu {
  list-style: none;
  padding: 0;
  margin: 0;
  flex: 1;
}

.sidebar-menu li {
  padding: 12px 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  border-left: 3px solid transparent;
}

.sidebar-menu li:hover {
  background-color: #e6f4ff;
  color: #1a73e8;
  border-left-color: #1a73e8;
}

.sidebar-menu li.active {
  background-color: #1a73e8;
  color: white;
  border-left-color: #1a73e8;
}

.sidebar-menu li a {
  text-decoration: none;
  color: #333;
  font-size: 14px;
  font-weight: 500;
  display: block;
  padding: 0;
}

.sidebar-menu li a:hover {
  color: #1a73e8;
}

.menu-item {
  display: block;
  padding: 12px 20px;
  text-decoration: none;
  color: #333;
  font-size: 14px;
  transition: all 0.3s ease;
  border-radius: 4px;
  margin-bottom: 8px;
}

.menu-item:hover {
  background-color: #e6f7ff;
  color: #007acc;
}

.menu-item.router-link-active {
  background-color: #007acc;
  color: white;
}

.content {
  flex: 1;
  /* 占据剩余空间 */
  background-color: lightgrey;
  padding: 6px;
  overflow: auto;
}
</style>