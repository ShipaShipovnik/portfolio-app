<template>
    <div class="main-block register-page container shadow p-5">
        <h1 class="h1 text-center">Редактировать профиль</h1>
        <div class="register-form form text-center">
            <form v-on:submit.prevent="submitForm" class="d-flex flex-column w-50 mx-auto my-3">
                <div class="input-group mb-3">
                    <input type="file" class="form-control" id="inputGroupFile02" @change="handleFileUpload">
                    <label class="input-group-text" for="inputGroupFile02">Upload</label>
                </div>

                <label class="form-label mb-2">
                    Имя:
                    <input class="form-control" type="text" v-model="form.name" required />
                </label>

                <!-- <label class="form-label mb-2">
                    Специализация:
                    <input class="form-control" type="email" placeholder="на чем вы специализируетесь?" v-model="form.spec"  />
                </label> -->

                <label class="form-label mb-2">
                    Email:
                    <input class="form-control" type="email" v-model="form.email" required />
                </label>

                <template v-if="this.errors.length > 0">
                    <div class="mt-3 p-6">
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>
                </template>

                <button type="submit" class="btn btn-warning mt-3 ">Сохранить изменения</button>
            </form>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'


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
                email: this.userStore.user.email,
                name: this.userStore.user.name,
                avatar: null,
            },
            errors: [],
        }
    },
    methods: {
        handleFileUpload(event) {
            this.form.avatar = event.target.files[0];
        },
        async submitForm() {
            this.errors = [];

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing');
                console.log('Your e-mail is missing');
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing');
                console.log('Имя не заполнено');
            }

            if (this.errors.length === 0) {
                try {
                    await this.userStore.refreshTokenIfNeeded();

                    const response = await axios.post(
                        'http://127.0.0.1:8000/api/edit-profile/',
                        this.form,
                        {
                            headers: {
                                Authorization: `Bearer ${this.userStore.user.access}`,
                                "Content-Type": "multipart/form-data",
                            },
                        }
                    );

                    if (response.data.message === 'Информация обновлена') {
                        console.log('Success!');

                        // Обновляем данные в хранилище Pinia
                        this.userStore.setUserInfo({
                            id: this.userStore.user.id,
                            name: this.form.name,
                            email: this.form.email,
                        });

                        // Очищаем форму (если нужно)
                        this.form.email = this.userStore.user.email;
                        this.form.name = this.userStore.user.name;

                        this.$router.back()

                    } else {
                        console.error('Что-то пошло не так');
                    }
                } catch (error) {
                    console.log('error', error);
                    if (error.response && error.response.status === 401) {
                        // Токен истек, попробуйте обновить его
                        await this.userStore.refreshToken();
                        // Повторите запрос после обновления токена
                        await this.submitForm();
                    } else {
                        this.errors.push('Ошибка при обновлении профиля');
                    }
                }
            }
        },
    }
}
</script>

<style></style>