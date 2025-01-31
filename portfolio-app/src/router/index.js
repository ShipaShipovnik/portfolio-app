import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Register from '../views/Register.vue'
import FAQ from '../views/FAQ.vue'
import Search from '@/views/Search.vue'
import LogIn from '@/views/LogIn.vue'
import ServicesList from '@/views/ServicesList.vue'
import Profile from '@/views/Profile.vue'
import AddService from '@/views/AddService.vue'
import LogOut from '@/views/LogOut.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
    },
    {
      path: '/login',
      name: 'login',
      component: LogIn,
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogOut,
    },
    {
      path: '/faq',
      name: 'FAQ',
      component: FAQ,
    },
    {
      path: '/search',
      name: 'search',
      component: Search,
    },
    {
      path: '/list',
      name: 'list',
      component: ServicesList,
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: Profile,
    },
    {
      path: '/add-service',
      name: 'add-service',
      component: AddService,
    },
    
  ],
})

export default router
