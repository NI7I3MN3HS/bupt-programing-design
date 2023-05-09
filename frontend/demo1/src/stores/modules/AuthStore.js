import { defineStore } from "pinia";
import Cookies from "js-cookie";

const useAuthStore = defineStore("auth", {
  state: () => {
    return {
      token: Cookies.get("access_token") ? Cookies.get("access_token") : "",
      is_Authenticated: Cookies.get("access_token") ? true : false,
    };
  },
  getters: {},
});

export default useAuthStore;
