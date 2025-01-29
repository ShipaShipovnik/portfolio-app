<template>
    <div class="main-block register-page container shadow p-5">
        <h1 class="h1 text-center">Регистрация</h1>
        <div class="register-form form text-center">
            <form v-on:submit.prevent="submitForm">
                <label class="form-label">
                    Имя:
                    <input class="form-control" type="text" v-model="form.name" required />
                </label>
                <br />
                <label class="form-label">
                    Email:
                    <input class="form-control" type="email" v-model="form.email" required />
                </label>
                <br />
                <label class="form-label">
                    Пароль:
                    <input class="form-control" type="password" v-model="form.password1" required />
                </label>
                <label class="form-label">
                    Поворите пароль:
                    <input class="form-control" type="password" v-model="form.password2" required />
                </label>
                <br />
                <br />

                <template v-if="this.errors.length > 0">
                    <div class="m-2 p-5">
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>
                </template>

                <button type="submit" class="btn btn-warning">Зарегистрироваться</button>
            </form>
            <p class="mt-4 text-muted">
                Уже есть аккаунт? <router-link to="/login" class="text-warning">Войти.</router-link>
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
            errors: [],
        }
    },

    methods: {
        submitForm() {
            console.log('Form submitted');
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
                console.log('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
                console.log('имя ьбоять')
            }

            if (this.form.password1 === '') {
                this.errors.push('паролоь')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('не совпадают')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/register/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            console.log('отправилось!')
                            this.toastStore.showToast(5000, 'Пользователь создан. Войдите.', 'bg-success text-white')
                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-warning')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
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