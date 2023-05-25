<template>
  <n-config-provider :theme-overrides="themeOverrides">
    <n-space justify="center">
      <n-dropdown
        trigger="click"
        :options="options"
        @select="handleSelect"
        style="width: 50vw"
      >
        <n-input
          style="width: 50vw; top: 30px; padding: 5px"
          v-model:value="searchValue"
          size="large"
          placeholder="搜索"
          passively-activated
          @keydown.enter="toSearch"
        />
      </n-dropdown>
    </n-space>
    <div class="demo-tabs">
      <el-tabs v-model="activeName" @tab-change="handleTabsChange">
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
import Cookies from "js-cookie";
import axios from "axios";
import {
  ref,
  reactive,
  defineComponent,
  watch,
  onMounted,
  onBeforeMount,
  toRefs,
  defineProps,
  defineExpose,
  computed,
  defineEmits,
  getCurrentInstance,
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
const route = useRoute();
const message = useMessage();

//tab页ref

const activeName = ref("post");

//搜索框ref
const searchValue = ref();

function toSearch() {
  if (searchValue.value.trim().length == 0) {
    message.warning("请输入搜索内容");
    return;
  }
  storeSearchHistory(searchValue.value);
  //存储搜索词
  sessionStorage.setItem("searchValue", searchValue.value);
  router.push({
    path: `/search/${activeName.value}`,
    query: {
      keyword: searchValue.value,
    },
  });
}

//载入时读取搜索历史
onBeforeMount(() => {
  tagList.value = getSearchHistory();
  const storedQuery = sessionStorage.getItem("searchValue");
  if (storedQuery) {
    searchValue.value = storedQuery;
  }
});

//当tab页发生变化时，更新路由
watch(
  () => activeName.value,
  (newVal) => {
    const storedQuery = sessionStorage.getItem("searchValue");
    if (storedQuery) {
      searchValue.value = storedQuery;
    }
    router.push({
      path: `/search/${newVal}`,
      query: {
        keyword: searchValue.value,
      },
    });
  }
);

/*
//监听路由参数，动态切换tab
watch(
  () => route.path,
  (newVal) => {
    if (newVal == "/search/post") {
      activeName.value = "post";
    } else if (newVal == "/search/user") {
      activeName.value = "user";
    } else if (newVal == "/search/post/") {
      activeName.value = "post";
    } else if (newVal == "/search/user/") {
      activeName.value = "user";
    }
  }
);*/

//同时监听path和query的变化
watch(
  () => [route.path, route.query],
  ([newPath, newQuery]) => {
    if (newPath == "/search/post" || newPath == "/search/post/") {
      activeName.value = "post";
    } else if (newPath == "/search/user" || newPath == "/search/user/") {
      activeName.value = "user";
    }
    if (newQuery.keyword) {
      searchValue.value = newQuery.keyword;
    }
  }
);

//搜索历史
const tagList = ref([]);

const options = computed(() => {
  return tagList.value.map((item) => {
    return {
      label: item,
      key: item,
    };
  });
});

// 存储搜索历史
function storeSearchHistory(searchTerm) {
  let searchHistory = getSearchHistory();

  // 如果搜索历史中已经有这个搜索词，那么就不需要再添加
  if (!searchHistory.includes(searchTerm)) {
    // 如果搜索历史超过了10条，移除最旧的一条
    if (searchHistory.length >= 10) {
      searchHistory.shift();
    }

    // 添加新的搜索词
    searchHistory.push(searchTerm);

    // 将搜索历史数组转换为字符串
    let searchHistoryString = JSON.stringify(searchHistory);

    // 存储在cookie中
    Cookies.set("searchHistory", searchHistoryString);
  }
}

// 读取搜索历史
function getSearchHistory() {
  let searchHistoryString = Cookies.get("searchHistory");

  // 如果找到了名为 "searchHistory" 的cookie，那么返回它的值
  if (searchHistoryString) {
    return JSON.parse(searchHistoryString);
  }

  // 如果没有找到名为 "searchHistory" 的cookie，那么返回一个空数组
  return [];
}

//点击搜索历史
function handleSelect(key) {
  searchValue.value = String(key);
  toSearch();
}
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
