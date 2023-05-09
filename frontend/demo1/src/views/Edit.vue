<template>
  <div class="Container">
    <WangEditor v-model="Content" />
    <div>这里是发布设置</div>
    <n-button @click="Post">发布</n-button>
  </div>
</template>

<script setup>
import WangEditor from "@/components/WangEditor.vue";
import { ref } from "vue";
import axios from "axios";
import Cookies from "js-cookie";

const Content = ref("");

const UserClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${Cookies.get("access_token")}`,
  },
});

const Post = () => {
  UserClient.post("/post/", {
    content: Content.value,
  })
    .then((response) => {
      console.log(response);
    })
    .catch((error) => {
      console.error(error);
    });
};
</script>

<style lang="less" scoped>
.Container {
  min-height: calc(100vh);
}
</style>
