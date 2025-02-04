<template>
  <div class="container">
    <header class="d-flex flex-wrap align-items-center justify-content-between py-3 mb-4 border-bottom">
      <!-- Логотип -->
      <router-link to="/" class="d-flex align-items-center text-dark text-decoration-none">
        <h3 class="m-0 fw-bold">MASTERskaya</h3>
      </router-link>

      <!-- Навигация -->
      <ul class="nav col-12 col-md-auto mb-2 mb-md-0 justify-content-center">
        <li class="nav-item">
          <router-link to="/" class="nav-link px-3 link-dark fw-medium">Главная</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/search" class="nav-link px-3 link-dark fw-medium">Поиск</router-link>
        </li>
      </ul>

      <!-- Кнопки авторизации/профиля -->
      <div class="col-md-3 text-end">
        <template v-if="userStore.user.isAuthenticated">
          <div class="d-flex align-items-center justify-content-end">
            <router-link :to="{ name: 'profile', params: { id: userStore.user.id } }"
              class="btn btn-warning me-2 d-flex align-items-center">
              <i class="bi bi-person-circle me-2"></i> <!-- Иконка профиля -->
              {{ userStore.user.name }}
            </router-link>
            <router-link to="/logout" class="btn btn-outline-secondary">
              <i class="bi bi-box-arrow-right"></i> <!-- Иконка выхода -->
            </router-link>
          </div>
        </template>
        <template v-else>
          <router-link to="/login" class="btn btn-outline-warning me-2">Войти</router-link>
          <router-link to="/register" class="btn btn-warning">Регистрация</router-link>
        </template>
      </div>
    </header>
  </div>
</template>

<script>
import { useUserStore } from '@/stores/user';
import { computed } from 'vue';
import 'bootstrap-icons/font/bootstrap-icons.css';

export default {
  setup() {
    const userStore = useUserStore()

    const isAuthenticated = computed(() => userStore.user.isAuthenticated);
    const user = computed(() => userStore.user);

    return {
      isAuthenticated,
      user,
      userStore
    }
  },

}
</script>

<style scoped>
.logout-button {
  background-color: transparent;
  border: none;
  color: #dc3545;
  cursor: pointer;
  margin-left: 10px;
}

.logout-button:hover {
  text-decoration: underline;
}
</style>