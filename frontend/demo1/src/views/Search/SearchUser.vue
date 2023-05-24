<template>
  <div class="BackGround">
    <div class="PageContainer">
      <n-space vertical align="center">
        <div v-for="item in userList">
          <SearchUserCard :data="item" />
        </div>
        <div v-if="userList.length == 0">找不到你想要的</div>
      </n-space>
    </div>
  </div>
</template>

<script setup>
import { onBeforeMount, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import SearchUserCard from "@/components/SearchUserCard.vue";

const route = useRoute();
const router = useRouter();

const userList = ref([]);

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
      "/user/search",
      {},
      {
        params: {
          keyword: route.query.keyword,
        },
      }
    )
    .then((res) => {
      console.log(res.data);
      userList.value = res.data;
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
