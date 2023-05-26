<template>
  <div class="Page_Container">
    <div class="Post_Container">
      <n-space vertical>
        <div class="post_title">{{ post_title }}</div>
        <n-card style="width: 60ch; margin: 0 auto" :bordered="false">
          <n-space justify="space-between">
            <n-button text color="black" @click="toAuthorProfile">
              <n-space align="center">
                <n-avatar
                  round
                  :size="36"
                  :src="post_author_avatar_url"
                  fallback-src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
                ></n-avatar>
                <n-space vertical align="start">
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
      <div
        style="max-width: 70vw"
        v-html="post_content"
        class="PostContent"
      ></div>
      <n-divider />
      <n-space justify="center">
        <!--点赞按钮-->
        <n-button text @click="CreatePostLike" v-if="is_like_post == false">
          <template #icon>
            <n-icon>
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                <path
                  d="M24.926 16.496a2.389 2.389 0 00-2.27-3.137l-4.61.002.1-.754c.275-2.09.178-3.497-.292-4.17-.417-.596-1.085-1-1.642-1.047-.767-.065-1.282.248-1.454.908-.077.297-.57 1.56-1.002 2.47-.797 1.68-1.45 2.59-2.313 2.59-.56 0-1.446 0-2.66.003a.744.744 0 00-.744.743v9.534c0 .41.333.744.744.744h11.985c.94 0 1.772-.61 2.057-1.515l2.1-6.37z"
                  stroke="#4E5969"
                  stroke-width="1.7"
                  stroke-linejoin="round"
                />
                <path
                  d="M11.553 24.618V13.503"
                  stroke="#4E5969"
                  stroke-width="1.7"
                />
              </svg>
            </n-icon>
          </template>
          {{ post_like }}
        </n-button>
        <!--取消点赞按钮-->
        <n-button text @click="DeletePostLike" v-if="is_like_post == true">
          <template #icon>
            <n-icon>
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                <path
                  d="M25.383 16.614a2.389 2.389 0 00-2.27-3.137l-4.61.002.1-.754c.276-2.09.178-3.496-.292-4.169-.416-.596-1.085-1-1.642-1.047-.767-.066-1.282.247-1.454.908-.076.296-.57 1.56-1.002 2.469-.542 1.143-1.359 1.93-2.098 2.316-.49.256-.952.722-.952 1.274V22.5a2 2 0 002 2h8.063c.94 0 1.772-.61 2.057-1.515l2.1-6.37z"
                  fill="#F04142"
                />
                <path
                  d="M8.497 14.945v8"
                  stroke="#F04142"
                  stroke-width="2.4"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
            </n-icon> </template
          >{{ post_like }}
        </n-button>
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
import { useMessage, useDialog } from "naive-ui";
import { onBeforeMount, ref, watch, computed } from "vue";
import { useRoute, useRouter, onBeforeRouteUpdate } from "vue-router";
import usePostStore from "@/stores/modules/PostStore";
import useAuthStore from "@/stores/modules/AuthStore";
import useUserStore from "@/stores/modules/UserStore";
import { storeToRefs } from "pinia";
import CommentEditor from "@/components/CommentEditor.vue";
import CommentCard from "@/components/CommentCard.vue";
import axios from "axios";

const message = useMessage();
const dialog = useDialog();
const router = useRouter();
const route = useRoute();

//导入请求状态
const authStore = useAuthStore();
//导入帖子状态
const postStore = usePostStore();
//导入用户状态
const userStore = useUserStore();

const {
  is_like_post,
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
  //baseURL: "http://localhost:8000",
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
        dialog.success({
          title: "评论成功",
          content: "经验+3 告辞！",
          positiveText: "溜了溜了",
        });
      })
      .catch((error) => {
        console.error(error);
      });
    comment_input.value.commentvalueHtml = ""; //清空评论框
    postStore.GetPostInfoAsync(route.params.id); //重新获取帖子信息
  } else {
    message.error("请先登录");
  }
}

//进入作者主页
function toAuthorProfile() {
  router.push(`/user/${post_user_id.value}`);
}
//创建关注
function CreateFollow() {
  if (authStore.is_Authenticated == false) {
    message.error("请先登录");
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

//点赞
function CreatePostLike() {
  if (authStore.is_Authenticated == false) {
    message.error("请先登录");
  } else {
    UserClient.post(`/like/create`, {
      post_id: postStore.post_id,
      comment_id: 0,
    })
      .then((res) => {
        is_like_post.value = true;
        //点赞数加一
        post_like.value++;
      })
      .catch((err) => {
        console.log(err);
      });
  }
}
//取消点赞
function DeletePostLike() {
  UserClient.delete(`/like/delete`, {
    data: {
      post_id: postStore.post_id,
      comment_id: 0,
    },
  })
    .then((res) => {
      is_like_post.value = false;
      //点赞数减一
      post_like.value--;
    })
    .catch((err) => {
      console.log(err);
    });
}
</script>

<style scoped lang="less">
.Page_Container {
  width: 50%;
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
.PostContent {
  width: 50vw;
  /deep/ * {
    img {
      max-height: 100%;
      max-width: 100%;
      vertical-align: middle;
    }
  }
}
</style>
