import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
import Search from "@/views/Search.vue";
import LogIn from "@/views/LogIn.vue";
import Profile from "@/views/Profile.vue";
import AddService from "@/views/AddService.vue";
import LogOut from "@/views/LogOut.vue";
import EditProfile from "@/views/EditProfile.vue";
import ServiceDetail from "@/views/ServiceDetail.vue";
import EditService from "@/views/EditService.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/register",
      name: "register",
      component: Register,
    },
    {
      path: "/login",
      name: "login",
      component: LogIn,
    },
    {
      path: "/logout",
      name: "logout",
      component: LogOut,
    },
    {
      path: "/search",
      name: "search",
      component: Search,
    },
    {
      path: "/profile/:id",
      name: "profile",
      component: Profile,
    },
    {
      path: "/profile/edit",
      name: "profile-edit",
      component: EditProfile,
    },
    {
      path: "/add-service",
      name: "add-service",
      component: AddService,
    },
    {
      path: "/services/:id",
      name: "service-detail",
      component: ServiceDetail,
    },
    {
      path: "/services/:id/edit",
      name: "service-edit",
      component: EditService,
    },
  ],
});

export const goToProfile = (userId) => {
  router.push({ name: 'profile', params: { id: userId } });
};

export default router;
