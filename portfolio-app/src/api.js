// main.js или App.vue
import axios from 'axios';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();

// Интерцептор для добавления токена к каждому запросу
axios.interceptors.request.use((config) => {
  const token = userStore.user.access;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Интерцептор для обработки ошибок
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401) {
      // Если токен истек, попробуйте обновить его
      userStore.refreshToken();
    }
    return Promise.reject(error);
  }
);