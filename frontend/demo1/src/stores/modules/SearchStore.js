//搜索状态管理

import { defineStore } from "pinia";
import Cookies from "js-cookie";

const useSearchStore = defineStore("search", {
  persist: true,
  state: () => {
    return {
      searchstr: null,
    };
  },
  actions: {},
});

export default useSearchStore;
