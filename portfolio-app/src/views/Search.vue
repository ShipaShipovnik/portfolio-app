<template>
    <div class="main-page container fill">
        <h1 class="text-center my-4">Поиск</h1>

        <!-- Поисковая строка -->
        <div class="row justify-content-center mb-4">
            <div class="col-md-8">
                <form class="input-group shadow-sm" @submit.prevent="submitSearch">
                    <input type="search" class="form-control rounded-start" v-model="query"
                        placeholder="Введите название услуги или имя пользователя...." aria-label="Search" />
                    <button class="btn btn-warning rounded-end" type="submit">
                        <i class="bi bi-search"></i> Найти
                    </button>
                </form>
            </div>
        </div>

        <!-- Основной контент -->
        <div class="row g-4">
            <div class="col-md-3">
                <div class="card shadow-sm">


                    <div class="card-body">
                        <h5 class="card-title text-muted mb-4">Фильтры</h5>

                        <div class="alert alert-warning" role="alert">
                            Все еще в разработке ;)
                        </div>

                        <!-- 
                        <div class="mb-3">
                            <label for="price" class="form-label">Цена, ₽</label>
                            <input type="number" class="form-control" id="price" placeholder="Цена">
                        </div>

                        <div class="mb-3">
                            <label for="category" class="form-label">Категория</label>
                            <select class="form-select" id="category">
                                <option value="">Все категории</option>
                                <option v-for="category in categories" :key="category.id" :value="category.id">
                                    {{ category.name }}
                                </option>
                            </select>
                        </div>

                        <button class="btn btn-outline-secondary w-100" @click="resetFilters">
                            <i class="bi bi-arrow-counterclockwise"></i> Сбросить
                        </button> -->   
                    </div>
                    </div>
                </div>


                <!-- Результаты поиска -->
                <div class="col-md-9">
                    <div class="card shadow-sm">
                        <div class="card-body">
                            <!-- Пок ничего не ввели. -->
                            <template v-if="query.length === 0">
                                <h5 class="card-title text-muted mb-4">Все услуги</h5>
                                <ServicesList />
                            </template>
                            <!-- Начали вводить. -->
                            <template v-else>
                                <h5 class="card-title text-muted mb-4">Результаты поиска</h5>

                                <!-- Услуги -->
                                <div v-if="servicesResult.length > 0">
                                    <h6 class="text-muted mb-3">Услуги</h6>
                                    <div v-for="service in servicesResult" :key="service.id" class="col-md-6">
                                        <div class="card ">
                                            <div class="card-body">
                                                <!-- Фото услуги -->
                                                <div class="service-img mb-3">
                                                    <img v-if="service.photos.length > 0"
                                                        :src="service.photos[0].get_image" alt="Фото услуги"
                                                        class="img-fluid rounded">
                                                </div>

                                                <!-- Заголовок и описание -->
                                                <h5 class="card-title">{{ service.title }}</h5>
                                                <p class="card-text">{{ service.descr }}</p>

                                                <!-- Цена -->
                                                <div class="d-flex justify-content-between align-items-center">
                                                    <span class="text-warning fw-bold">{{ service.price }} р</span>
                                                    <div class="d-flex justify-content-between align-items-center">
                                                    </div>
                                                    <div>
                                                        <button class="btn btn-outline-danger btn-sm"
                                                            @click="deleteService(service)">
                                                            <i class="bi bi-trash"></i>
                                                        </button>
                                                        <router-link
                                                            :to="{ name: 'service-detail', params: { id: service.id } }"
                                                            class="btn btn-outline-warning btn-sm mx-2">

                                                            <i class="bi bi-eye"></i> Подробнее
                                                        </router-link>
                                                    </div>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Пользователи -->
                                <div v-if="usersResult.length > 0" class="mt-4">
                                    <h6 class="text-muted mb-3">Пользователи</h6>
                                    <div class="row g-4">
                                        <div v-for="user in usersResult" :key="user.id" class="col-md-6">
                                            <div class="card h-100">
                                                <div class="card-body d-flex align-items-center">
                                                    <!-- Аватар -->
                                                    <img :src="user.get_avatar" alt="Аватар" class="rounded-circle me-3"
                                                        style="width: 50px; height: 50px; object-fit: cover;">
                                                    <!-- Имя и ссылка -->
                                                    <div>
                                                        <router-link :to="{ name: 'profile', params: { id: user.id } }"
                                                            class="text-decoration-none text-dark fw-bold">
                                                            {{ user.name }}
                                                        </router-link>
                                                        <p class="text-muted small mb-0">Мастер</p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- Сообщение, если ничего не найдено -->
                                <div v-if="servicesResult.length === 0 && usersResult.length === 0"
                                    class="text-center py-5">
                                    <i class="bi bi-search display-4 text-muted mb-3"></i>
                                    <p class="text-muted">Ничего не найдено</p>
                                </div>


                            </template>


                        </div>
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
import ServicesList from '@/components/ServicesList.vue';
import axios from 'axios'

export default {
    data() {
        return {
            query: '',
            usersResult: [],
            servicesResult: [],
            services: [],
            categories: [],
        }
    },
    components: {
        ServicesList
    },
    created() {
        this.getCategories();
    },
    methods: {
        getCategories() {
            axios
                .get('http://127.0.0.1:8000/api/services/categories')
                .then(response => {
                    console.log('data', response.data);
                    this.categories = response.data.data || [];
                    console.log(this.categories);
                })
                .catch(error => {
                    console.log('error', error);
                    this.error = 'Ошибка при загрузке данных';
                });
        },
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
.main-page {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.service-img img {
    height: 200px;
    width: 100%;
    object-fit: cover;
}

.card {
    border: none;
    border-radius: 12px;
}

.btn-outline-warning {
    transition: all 0.3s ease;
}

.btn-outline-warning:hover {
    background-color: #ffc107;
    color: #000;
}

.rounded-circle {
    border: 2px solid #ffc107;
}
</style>