//其他用户状态管理

import { defineStore } from "pinia";
import axios from "axios";

const useOtherUserStore = defineStore("user", {
  state: () => {
    return {
      id: 0,
      username: "",
      email: "",
      avatar_url: null,
      is_active: true,
      introduction: "",
    };
  },
  actions: {
    GetDefiniteUserInfo(user_id) {
      axios
        .get(`/user/${user_id}`)
        .then((response) => {
          this.username = response.data.username;
          this.email = response.data.email;
          this.avatar_url = response.data.avatar_url;
          this.is_active = response.data.is_active;
          this.introduction = response.data.introduction;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
});

export default useOtherUserStore;
