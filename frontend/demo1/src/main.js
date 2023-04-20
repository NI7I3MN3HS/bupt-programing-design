import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import naive from "naive-ui";

import ElementPlus from "element-plus";

import "./assets/base.less";

import axios from "axios";
axios.defaults.withCredentials = true; //跨域请求时发送cookie
axios.defaults.baseURL = "http://localhost:8000"; //设置默认请求地址

const app = createApp(App);

app.use(createPinia()).use(router).use(naive).use(ElementPlus).mount("#app");
