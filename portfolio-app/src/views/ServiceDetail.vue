<template>
    <div class="container ">
        <div class="border p-3">
            <div class="row g-4">
                <div class="col">
                    <!-- Фото услуги -->
                    <div class="service-img">
                        <img v-if="service.photos && service.photos.length > 0" :src="service.photos[0].get_image"
                            alt="Фото услуги" class="img-fluid">
                    </div>
                </div>
                <div class="col-7 d-flex flex-column">
                    <!-- Заголовок и описание -->
                    <h5 class="card-title mb-3">{{ service.title }}</h5>
                    <p class="card-title mb-3 text-muted">Категория: {{ service.category.name }}</p>
                    <p class="card-text">{{ service.descr }}</p>

                    <!-- Цена и статус -->
                    <div class="d-flex flex-column justify-self-end w-100">
                        <span v-if="service.isActive" class="alert alert-success flex-grow-1">
                            Активна! Можно заказывать.
                        </span>
                        <span v-else class="alert alert-secondary text-bg-secondary">
                            Не активна. Автор не готов принять заказ.
                        </span>

                        <div class="btn btn-outline-warning mb-3">
                            {{ service.price }} руб.
                        </div>

                        <div v-if="userStore.user.id === user.id" class="btn-group " role="group" >
                            <button class="service-control-btns btn btn-danger mb-5 btn-sm" @click="deleteService(service)">
                                <i class="bi bi-trash">Удалить</i>
                            </button>
                            <router-link :to="{ name: 'service-edit', params: { id: service.id } }"
                                class="service-control-btns btn btn-success btn-sm ">
                                <i class="bi bi-pencil"> Редактировать</i>
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';

export default {
    data() {
        return {
            service: {
                title: '',
                descr: '',
                category: {},
                price: 0,
                isActive: false,
                photos: [],
                image: null
            },
            categories: [],
            user: {}
        };
    },
    setup() {
        const userStore = useUserStore();
        return {
            userStore
        };
    },
    mounted() {
        this.getServiceDetail();
        this.getCategories();
    },
    methods: {
        async deleteService(service) {
            try {
                const isConfirmed = confirm(`Вы уверены, что хотите удалить услугу "${service.title}"?`);
                if (!isConfirmed) {
                    return;
                }
                const response = await axios.delete(
                    `http://127.0.0.1:8000/api/services/delete-service/${service.id}/`
                );
                this.$router.push({ name: 'profile', params: { id: this.userStore.user.id } });
            } catch (error) {
                console.error('Error deleting service:', error);
                alert('Ошибка при удалении услуги');
            }
        },

        getServiceDetail() {
            axios
                .get(`http://127.0.0.1:8000/api/services/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data);

                    // Получаем данные из вложенного объекта "service"
                    this.service = response.data.service || {};
                    console.log(this.service);

                    // Получаем данные пользователя
                    this.user = response.data.user || {};
                    console.log('User data from service:', this.user);
                })
                .catch(error => {
                    console.log('error', error);
                    this.error = 'Ошибка при загрузке данных';
                });
        },

        getCategories() {
            axios
                .get('http://127.0.0.1:8000/api/categories/')
                .then(response => {
                    this.categories = response.data;
                })
                .catch(error => {
                    console.log('error', error);
                    this.error = 'Ошибка при загрузке категорий';
                });
        }
    }
};
</script>

<style scoped>
.service-control-btns{
    height: 30px;
}

</style>