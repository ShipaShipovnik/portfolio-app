<template>
    <div class="main-page container fill">
        <h1>Поиск</h1>
        <div class="container pt-5 row mx-auto h-75 gap-4">
            <div class="row p-3 mx-auto shadow">
                <form class="input-group rounded" @submit.prevent="submitSearch">
                    <input type="search" class="form-control rounded" v-model="query" placeholder="Search"
                        aria-label="Search" aria-describedby="search-addon" />
                    <button class="input-group-text border-0 text-warning" id="search-addon">
                        Найти
                    </button>
                </form>
            </div>
            <div class="sidebar col-4 p-3 mx-auto shadow">
                <p class="text-muted">Фильтрация:</p>
                <label class="">Цена р. <input type="number" class="form-control"></label>
                <label for="">Категория</label><input type="text" class="form-control">
            </div>
            <div class="main-block p-3 col shadow">
                <p class="text-muted">Результат поиска:</p>
                <!-- услуги -->
                <p v-if="servicesResult.length === 0">Таких услуг не нашлось!</p>
                <div class="card mb-3 service-card" v-for="service in servicesResult" :key="service.id">
                    <div class="row g-0 p-2">
                        <div class="col">
                            <div class="service-img"><img src="" alt="фото услуги"></div>
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">{{ service.title }}</h5>
                                <p class="card-text">
                                    {{ service.descr }}
                                </p>
                                <p class="card-text d-flex align-items-end justify-content-between">
                                    <a class="btn btn-warning">{{ service.price }} р</a>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- <p class="text-muted">Вы еще ничего не искали):</p> -->
                <!-- Пользователи -->
                <p v-if="usersResult.length === 0">Таких пользователей не нашлось!</p>
                <div class="row py-3 flex-items-sm-center" v-for="user in usersResult" :key="user.id">
                    <div class="column border">
                        <img :src="user.get_avatar" alt="">
                        <router-link :to="{ name: 'profile', params: { 'id': user.id } }"> {{ user.name }}
                        </router-link>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            query: '',
            usersResult: [],
            servicesResult: [],
        }
    },
    methods: {
        submitSearch() {
            console.log('Поиск поиск посик', this.query)

            axios
                .post('http://127.0.0.1:8000/search/', {
                    query: this.query
                })
                .then(response => {
                    console.log('Response', response.data)

                    this.usersResult = response.data.users || [];
                    this.servicesResult = response.data.services || [];
                })
                .catch(error => {
                    console.error('error', error)
                })
        }
    }
}
</script>

<style scoped>
/* юзер карты */
</style>