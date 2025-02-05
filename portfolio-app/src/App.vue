<script>
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';
import Toast from './components/Toast.vue';
import { useUserStore } from '@/stores/user'
import axios from 'axios';

export default {
  components: {
    Toast,
    AppHeader,
    AppFooter,
  },
  setup() {
    const userStore = useUserStore()

    return {
      userStore
    }
  },

  beforeCreate() {
    this.userStore.initStore()

    const token = this.userStore.user.access

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;

    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  }
}
</script>

<template>
  <div class="wrapper">
    <AppHeader />
    <div class="content">
      <router-view>
      </router-view>
    </div>
    <AppFooter />
    <Toast />
  </div>

</template>

<style scoped>
.wrapper{
  min-height: 100vh;
  position: relative;
}
</style>
