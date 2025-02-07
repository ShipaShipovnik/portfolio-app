<template>
  <div class="row g-4 grid">
    <div v-for="service in services" :key="service.id" class="col">
      <div class="card ">
        <div class="card-body">
          <!-- Фото услуги -->
          <div class="service-img mb-3">
            <img v-if="service.photos.length > 0" :src="service.photos[0].get_image" alt="Фото услуги"
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
              <button class="btn btn-outline-danger btn-sm" @click="deleteService(service)">
                <i class="bi bi-trash"></i>
              </button>
              <router-link :to="{ name: 'service-detail', params: { id: service.id } }"
                class="btn btn-outline-warning btn-sm mx-2">

                <i class="bi bi-eye"></i> Подробнее
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

export default {
  data() {
    return {
      services: [],
      error: ''
    };
  },
  mounted() {
    this.getServices();
  },
  methods: {
    getServices() {
      axios
        .get('http://127.0.0.1:8000/api/services/')
        .then(response => {
          console.log('data', response.data);

          // Убедитесь, что данные находятся в response.data.data
          this.services = response.data.data || [];
          console.log(this.services);
        })
        .catch(error => {
          console.log('error', error);
          this.error = 'Ошибка при загрузке данных';
        });
    }
  }
};
</script>

<style scoped>
.service-card {
  border: 1px solid #ddd;
  border-radius: 8px;
}

.service-img img {
  width: 100%;
  height: auto;
  border-radius: 8px;
}
</style>