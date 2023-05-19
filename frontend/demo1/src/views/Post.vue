<template>
  <div class="Page_Container">
    <div class="Post_Container">
      <n-space vertical>
        <div class="post_title">{{ post_title }}</div>
        <n-card style="min-width: 60ch" :bordered="false">
          <n-space justify="space-between">
            <n-button text color="black" @click="toAuthorProfile">
              <n-space align="center">
                <n-avatar
                  round
                  :size="36"
                  :src="post_author_avatar_url"
                  fallback-src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
                ></n-avatar>
                <n-space vertical>
                  <div style="font-weight: 600; font-size: 16px">
                    {{ post_author_name }}
                  </div>
                  <div>{{ post_author_introduction }}</div>
                </n-space>
              </n-space>
            </n-button>
            <n-button
              color="#056de8"
              v-if="userStore.id != post_user_id && !is_follow_author"
              @click="CreateFollow"
              >关注</n-button
            >
            <n-button
              color="#8590a6"
              v-if="userStore.id != post_user_id && is_follow_author"
              @click="DeleteFollow"
              >取消关注</n-button
            >
          </n-space>
        </n-card>
      </n-space>

      <n-divider />
      <div v-html="post_content"></div>
      <n-divider />
      <n-space justify="center">
        <n-button @click="CreatePostLike">like</n-button>
        <div>点赞数：{{ post_like }}</div>
      </n-space>
    </div>
  </div>
  <div class="CommentZoneBG">
    <div class="Page_Container">
      <div class="Comment_Container">
        <div class="CommentZone">
          <n-space vertical>
            <n-space justify="center">
              <div style="font-size: 16px">
                全部评论（{{ post_comment_count }}）
              </div>
            </n-space>
            <CommentEditor ref="comment_input" />
            <n-button color="#056de8" @click="CreateComment">发表</n-button>
            <div v-for="item in post_comment">
              <CommentCard :data="item" />
            </div>
            <n-card
              ><n-space justify="center"><div>评论已经到底了！</div></n-space>
            </n-card>
          </n-space>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onBeforeMount, ref, watch, computed } from "vue";
import { useRoute, useRouter, onBeforeRouteUpdate } from "vue-router";
import usePostStore from "../stores/modules/PostStore";
import useAuthStore from "../stores/modules/AuthStore";
import useUserStore from "../stores/modules/UserStore";
import { storeToRefs } from "pinia";
import CommentEditor from "../components/CommentEditor.vue";
import CommentCard from "../components/CommentCard.vue";
import axios from "axios";

const router = useRouter();
const route = useRoute();

//导入请求状态
const authStore = useAuthStore();
//导入帖子状态
const postStore = usePostStore();
//导入用户状态
const userStore = useUserStore();

const {
  post_content,
  post_title,
  post_comment,
  post_user_id,
  post_author_name,
  post_author_avatar_url,
  is_follow_author,
  post_author_introduction,
  post_like,
  post_comment_count,
} = storeToRefs(postStore);

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
  postStore.GetPostInfoAsync(route.params.id);
});

//仅当 id 更改时才获取帖子数据
onBeforeRouteUpdate(async (to, from) => {
  if (to.params.id !== from.params.id) {
    postStore.GetPostInfoAsync(route.params.id);
  }
});

//发布评论
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
    postStore.GetPostInfoAsync(route.params.id); //重新获取帖子信息
  } else {
    alert("请先登录");
    router.push("/loginandregister");
  }
}

//进入作者主页
function toAuthorProfile() {
  router.push(`/user/${post_user_id.value}`);
}
//创建关注
function CreateFollow() {
  if (authStore.is_Authenticated == false) {
    alert("请先登录");
  } else {
    UserClient.post(`/follow/create`, { followed_id: post_user_id.value })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
    is_follow_author.value = true;
  }
}
//取消关注
function DeleteFollow() {
  UserClient.delete(`/follow/delete`, {
    data: { followed_id: post_user_id.value },
  })
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.error(error);
    });
  is_follow_author.value = false;
}
//创建帖子点赞
function CreatePostLike() {
  if (authStore.is_Authenticated == false) {
    alert("请先登录");
  } else {
    UserClient.post(`/post/like/create`, { post_id: postStore.post_id })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
    postStore.GetPostInfoAsync(route.params.id); //重新获取帖子信息
  }
}
</script>

<style lang="less">
.Page_Container {
  width: 70%;
  height: 100%;
  margin: 0 auto;
}
.Comment_Container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.Post_Container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 5ch;
}
.post_title {
  font-size: 28px;
  font-weight: bold;
  line-height: 42px;
  color: #292525;
  margin: 40px auto 0px;
}
.CommentZoneBG {
  background-color: #f4f4f4;
}
.CommentZone {
  width: 40vw;
  margin-top: 5ch;
  margin-bottom: 5ch;
}
</style>
