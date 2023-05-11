//认证状态管理

import { defineStore } from "pinia";
import Cookies from "js-cookie";

const useAuthStore = defineStore("auth", {
  state: () => {
    return {
      token: Cookies.get("access_token") ? Cookies.get("access_token") : "",
      is_Authenticated: Cookies.get("access_token") ? true : false,
    };
  },
  actions: {
    login() {
      this.token = Cookies.get("access_token");
      this.is_Authenticated = true;
      console.log("login");
    },
    logout() {
      Cookies.remove("access_token");
      this.is_Authenticated = false;
    },
  },
});

export default useAuthStore;
