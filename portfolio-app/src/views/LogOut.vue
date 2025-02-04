<template>
  <div class="main-block register-page container shadow p-5">
    <div class="text-center">
      <!-- Иконка выхода -->
      <i class="bi bi-box-arrow-right display-1 text-warning mb-4"></i>

      <!-- Заголовок -->
      <h1 class="h1 mb-3">Выход</h1>

      <!-- Сообщение -->
      <p class="lead text-muted mb-4">Вы уверены, что хотите выйти?</p>

      <!-- Кнопки -->
      <div class="d-flex justify-content-center gap-3">
        <button @click="logout" class="btn btn-danger btn-lg">
          <i class="bi bi-box-arrow-right me-2"></i> Выйти
        </button>
        <router-link to="/" class="btn btn-outline-secondary btn-lg">
          <i class="bi bi-x-circle me-2"></i> Нет
        </router-link>
      </div>
    </div>
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

<style scoped>
.register-page {
  max-width: 600px;
  margin: 5rem auto;
  padding: 2rem;
  border-radius: 12px;
  background-color: #fff;
}

.display-1 {
  font-size: 4rem;
}

.lead {
  font-size: 1.25rem;
}

.btn-lg {
  padding: 0.5rem 1.5rem;
  font-size: 1.1rem;
}

.btn-danger {
  background-color: #dc3545;
  border-color: #dc3545;
}

.btn-danger:hover {
  background-color: #c82333;
  border-color: #bd2130;
}

.btn-outline-secondary {
  border-color: #6c757d;
  color: #6c757d;
}

.btn-outline-secondary:hover {
  background-color: #6c757d;
  color: #fff;
}
</style>