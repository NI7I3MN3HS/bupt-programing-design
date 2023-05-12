<template>
  <div class="Page_Container">
    <div class="Post_Container">
      <n-space vertical>
        <H1>帖子标题:{{ post_title }}</H1>
        <n-card>
          <n-button text color="black" @click="router.go(-1)">
            <template #icon
              ><n-avatar
                src="/"
                fallback-src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
              ></n-avatar
            ></template>
            作者{{ post_author }}
          </n-button>
        </n-card>
      </n-space>

      <n-divider />
      <div v-html="post_content"></div>
      <n-divider />
      <div class="CommentZone">
        <CommentEditor />
      </div>
    </div>
  </div>
</template>

<script setup>
import { onBeforeMount, ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import usePostStore from "../stores/modules/PostStore";
import { storeToRefs } from "pinia";
import CommentEditor from "../components/CommentEditor.vue";

const router = useRouter();
const route = useRoute();

const postStore = usePostStore();

const { post_content, post_title } = storeToRefs(postStore);

onBeforeMount(() => {
  postStore.GetPostInfo(route.params.id);
});

console.log(postStore.post_content);

// 当参数更改时获取新帖子信息
watch(
  () => route.params.id,
  async (newId) => {
    post_content.value = await postStore.GetPostInfo(newId);
  }
);
</script>

<style scoped>
.Page_Container {
  width: 70%;
  height: 100%;
  margin: 0 auto;
}
.Post_Container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
