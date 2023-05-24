<template>
  <n-config-provider :theme-overrides="themeOverrides">
    <n-space justify="center">
      <n-input
        style="width: 50vw; top: 30px; padding: 5px"
        v-model:value="searchValue"
        size="large"
        placeholder="搜索"
        passively-activated
        @keydown.enter="toSearch"
      />
    </n-space>
    <div class="demo-tabs">
      <el-tabs v-model="activeName">
        <el-tab-pane label="帖子" name="post">
          <RouterView />
        </el-tab-pane>
        <el-tab-pane label="用户" name="user">
          <RouterView />
        </el-tab-pane>
      </el-tabs>
    </div>
  </n-config-provider>
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
import { useRouter, useRoute } from "vue-router";
import { useMessage } from "naive-ui";

const themeOverrides = {
  Input: {
    borderFocus: "1px solid #8590a6",
    boxShadowFocus: "0 0 0 2px rgba(133, 144, 166, 0.2)",
    borderHover: "1px solid #8590a6",
    caretColor: "#8590a6FF",
  },
};

const router = useRouter();
const message = useMessage();

//tab页ref
const activeName = ref("post");

//搜索框ref
const searchValue = ref("");

function toSearch() {
  if (searchValue.value.trim().length == 0) {
    message.warning("请输入搜索内容");
    return;
  }
  router.push({
    path: `/search/${activeName.value}`,
    query: {
      keyword: searchValue.value,
    },
  });
}

//当tab页发生变化时，更新路由
watch(
  () => activeName.value,
  (newVal) => {
    router.push({
      path: `/search/${newVal}`,
      query: {
        keyword: searchValue.value,
      },
    });
  }
);
</script>

<style scoped lang="less">
.demo-tabs {
  margin: 0 auto;
}

::v-deep .el-tabs__header {
  width: 50vw;
  margin: 50px auto 0;
}
</style>
