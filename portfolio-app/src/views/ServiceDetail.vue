<template>
    <div class="col-md-6">
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
                    <button class="btn btn-outline-warning btn-sm">
                        <i class="bi bi-eye"></i> Подробнее
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
</style>