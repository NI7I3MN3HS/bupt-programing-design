<template>
  <div class="PageContainer">
    <n-space vertical
      ><div class="NoticeTitle">
        <n-space justify="center">全部通知</n-space>
      </div>
      <n-divider />
      <el-tabs v-model="activeName" class="demo-tabs" stretch="true">
        <el-tab-pane label="评论" name="first"><NoticeCard /></el-tab-pane>
        <el-tab-pane label="系统" name="second">Config</el-tab-pane>
      </el-tabs>
    </n-space>
  </div>
</template>
<script setup>
import { ref } from "vue";
import NoticeCard from "./NoticeCard.vue";

const activeName = ref("first");
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
