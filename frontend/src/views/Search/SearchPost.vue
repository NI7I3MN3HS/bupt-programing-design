<template>
  <div class="BackGround">
    <div class="PageContainer">
      <n-space vertical align="center">
        <div v-for="item in postList">
          <SearchPostCard :data="item" />
        </div>
        <div v-if="postList.length == 0">找不到你想要的</div>
      </n-space>
    </div>
  </div>
</template>
<script setup>
import { onBeforeMount, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import SearchPostCard from "@/components/SearchPostCard.vue";

const route = useRoute();
const router = useRouter();

const postList = ref([]);

onBeforeMount(() => {
  fetchData();
});

//当路由参数发生变化时，重新获取数据
router.afterEach(() => {
  fetchData();
});

function fetchData() {
  axios
    .post(
      "/post/search",
      {},
      {
        params: {
          keyword: route.query.keyword,
        },
      }
    )
    .then((res) => {
      console.log(res.data);
      postList.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
}
</script>
<style lang="less" scoped>
.BackGround {
  background-color: #f4f4f4;
  min-height: 100vh;
}
.PageContainer {
  width: 60%;
  margin: 0 auto;
  padding: 50px 0px 50px 0px;
}
</style>
