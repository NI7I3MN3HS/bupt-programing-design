<template>
  <div class="BackGround">
    <div class="PageContainer">
      <n-space align="center" vertical>
        <div v-for="item in postList" class="PostList">
          <PostCard :data="item" />
        </div>
      </n-space>
    </div>
  </div>
</template>

<script setup>
import PostCard from "@/components/PostCard.vue";
import { ref, onBeforeMount } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const postList = ref([]);

function fetchAllPost() {
  axios
    .get("/post/all")
    .then((res) => {
      console.log(res.data);
      postList.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
}

// 每次加载从后端获取所有帖子
onBeforeMount(() => {
  fetchAllPost();
});
</script>

<style scoped lang="less">
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
