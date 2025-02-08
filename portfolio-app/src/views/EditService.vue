<template>
  <div class="container">
    <div class="border p-3">
      <form @submit.prevent="updateService">
        <div class="row g-4">
          <div class="col">
            <!-- Фото услуги -->
            <div class="service-img">
              <img v-if="service.photos && service.photos.length > 0" :src="service.photos[0].get_image"
                alt="Фото услуги" class="img-fluid">
              <input type="file" @change="handleFileUpload" class="form-control mt-2">
            </div>
          </div>
          <div class="col-7 d-flex flex-column">
            <!-- Заголовок и описание -->
            <div class="mb-3">
              <label for="title" class="form-label">Заголовок</label>
              <input type="text" id="title" v-model="service.title" class="form-control" required>
            </div>
            <div class="mb-3">
              <label for="category" class="form-label">Категория</label>
              <select id="category" v-model="service.category.id" class="form-select" required>
                <option v-for="category in categories" :key="category.id" :value="category.id">
                  {{ category.name }}
                </option>
              </select>
            </div>
            <div class="mb-3">
              <label for="description" class="form-label">Описание</label>
              <textarea id="description" v-model="service.descr" class="form-control" required></textarea>
            </div>

            <!-- Цена и статус -->
            <div class="d-flex flex-column justify-self-end w-100">
              <div class="mb-3">
                <label for="price" class="form-label">Цена</label>
                <input type="number" id="price" v-model="service.price" class="form-control" required>
              </div>
              <div class="mb-3 form-check">
                <input type="checkbox" id="isActive" v-model="service.isActive" class="form-check-input">
                <label for="isActive" class="form-check-label">Активна</label>
              </div>

              <button type="submit" class="btn btn-primary mb-3">Сохранить изменения</button>

              <template v-if="userStore.user.id === user.id">
                <button class="btn btn-danger mb-5" @click="deleteService(service)">
                  <i class="bi bi-trash"> Удалить</i>
                </button>
              </template>
            </div>
          </div>
        </div>
      </form>
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
        this.$router.push('/');
      } catch (error) {
        console.error('Error deleting service:', error);
        alert('Ошибка при удалении услуги');
      }
    },

    getServiceDetail() {
      axios
        .get(`http://127.0.0.1:8000/api/services/${this.$route.params.id}/`)
        .then(response => {
          this.service = response.data.service || {};
        })
        .catch(error => {
          console.log('error', error);
          this.error = 'Ошибка при загрузке данных';
        });
    },

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

    handleFileUpload(event) {
      this.service.image = event.target.files[0];
      console.log("Теперь фотка ",this.service.image)
    },

    async updateService() {
      try {
        const formData = new FormData();
        formData.append('title', this.service.title);
        formData.append('descr', this.service.descr);
        formData.append('category', this.service.category.id);
        formData.append('price', this.service.price);
        formData.append('isActive', this.service.isActive);
        if (this.service.image) {
          formData.append('image', this.service.image);
        }

        const response = await axios.post(
          `http://127.0.0.1:8000/api/services/edit-service/${this.$route.params.id}/`,
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        );

        alert('Информация об услуге обновлена');
        this.$router.push('/');
      } catch (error) {
        console.error('Error updating service:', error);
        alert('Ошибка при обновлении услуги');
      }
    }
  }
};
</script>

<style scoped></style>