import './assets/base.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import vSelect from 'vs-vue3-select'
import 'vs-vue3-select/dist/vs-vue3-select.css'

const app = createApp(App)

axios.defaults.baseURL='http://127.0.0.1:8000/api';

app.use(createPinia())
app.use(router,axios)
app.component('v-select', vSelect)
app.mount('#app')
