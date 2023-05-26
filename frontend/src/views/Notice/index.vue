<template>
  <div class="PageContainer">
    <n-space vertical
      ><div class="NoticeTitle">
        <n-space justify="center">全部通知</n-space>
      </div>
      <n-divider />
      <el-tabs v-model="activeName" class="demo-tabs" stretch="true">
        <el-tab-pane label="系统" name="first">
          <n-space vertical>
            <div v-for="item in notices"><NoticeCard :data="item" /></div>
          </n-space>
        </el-tab-pane>
      </el-tabs>
    </n-space>
  </div>
</template>
<script setup>
import axios from "axios";
import { onBeforeMount, ref } from "vue";
import useAuthStore from "../../stores/modules/AuthStore";
import useUserStore from "../../stores/modules/UserStore";
import NoticeCard from "./NoticeCard.vue";

const activeName = ref("first");

const authStore = useAuthStore();
const userStore = useUserStore();

// 通知列表
const notices = ref([]);

const UserClient = axios.create({
  //baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
  },
});

// 获取通知列表
const getNotices = async () => {
  const res = await UserClient.get("/notification/all");
  notices.value = res.data;
};

onBeforeMount(() => {
  getNotices();
});
</script>
<style lang="less">
.demo-tabs > .el-tabs__content {
  padding: 16px;
  color: #6b778c;
  font-size: 16px;
  font-weight: 600;
}
.PageContainer {
  padding: 32px;
  width: 40%;
  margin: 0 auto;
}
.NoticeTitle {
  font-size: 32px;
  font-weight: 600;
}
</style>
