<template>
  <n-card hoverable
    ><n-space
      ><div class="Left">
        <n-avatar :size="48" :src="userData.avatar_url" round />
      </div>
      <div class="Right">
        <div class="PostInfo">
          <n-space align="center">
            <div class="AuthorName">{{ userData.username }}</div>
            <div class="PostTime">{{ data.created_time }}</div>
          </n-space>
        </div>
        <n-space vertical>
          <div class="PostTitle">{{ data.title }}</div>
          <div class="PostContent">
            <n-ellipsis style="max-width: 400px" :line-clamp="2">
              <div style="max-height: 100px" v-html="data.content"></div>
            </n-ellipsis>
          </div>
        </n-space>
      </div>
    </n-space>
    <template #footer>
      <div class="PostExtraInfo">
        <n-space align="center">
          <!--点赞按钮-->
          <n-button text @click="CreatePostLike" v-if="likestate == false">
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
            {{ data.like_count }}
          </n-button>
          <!--取消点赞按钮-->
          <n-button text @click="DeletePostLike" v-if="likestate == true">
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
            >{{ data.like_count }}
          </n-button>
          <!--评论按钮-->
          <n-button text @click="toCommentZone">
            <template #icon>
              <n-icon>
                <svg width="24" height="24" viewBox="0 0 48 48" fill="none">
                  <path
                    d="M15 20h18m-18 9h9M7 41h17.63C33.67 41 41 33.67 41 24.63V24c0-9.389-7.611-17-17-17S7 14.611 7 24v17z"
                    stroke="#4E5969"
                    stroke-width="2"
                  />
                </svg>
              </n-icon>
            </template>
            {{ data.comment_count }}
          </n-button>
        </n-space>
      </div></template
    >
  </n-card>
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
import useAuthStore from "../stores/modules/AuthStore";

const authStore = useAuthStore();

//定义axios请求头
const UserClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
  },
});

const props = defineProps({
  //子组件接收父组件传递过来的值
  data: {
    type: Object,
  },
});
const { data } = toRefs(props);

console.log(data.value);

//获取帖子的作者信息
const userData = ref({});

//获取帖子的作者信息
function getUserData() {
  axios
    .get(`/user/${data.value.user_id}`)
    .then((res) => {
      userData.value = res.data;
      console.log(userData.value);
    })
    .catch((err) => {
      console.log(err);
    });
}

//点赞状态
const likestate = ref(false);

//获取当前用户是否已经点赞
function getLikeState(post_id, comment_id) {
  UserClient.get(`/like/is_like/${post_id}/${comment_id}`)
    .then((res) => {
      likestate.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
}

onBeforeMount(() => {
  getUserData();
  getLikeState(data.value.id, 0);
});

//点赞
function CreatePostLike() {
  UserClient.post(`/like/create`, {
    post_id: data.value.id,
    comment_id: 0,
  })
    .then((res) => {
      likestate.value = true;
      //点赞数加一
      data.value.like_count++;
    })
    .catch((err) => {
      console.log(err);
    });
}
//取消点赞
function DeletePostLike() {
  UserClient.delete(`/like/delete`, {
    data: {
      post_id: data.value.id,
      comment_id: 0,
    },
  })
    .then((res) => {
      likestate.value = false;
      //点赞数减一
      data.value.like_count--;
    })
    .catch((err) => {
      console.log(err);
    });
}
//跳转到评论区
function toCommentZone() {
  window.location.href = `/post/${data.value.id}`;
}
</script>

<style lang="less" scoped>
.n-card {
  width: 600px;
  height: 200px;
}
.AuthorName {
  font-size: 14px;
  color: #838ead;
  font-weight: 500;
}
.PostTime {
  font-size: 12px;
  color: #c7ccda;
  font-weight: 400;
}
.PostTitle {
  font-size: 16px;
  color: #2c3a61;
  font-weight: 600;
}
.PostExtraInfo {
  padding-left: 48px+16px;
}
</style>
