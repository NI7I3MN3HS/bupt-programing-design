//个人用户状态管理

import { defineStore } from "pinia";
import axios from "axios";
import useAuthStore from "@/stores/modules/AuthStore";

//导入请求状态
const authStore = useAuthStore();

//定义请求头
const UserClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
  },
});

const useUserStore = defineStore("user", {
  state: () => {
    return {
      username: "",
      email: "",
      avatar_url: "",
      is_active: true,
      id: 0,
      introduction: null,
    };
  },
  actions: {
    setUserInfo() {
      UserClient.get("/user/")
        .then((response) => {
          this.username = response.data.username;
          this.email = response.data.email;
          this.avatar_url = response.data.avatar_url;
          this.is_active = response.data.is_active;
          this.id = response.data.id;
          this.introduction = response.data.introduction;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
});

export default useUserStore;
