<template>
    <div class="main-block register-page container shadow p-5">
        <h1 class="h1 text-center">Авторизация</h1>
        <div class="login-form text-center">
            <form @submit.prevent="submitForm">
                <label class="form-label">
                    Email:
                    <input class="form-control" type="email" v-model="form.email" required />
                </label>
                <br />
                <label class="form-label">
                    Пароль:
                    <input class="form-control" type="password" v-model="form.password" required />
                </label>
                <br />
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
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.password === '') {
                this.errors.push('Your password is missing')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/login/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)

                        console.log(response.data.access)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
                
                await axios
                    .get('/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data)

                        this.$router.push('/')
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
.login-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
</style>