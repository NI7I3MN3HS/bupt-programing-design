<template>
  <div class="Page_Container">
    <div class="Post_Container">
      <n-space vertical>
        <div class="post_title">{{ post_title }}</div>
        <n-card>
          <n-button text color="black" @click="router.push(post_user_id)">
            <template #icon
              ><n-avatar
                src="/"
                fallback-src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
              ></n-avatar
            ></template>
            作者{{ post_authon }}
          </n-button>
        </n-card>
      </n-space>

      <n-divider />
      <div v-html="post_content"></div>
      <n-divider />
      <div class="CommentZone">
        <n-space vertical>
          <CommentEditor ref="comment_input" />
          <n-button color="#056de8" @click="CreateComment">发表</n-button>
          <n-divider />
          <div v-for="item in post_comment">
            <n-card>
              <template #header
                ><n-space
                  ><n-avatar></n-avatar>
                  <div>作者{{ commentUsername(id) }}</div></n-space
                ></template
              >
              <div v-html="item.content"></div>
            </n-card>
          </div>
          <n-card>评论已经到底了！</n-card>
        </n-space>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onBeforeMount, ref, watch, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import usePostStore from "../stores/modules/PostStore";
import useAuthStore from "../stores/modules/AuthStore";
import { storeToRefs } from "pinia";
import CommentEditor from "../components/CommentEditor.vue";
import axios from "axios";

const router = useRouter();
const route = useRoute();

//导入请求状态
const authStore = useAuthStore();
//导入帖子状态
const postStore = usePostStore();

const { post_content, post_title, post_comment, post_user_id } =
  storeToRefs(postStore);

//评论框ref
const comment_input = ref();

//定义axios请求头
const UserClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
  },
});

//dom加载前获取帖子信息
onBeforeMount(() => {
  postStore.GetPostInfo(route.params.id);
});

// 当参数更改时获取新帖子信息
watch(
  () => route.params.id,
  async (newId) => {
    post_content = await postStore.GetPostInfo(newId); //获取新帖子信息
  }
);

function CreateComment() {
  if (authStore.is_Authenticated) {
    //后期改一下路径
    UserClient.post("/comment/create", {
      content: comment_input.value.commentvalueHtml,
      post_id: postStore.post_id,
      parent_id: 0,
    })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
    comment_input.value.commentvalueHtml = ""; //清空评论框
  } else {
    alert("请先登录");
    router.push("/loginandregister");
  }
}

const commentUsername = computed((id) => {
  return getCommentUser(id);
});
</script>

<style scoped lang="less">
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
.post_title {
  font-size: 50px;
  font-weight: bolder;
}
</style>
