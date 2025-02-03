<template>
    <div class="profile-layout">
        <div class="container pt-5 row mx-auto h-75 gap-4">
            <div class="sidebar col-4  w-25 p-3 mx-auto shadow-lg">
                <div class="container">
                    <img :src="user.get_avatar" alt="" class="avatar mb-3 img-fluid">
                    <h4 class="card-title mb-1">
                        {{ user.name || 'Имя пользователя' }}
                    </h4>
                    <p class="text-muted small">
                        <!-- {{ profile.profile_spec || 'Специальность' }} -->
                        Специальность не указана
                    </p>
                    <div class="tab-btns">
                        <button class="btn mb-2 d-block btn-warning w-100"
                            @click="setActiveTab('gallery')">Галлерея</button>
                        <button class="btn mb-2 d-block btn-warning w-100"
                            @click="setActiveTab('services')">Услуги</button>
                        <button class="btn d-block btn-warning w-100" @click="setActiveTab('about')">Обо
                            мне</button>
                    </div>
                    <div class="socials">
                        <!-- <a href=""><svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor"
                                class="bi bi-telegram" viewBox="0 0 16 16">
                                <path
                                    d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.287 5.906q-1.168.486-4.666 2.01-.567.225-.595.442c-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294q.39.01.868-.32 3.269-2.206 3.374-2.23c.05-.012.12-.026.166.016s.042.12.037.141c-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8 8 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629q.14.092.27.187c.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.4 1.4 0 0 0-.013-.315.34.34 0 0 0-.114-.217.53.53 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09" />
                            </svg></a> -->
                    </div>
                    <router-link to="/profile/edit" class="btn mb-2 d-block btn-warning w-100"
                        v-if="userStore.user.id === user.id">
                        Редактировать профиль
                    </router-link>
                </div>
            </div>
            <!-- <div class="col-1"></div> -->
            <div class="main-block p-3 col shadow-lg">
                <div class="container">
                    <div class="about-tab" v-if="activeTab === 'gallery'">
                        <h3 class="text-muted">Тут будут ваши работы</h3>
                    </div>
                    <div class="services-list" v-if="activeTab === 'services'">
                        <!-- добавление услуги кнопка -->
                        <router-link to="/add-service" v-if="userStore.user.id === user.id">
                            <div class="btn add-service-btn btn-warning w-100 mb-3">+ Добавить услугу</div>
                        </router-link>

                        <!-- список -->
                        <p v-if="services.lenght === 0">У вас нет услуг!</p>
                        <!-- услуга -->
                        <div class="card mb-3 service-card" v-for="service in services" :key="service.id">
                            <div class="row g-0 p-2">
                                <!-- Блок с фото -->
                                <div class="col-md-4">
                                    <div class="service-img">
                                        <!-- Выводим первое фото, если оно есть -->
                                        <img v-if="service.photos.length > 0" :src="service.photos[0].get_image"
                                            alt="фото услуги" class="img-fluid rounded-start">
                                    </div>
                                </div>
                                <!-- Блок с описанием -->
                                <div class="col-md-8">
                                    <div class="card-body">
                                        <h5 class="card-title">{{ service.title }}</h5>
                                        <p class="card-text">{{ service.descr }}</p>
                                        <p class="card-text d-flex align-items-end justify-content-between">
                                            <a class="btn btn-warning">{{ service.price }} р</a>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="about-tab" v-if="activeTab === 'about'">
                        <div class="about-text">
                            <!-- {{ profile.profile_bio || 'Информация о пользователе отсутствует.' }} -->
                        </div>
                        <div class="about-links">
                            <li class="list-group-item">
                                <span class="text-secondary">ВКонтакте:</span>
                                <a href class="primary-link">укпуцкпукпукп</a>
                            </li>
                            <li class="list-group-item">
                                <span class="text-secondary">ТГ:</span>
                                <a href class="primary-link">кпакупук</a>
                            </li>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }

    },
    mounted() {
        this.getMyServices()
    },
    data() {
        return {
            activeTab: 'services',
            services: [],
            user: {
            }
        };
    },

    methods: {
        setActiveTab(tab) {
            this.activeTab = tab;
        },
        getMyServices() {
            axios
                .get(`http://127.0.0.1:8000/api/services/profile/${this.$route.params.id}`)
                .then(response => {
                    console.log('data', response.data);

                    // Убедитесь, что данные находятся в response.data.data
                    this.services = response.data.services || [];
                    this.user = response.data.user || [];
                    console.log(this.services);
                })
                .catch(error => {
                    console.log('error', error);
                    this.error = 'Ошибка при загрузке данных';
                });
        }
    },

}
</script>

<style scoped>
.link-active {
    color: #ffc107;
    font-weight: bold;
}
</style>