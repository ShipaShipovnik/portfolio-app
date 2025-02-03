<template>
    <div class="main-page container shadow p-5">
        <div class="addService-window">
            <form ref="addServiceForm" @submit.prevent="onSubmit">
                <h3>Заполните информацию об услуге</h3>
                <hr>
                <br>

                <div class="input-block">
                    <label>Название услуги</label>
                    <input type="text" class="form-control" v-model="form.serviceTitle"
                        placeholder="Какую услугу вы предоставляете?">
                </div>

                <div class="input-block">
                    <label>*Описание</label>
                    <textarea v-model="form.serviceDescrpt" placeholder="Опишите предоставляемую услугу."></textarea>
                </div>

                <div class="input-block">
                    <label>Цена</label>
                    <input type="text" class="form-control" v-model.number="form.servicePrice"
                        placeholder="Какую услугу вы предоставляете?">
                </div>

                <div class="input-group mb-3">
                    <input type="file"  accept="image/*" class="form-control" id="inputGroupFile02" @change="handleFileUpload">
                    <label class="input-group-text" for="inputGroupFile02">Upload</label>
                </div>
                <!-- <div class="input-block">
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
                </div> -->

                <div class="input-block">
                    <label for="">Категория:</label>
                    <v-select v-model="form.serviceCategory" :options="categories" label="name"
                        :reduce="category => category.id" placeholder="Выберите категорию"></v-select>
                </div>


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
import vSelect from 'vs-vue3-select'
import 'vs-vue3-select/dist/vs-vue3-select.css'
import axios from 'axios'

export default {
    components: {
        vSelect,
    },
    data() {
        return {
            form: {
                serviceTitle: "",
                serviceDescrpt: "",
                servicePrice: 1,
                serviceCategory: null,
                serviceActive: false,
                image: null,
            },
            activeDrop: false,
            categories: [],
        }
    },
    created() {
        this.getCategories();
    },
    methods: {

        handleFileUpload(event) {
            this.form.image = event.target.files[0]; // Обновление поля файла
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

        async onSubmit() {
            const formData = new FormData()

            formData.append('title', this.form.serviceTitle)
            formData.append('descr', this.form.serviceDescrpt)
            formData.append('price', parseFloat(this.form.servicePrice))
            formData.append('isActive', Boolean(this.form.serviceActive))
            formData.append('category', this.form.serviceCategory) 

            if (this.form.image) {
                formData.append('image', this.form.image)
            }

            try {
                const response = await axios.post(
                    'http://127.0.0.1:8000/api/services/add-service', // Проверьте URL endpoint
                    formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data',

                        }
                    }
                );

                // Сброс формы после успешной отправки
                this.form = {
                    title: "",
                    descr: "",
                    price: 1,
                    category: null,
                    isActive: false,
                    image: null,
                };

                this.$router.push('/');
            } catch (error) {
                console.error('Submission error:', error);
                const errorMessage = error.response?.data?.error || error.message
                alert(`Ошибка при создании услуги: ${JSON.stringify(errorMessage)}`);
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