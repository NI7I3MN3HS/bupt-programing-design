<template>
  <el-tabs v-model="activeName" class="demo-tabs">
    <el-tab-pane label="帖子" name="first">
      <SearchPost />
    </el-tab-pane>
    <el-tab-pane label="用户" name="second">
      <div v-for="item in followData">
        <Follow :data="item" /></div
    ></el-tab-pane>
  </el-tabs>
</template>

<script setup>
import axios from "axios";
import {
  ref,
  reactive,
  defineComponent,
  watch,
  onBeforeMount,
  toRefs,
  defineProps,
  defineExpose,
  computed,
  defineEmits,
} from "vue";
import PostCard from "./PostCard.vue";
import { Search } from "@vicons/ionicons5";

//tab页ref
const activeName = ref("first");
</script>

<style scoped lang="less">
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
</style>
