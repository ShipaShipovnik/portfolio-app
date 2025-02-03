<template>
  <div>
    <div class="card mb-3 service-card" v-for="service in services" :key="service.id">
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
              <!-- <small class="text-muted align-middle">Срок {{ service.workTime || 'Не указано' }}</small> -->
              <a class="btn btn-warning">{{ service.price }} р</a>
            </p>
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