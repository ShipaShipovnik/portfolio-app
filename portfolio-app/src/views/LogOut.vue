<template>
  <div>
    <p>Вы уверены, что хотите выйти?</p>
    <button @click="logout">Выйти</button>
    <router-link class="text-muted" to="/">Нет</router-link>
  </div>
</template>

<script>
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router'; // Импортируем useRouter

export default {
  setup() {
    const userStore = useUserStore();
    const router = useRouter(); // Получаем router

    const logout = () => {
      userStore.logout();
      router.push('/login'); // Используем router для навигации
    };

    return {
      logout,
    };
  },
};
</script>