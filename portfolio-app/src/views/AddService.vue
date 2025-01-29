<template>
    <div class="main-page container shadow p-5">
        <div class="addService-window">
            <form ref="addServiceForm" @submit.prevent="onSubmit">
                <h3>Заполните информацию об услуге</h3>
                <hr>
                <br>

                <div class="input-block">
                    <label>Название услуги</label>
                    <input type="text" class="form-control" v-model="form.serviceName"
                        placeholder="Какую услугу вы предоставляете?">
                </div>

                <div class="input-block">
                    <label>*Описание</label>
                    <textarea v-model="form.serviceDescrpt" placeholder="Опишите предоставляемую услугу."></textarea>
                </div>

                <div class="input-block">
                    <label>Цена(руб):</label>
                    <span>*Мин. цена<input type="number" class="form-control" placeholder="0"
                            v-model.number="form.serviceMinPrice"> - Макс. цена <input type="number"
                            class="form-control" placeholder="0" v-model.number="form.serviceMaxPrice"></span>
                </div>

                <div class="input-block">
                    <label for="">Кол-во свободных слотов:</label>
                    <input type="number" class="input-short" v-model.number="form.serviceAmount" />
                </div>

                <div class="input-block">
                    <label>Срок выполнения:</label>
                    <input type="text" class="form-control" placeholder="Напр. от 2 недель до 1 месяца"
                        v-model="form.serviceWorkTime">
                </div>

                <div class="input-block">
                    <label for="">Категория:</label>
                    <v-select v-model="form.serviceCategory" :options="catgList" label="name"
                        :reduce="category => category.id" placeholder="Выберите категорию"></v-select>
                </div>

                <!-- <div class="input-block">
                    <label for="">*Фото услуги:</label>
                    <div class="input-block">
                        <div class="dropzone" :class="{ 'active-dropzone': activeDrop }"
                            @dragenter.prevent="toggleActive" @dragleave.prevent="toggleActive" @dragover.prevent
                            @drop.prevent="toggleActive">
                            <span>Перетащите или дропните файл</span>
                            <span>ИЛИ</span>
                            <label for="dropzoneFile">Выбрать файлы</label>
                            <input type="file" id="dropzoneFile" accept=".png, .jpg, .jpeg"
                                @change="handleFileUpload" />
                            <span v-if="form.files">
                                Выбрано фото: {{ form.files }}
                            </span>
                            <span v-else> Фото не выбраны </span>
                        </div>
                        <div class="input-errors">
                            <div class="error-msg"></div>
                        </div>
                    </div>
                </div> -->

                <div class="input-block">
                    <label>Активна сейчас?:</label>
                    <input type="checkbox" v-model="form.serviceActive">
                </div>

                <button type="submit" class="btn btn-primary">Создать услугу</button>
            </form>
        </div>
    </div>
</template>

<script>
import api from '@/api';
import vSelect from 'vue-select';
import 'vue-select/dist/vue-select.css';

export default {
    components: {
        vSelect,
    },
    data() {
        return {
            form: {
                serviceName: "",
                serviceDescrpt: "",
                serviceMinPrice: 0,
                serviceMaxPrice: 1,
                serviceAmount: 1,
                serviceWorkTime: "",
                serviceCategory: "",
                serviceActive: false,
                //files: null,
            },
            activeDrop: false,
            catgList: [],
            //fileError: "",
        }
    },
    created() {
        this.fetchCategories();
    },
    methods: {
        // Категории
        async fetchCategories() {
            try {
                const response = await api.getCategories()
                this.catgList = response.data;
            } catch (error) {
                console.error('Ошибка при получении категорий:', error)
            }
        },
        // Переключение состояния dropzone
        toggleActive() {
            this.activeDrop = !this.activeDrop;
        },

        // handleFileUpload(event) {
        //     const file = event.target.files[0];
        //     if (file) {
        //         this.form.file = file; 
        //     } else {
        //         this.form.file = null;
        //     }
        // },

        async onSubmit() {
            const formData = new FormData();

            // Добавляем текстовые поля
            formData.append('title', this.form.serviceName);
            formData.append('descr', this.form.serviceDescrpt);
            formData.append('priceMin', parseFloat(this.form.serviceMinPrice));
            formData.append('priceMax', parseFloat(this.form.serviceMaxPrice));
            formData.append('amount', parseInt(this.form.serviceAmount, 10));
            formData.append('workTime', this.form.serviceWorkTime);
            formData.append('isActive', Boolean(this.form.serviceActive));
            formData.append('category', this.form.serviceCategory);

            // if (this.form.file) {
            //     formData.append('photo', this.form.file); 
            // } else {
            //     console.error("Файл не выбран!");
            // }

            // Логирование FormData для отладки
            for (let [key, value] of formData.entries()) {
                console.log(key, value);
            }

            try {
                const response = await api.createService(formData);
                console.log('Услуга успешно создана:', response.data);
                alert('Услуга успешно создана!');
            } catch (error) {
                console.error('Ошибка при создании услуги:', error.response ? error.response.data : error.message);
                alert('Произошла ошибка при создании услуги.');
            }
        }
    }
}
</script>

<style scoped>
.addService-window {
    margin: 0px auto;
    border-radius: 10px;
    padding: 15px;
    display: block;
    overflow: hidden;
    font-family: "Montserrat", sans-serif;
}

.addServiceForm__header {
    margin-bottom: 15px;
}

.addServiceForm__header h3 {
    margin-bottom: 5px;
}

label {
    display: block;
    text-align: left;
    margin-bottom: 5px;
    text-transform: uppercase;
    font-weight: 700;
    font-size: 12px;
    font-family: "Montserrat", sans-serif;
}

input,
textarea {
    display: block;
    border: none;
    padding: 5px;
    background-color: rgb(219, 219, 219);
    border-radius: 3px;
    font-family: "Montserrat", sans-serif;
}

.input-block {
    margin-bottom: 20px;
}

/* Стили полей ввода */
textarea {
    resize: vertical;
    max-height: 300px;
    min-height: 30px;
    width: 100%;
}

input {
    min-height: 30px;
    width: 100%;
}

.input-long {
    width: 100%;
}

.input-medium {
    width: 50%;
}

.input-short {
    width: 20%;
}

.input-errors {
    margin-top: 5px;
    font-family: "Montserrat", sans-serif;
    font-size: 10pt;
    color: brown;
}

button {
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    float: right;
    cursor: pointer;
}

.dropzone {
    width: 100%;
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    row-gap: 16px;
    border: 2px dashed blue;
    background-color: white;
    transition: 0.3s ease all;


}

.dropzone label {
    padding: 8px;
    color: white;
    background-color: blue;
    transition: 0.3s ease all;
    cursor: pointer;
}

.dropzone input {
    display: none;
}

.active-dropzone {
    color: white;
    border-color: white;
    background-color: blue;
}

.active-dropzone label {
    background-color: white;
    color: blue;
}
</style>