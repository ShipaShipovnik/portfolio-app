<template>
    <div class="profile-layout">
        <div class="container pt-5">
            <div class="row g-4">
                <!-- Сайдбар -->
                <div class="col-md-4">
                    <div class="card shadow-lg">
                        <div class="card-body text-center">
                            <!-- Аватар -->
                            <img :src="user.get_avatar" alt="Аватар" class="avatar img-fluid rounded-circle mb-3"
                                style="width: 150px; height: 150px; object-fit: cover;">

                            <!-- Имя пользователя -->
                            <h4 class="card-title mb-2">
                                {{ user.name || 'Имя пользователя' }}
                            </h4>

                            <!-- Специальность -->
                            <!-- <p class="text-muted small mb-4">
                                {{ profile.profile_spec || 'Специальность не указана' }}
                            </p> -->

                            <!-- Кнопки табов -->
                            <div class="d-grid gap-2">
                                <button class="btn btn-outline-warning text-start d-flex align-items-center"
                                    @click="setActiveTab('gallery')">
                                    <i class="bi bi-images me-2"></i> Галерея
                                </button>
                                <button class="btn btn-outline-warning text-start d-flex align-items-center"
                                    @click="setActiveTab('services')">
                                    <i class="bi bi-briefcase me-2"></i> Услуги
                                </button>
                                <button class="btn btn-outline-warning text-start d-flex align-items-center"
                                    @click="setActiveTab('about')">
                                    <i class="bi bi-person-lines-fill me-2"></i> Обо мне
                                </button>
                            </div>

                            <!-- Социальные сети -->
                            <div class="socials mt-4">
                                <a href="#" class="text-decoration-none text-secondary me-3">
                                    <i class="bi bi-telegram fs-5"></i>
                                </a>
                                <a href="#" class="text-decoration-none text-secondary">
                                    <i class="bi bi-vk fs-5"></i>
                                </a>
                            </div>

                            <!-- Кнопка редактирования -->
                            <router-link v-if="userStore.user.id === user.id" to="/profile/edit"
                                class="btn btn-warning w-100 mt-4">
                                <i class="bi bi-pencil-square me-2"></i> Редактировать профиль
                            </router-link>
                        </div>
                    </div>
                </div>

                <!-- Основной блок -->
                <div class="col-md-8">
                    <div class="card shadow-lg">
                        <div class="card-body">
                            <!-- Галерея -->
                            <div v-if="activeTab === 'gallery'" class="about-tab">
                                <h3 class="text-muted">Тут будут ваши работы</h3>
                            </div>

                            <!-- Услуги -->
                            <div v-if="activeTab === 'services'" class="services-list">
                                <!-- Кнопка добавления услуги -->
                                <router-link v-if="userStore.user.id === user.id" to="/add-service"
                                    class="btn btn-warning w-100 mb-4 d-flex align-items-center justify-content-center">
                                    <i class="bi bi-plus-lg me-2"></i> Добавить услугу
                                </router-link>

                                <!-- Список услуг -->
                                <p v-if="services.length === 0" class="text-muted text-center">У вас нет услуг!</p>

                                <div class="row g-4">
                                    <div v-for="service in services" :key="service.id" class="col-md-6">
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
                            </div>

                            <!-- Обо мне -->
                            <div v-if="activeTab === 'about'" class="about-tab">
                                <div class="about-text mb-4">
                                    <p class="text-muted">
                                        О вас
                                    </p>
                                </div>

                                <div class="about-links">
                                    <ul class="list-group">
                                        <li class="list-group-item d-flex justify-content-between align-items-center">
                                            <span class="text-secondary">ВКонтакте:</span>
                                            <a href="#" class="text-decoration-none">ссылка</a>
                                        </li>
                                        <li class="list-group-item d-flex justify-content-between align-items-center">
                                            <span class="text-secondary">Телеграм:</span>
                                            <a href="#" class="text-decoration-none">ссылка</a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
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

        async deleteService(service) {
            try {
                const isConfirmed = confirm(`Вы уверены, что хотите удалить услугу "${service.title}"?`);

                // Если пользователь нажал "Отмена", прерываем выполнение
                if (!isConfirmed) {
                    return;
                }

                console.log('Deleting service:', service);

                // Отправляем запрос на удаление
                const response = await axios.delete(
                    `http://127.0.0.1:8000/api/services/delete-service/${service.id}/`,
                );

                console.log('Service deleted:', response.data);

                this.$router.push('/')

                this.services = this.services.filter(s => s.id !== service.id);
            } catch (error) {
                console.error('Error deleting service:', error);
                alert('Ошибка при удалении услуги');
            }
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
.profile-layout {
    background-color: #f8f9fa;
    min-height: 100vh;
}

.avatar {
    border: 3px solid #ffc107;
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

.service-img img {
    height: 200px;
    width: 100%;
    object-fit: cover;
}

.list-group-item {
    border: none;
    background-color: transparent;
}
</style>