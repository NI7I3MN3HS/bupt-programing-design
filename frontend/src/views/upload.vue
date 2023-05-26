<template>
  <n-upload :custom-request="myUpload" :show-file-list="false">
    <n-button>点击选择文件</n-button>
  </n-upload>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import useAuthStore from "../stores/modules/AuthStore";

const authStore = useAuthStore();

const myUpload = (file) => {
  const formData = new FormData();
  formData.append("avatar", file.file.file);
  //定义请求头
  const UserClient = axios.create({
    //baseURL: "http://localhost:8000",
    timeout: 10000,
    headers: {
      Accept: "application/json",
      Authorization: `Bearer ${authStore.token}`,
      headers: { "Content-Type": "multipart/form-data" },
    },
  });
  UserClient.post("/user/upload_avatar", formData)
    .then((response) => {
      console.log(response);
    })
    .catch((error) => {
      console.error(error);
    });
};
</script>

<style scoped></style>
