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

                        <button type="button" class="btn btn-warning">
                            {{ service.price }} руб.
                        </button>

                        <button class="btn btn-outline-danger btn-sm" @click="deleteService(service)"
                            v-if="userStore.user.id === user.id">
                            <i class="bi bi-trash"> Удалить</i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user'

export default {
    data() {
        return {
            service: {
                category:{}
            },
            user: {
            }
        }
    },
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }

    },
    mounted() {
        this.getServiceDetail()
    },
    methods: {
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

                // this.services = this.services.filter(s => s.id !== service.id);
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
                })
                .catch(error => {
                    console.log('error', error);
                    this.error = 'Ошибка при загрузке данных';
                });
        }
    }
}
</script>

<style scoped>
/* .service-img img {
    height: 200px;
    width: 100%;
    object-fit: cover;
} */
</style>