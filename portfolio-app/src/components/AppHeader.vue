<template>
  <div class="container">
    <header
      class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
      <a href="/" class="d-flex align-items-center col-md-3 mb-2 mb-md-0 text-dark text-decoration-none">
        <h3>MASTERskaya</h3>
      </a>

      <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
        <li>
          <router-link to="/" class="nav-link px-2 link-dark">Главная</router-link>
        </li>
        <li>
          <router-link to="/search" class="nav-link px-2 link-dark">Поиск</router-link>
        </li>
        <li>
          <router-link to="/faq" class="nav-link px-2 link-dark">FAQs</router-link>
        </li>
      </ul>

      <div class="col-md-3 text-end ">
        <span v-if="userStore.user.isAuthenticated" class="d-flex align-items-center">
          <router-link :to="{ name: 'profile', params: { 'id': userStore.user.id } }"
            class="mx-2 btn btn-warning">Профиль {{
              userStore.user.name }}</router-link>
          <router-link to="/logout" class="btn btn-secondary mx-2">Выйти</router-link>
        </span>
        <span v-else>
          <router-link to="/login" class="btn btn-outline-warning me-2">Login</router-link>
          <router-link to="/register" class="btn btn-warning">Sign-up</router-link>
        </span>
      </div>
    </header>
  </div>
</template>

<script>
import { useUserStore } from '@/stores/user';
import { watchEffect } from 'vue';

export default {
  setup() {
    const userStore = useUserStore()
    
    watchEffect(() => {
      console.log("Authentication status:", userStore.user.isAuthenticated);
    });

    return {
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