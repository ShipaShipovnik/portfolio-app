import { defineStore } from "pinia";
import axios from "axios";
import LogOut from "@/views/LogOut.vue";

export const useUserStore = defineStore({
  id: "user",

  state: () => ({
    user: {
      isAuthenticated: false,
      id: null,
      name: '',
      email: '',
      access: null,
      refresh: null,
    },
  }),

  actions: {
    initStore() {
      console.log("initStore", localStorage.getItem("user.access"));

      if (localStorage.getItem("user.access")) {
        console.log("User has access!");

        this.user.access = localStorage.getItem("user.access");
        this.user.refresh = localStorage.getItem("user.refresh");
        this.user.id = localStorage.getItem("user.id");
        this.user.name = localStorage.getItem("user.name");
        this.user.email = localStorage.getItem("user.email");
        this.user.isAuthenticated = true;

        this.refreshToken();

        console.log("Initialized user:", this.user);
      }
    },

    setToken(data) {
      console.log("setToken", data);

      this.user.access = data.access;
      this.user.refresh = data.refresh;
      this.user.isAuthenticated = true;

      localStorage.setItem("user.access", data.access);
      localStorage.setItem("user.refresh", data.refresh);

      console.log("user.access: ", localStorage.getItem("user.access"));
    },

    removeToken() {
      console.log("removeToken");

      this.user.refresh = null;
      this.user.access = null;
      this.user.isAuthenticated = false;
      this.user.id = false;
      this.user.name = false;
      this.user.email = false;

      localStorage.setItem("user.access", "");
      localStorage.setItem("user.refresh", "");
      localStorage.setItem("user.id", "");
      localStorage.setItem("user.name", "");
      localStorage.setItem("user.email", "");
    },

    setUserInfo(user) {
      console.log("setUserInfo", user);

      this.user.id = user.id;
      this.user.name = user.name;
      this.user.email = user.email;

      localStorage.setItem("user.id", this.user.id);
      localStorage.setItem("user.name", this.user.name);
      localStorage.setItem("user.email", this.user.email);

      console.log("User", this.user);
    },

    refreshToken() {
      axios
        .post("/refresh/", {
          refresh: this.user.refresh,
        })
        .then((response) => {
          this.user.access = response.data.access;

          localStorage.setItem("user.access", response.data.access);

          axios.defaults.headers.common["Authorization"] =
            "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.log(error);

          this.removeToken();
        });
    },

    async refreshTokenIfNeeded() {
      if (!this.user.access) {
        await this.refreshToken();
      } else {
        try {
          // Проверяем, истек ли токен
          const tokenPayload = JSON.parse(atob(this.user.access.split('.')[1]));
          const tokenExpiration = tokenPayload.exp * 1000; // Переводим в миллисекунды
          const currentTime = Date.now();
  
          if (tokenExpiration < currentTime) {
            // Токен истек, обновляем его
            await this.refreshToken();
          }
        } catch (error) {
          console.log('Ошибка при проверке токена:', error);
          await this.refreshToken();
        }
      }
    },


    logout() {
      const token = this.user.access; 

      
      this.removeToken();

      
      axios.defaults.headers.common["Authorization"] = "";

      
      axios
        .post(
          "/logout/",
          {},
          {
            headers: {
              Authorization: `Bearer ${token}`, // Передаем токен в заголовке
            },
          }
        )
        .then(() => {
          console.log("User logged out successfully");
        })
        .catch((error) => {
          console.log("Logout error:", error);
        });
    },
  },
});
