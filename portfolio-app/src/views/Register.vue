html
Copy
<template>
    <div class="main-block register-page container shadow p-5 rounded">
        <h1 class="h1 text-center mb-4">Регистрация</h1>
        <div class="register-form form">
            <form @submit.prevent="submitForm" class="needs-validation" novalidate>
                <!-- Поле для имени -->
                <div class="mb-3">
                    <label for="name" class="form-label">Имя:</label>
                    <input id="name" class="form-control" type="text" v-model="form.name" placeholder="Введите ваше имя"
                        required />
                </div>

                <!-- Поле для email -->
                <div class="mb-3">
                    <label for="email" class="form-label">Email:</label>
                    <input id="email" class="form-control" type="email" v-model="form.email"
                        placeholder="Введите ваш email" required />
                </div>

                <!-- Поле для пароля -->
                <div class="mb-3">
                    <label for="password1" class="form-label">Пароль:</label>
                    <input id="password1" class="form-control" type="password" v-model="form.password1"
                        placeholder="Введите пароль" required />
                </div>

                <!-- Поле для подтверждения пароля -->
                <div class="mb-4">
                    <label for="password2" class="form-label">Повторите пароль:</label>
                    <input id="password2" class="form-control" type="password" v-model="form.password2"
                        placeholder="Повторите пароль" required />
                </div>

                <!-- Блок для вывода ошибок -->
                <div v-if="successMessage.length > 0" class="alert alert-success" role="alert">
                    {{ successMessage }}
                </div>
                <template v-if="errors.length > 0">
                    <div class="alert alert-danger">
                        <p class="m-0" v-for="error in errors" :key="error">{{ error }}</p>
                    </div>
                </template>

                <!-- Кнопка отправки формы -->
                <div class="d-grid">
                    <button type="submit" class="btn btn-warning btn-lg mt-3">
                        Зарегистрироваться
                    </button>
                </div>
            </form>

            <!-- Ссылка на страницу входа -->
            <p class="mt-4 text-center text-muted">
                Уже есть аккаунт? <router-link to="/login" class="text-warning">Войти</router-link>
            </p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            successMessage: '',
            errors: [],
        }
    },

    methods: {
        submitForm() {
            console.log('Отправка формы...');
            this.errors = []

            // Валидация
            if (this.form.email === '') {
                this.errors.push('Введите почту!')

                console.log('Не введена почта!')
            }

            if (this.form.name === '') {
                this.errors.push('Введите имя!')

                console.log('Не введено имя!')
            }

            if (this.form.password1 === '') {
                this.errors.push('Не введен пароль!')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('Пароли не совпадают!')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/register/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            console.log('Отправилось на сервер!')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''

                            this.successMessage = 'Регистрация прошла успешно. Перейдите на страницу входа.'
                        } else {
                            this.errors.push('Что-то пошло не так. Обновите страницу и попробуйте снова.')
                        }
                    })
                    .catch(error => {
                        if (error.response && error.response.data.errors) {
                            //ошибки валидации с сервера
                            const serverErrors = error.response.data.errors;
                            for (let field in serverErrors) {
                                this.errors.push(serverErrors[field]);
                            }
                        } else {
                            this.errors.push('Что-то пошло не так. Обновите страницу и попробуйте снова.');
                        }
                        console.log('error', error);
                    });
            }
        }
    }
}
</script>

<style scoped>
.register-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
</style>