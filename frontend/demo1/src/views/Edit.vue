<template>
  <div class="Container">
    <!--这里设置文章标题-->
    <div>这里是标题</div>
    <n-input v-model:value="Title" type="text" placeholder="请输入标题" />
    <div>这里是文章</div>
    <!-- 这里是正文内容 -->
    <WangEditor />
    <div>这里是发布设置</div>
    <n-button @click="Post">发布</n-button>
  </div>
</template>

<script setup>
import WangEditor from "@/components/WangEditor.vue";
import { ref } from "vue";
import { storeToRefs } from "pinia";
import usePostStore from "../stores/modules/PostStore";

const postStore = usePostStore();

const { post_title } = storeToRefs(postStore);

const Title = ref(post_title);

function Post() {
  postStore.CreatePost();
}
</script>

<style lang="less" scoped>
.Container {
  min-height: calc(100vh);
}
</style>
