<template>
    <div class="main-block register-page container shadow p-5">
        <h1 class="h1 text-center">Авторизация</h1>
        <div class="login-form text-center">
            <form @submit.prevent="submitForm">
                <div class="mb-3">
                    <label for="email" class="form-label">Email:</label>
                    <input id="email" class="form-control" type="email" v-model="form.email"
                        placeholder="Введите ваш email" required />
                </div>

                <!-- Поле для пароля -->
                <div class="mb-3">
                    <label for="password1" class="form-label">Пароль:</label>
                    <input id="password1" class="form-control" type="password" v-model="form.password"
                        placeholder="Введите пароль" required />
                </div>

                <!-- Блок для вывода ошибок -->
                <template v-if="errors.length > 0">
                    <div class="alert alert-danger">
                        <p class="m-0" v-for="error in errors" :key="error">{{ error }}</p>
                    </div>
                </template>

                <button type="submit" class="btn btn-warning ">Войти</button>
            </form>
            <p class="text-muted" mt-4>
                Нет аккаунта? <router-link to="/register" class="text-warning">Регистрация.</router-link>
            </p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                password: ''
            },
            errors: []

        }
    },

    methods: {
        async submitForm() {
            this.errors = [];

            // Валидация полей
            if (this.form.email === '') {
                this.errors.push('Введите почту!');
            }

            if (this.form.password === '') {
                this.errors.push('Введите пароль!');
            }

            if (this.errors.length === 0) {
                try {
                    // Авторизация (получение токена)
                    const loginResponse = await axios.post('/login/', this.form);
                    this.userStore.setToken(loginResponse.data);

                    axios.defaults.headers.common["Authorization"] = "Bearer " + loginResponse.data.access;

                    //Получение информации о пользователе
                    const userResponse = await axios.get('/me/');
                    this.userStore.setUserInfo(userResponse.data);

                    this.errors = [];
                    
                    // Перенаправление на главную страницу  
                    this.$router.push('/');
                } catch (error) {
                    console.log('error', error);

                    // Обработка ошибок
                    if (error.response) {
                        if (error.response.status === 401) {
                            this.errors.push('Неправильная почта или пароль');
                        } else {
                            this.errors.push('Что то пошло не так. Пожалуйста повторите попытку.');
                        }
                    } else {
                        this.errors.push('Ошибка сети. Проверьте соединение.');
                    }
                }
            }
        },
    }
}
</script>

<style scoped>
.login-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
</style>