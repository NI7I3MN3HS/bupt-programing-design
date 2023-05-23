<template>
  <n-card header-style="padding:20px 24px 10px 24px">
    <template #header
      ><n-space
        ><n-avatar round :src="userData.avatar_url" :size="40" />
        <n-space vertical :size="0">
          <div style="font-weight: 600; font-size: 14px">
            {{ userData.username }}
          </div>
          <div style="font-size: 12px; color: #c7ccda; font-weight: 400">
            {{ formattedDate }}
          </div>
        </n-space>
      </n-space></template
    >
    <n-space vertical>
      <!--评论区内容-->
      <div class="CommentContent" v-html="data.content"></div>
      <!--评论区操作-->
      <div class="CommentAction">
        <n-space align="center">
          <!--展开二级评论输入框-->
          <n-button text color="black" @click="toSecondaryComment(0)" block>
            <template #icon
              ><n-icon
                ><svg
                  xmlns="http://www.w3.org/2000/svg"
                  xmlns:xlink="http://www.w3.org/1999/xlink"
                  viewBox="0 0 16 16"
                >
                  <g fill="none">
                    <path
                      d="M1 4.5A2.5 2.5 0 0 1 3.5 2h9A2.5 2.5 0 0 1 15 4.5v5a2.5 2.5 0 0 1-2.5 2.5H8.688l-3.063 2.68A.98.98 0 0 1 4 13.942V12h-.5A2.5 2.5 0 0 1 1 9.5v-5zM3.5 3A1.5 1.5 0 0 0 2 4.5v5A1.5 1.5 0 0 0 3.5 11H5v2.898L8.312 11H12.5A1.5 1.5 0 0 0 14 9.5v-5A1.5 1.5 0 0 0 12.5 3h-9z"
                      fill="currentColor"
                    ></path>
                  </g></svg></n-icon></template></n-button
          >{{ SecondarycommentCount }}
          <!--点赞按钮-->
          <n-button
            text
            @click="CreatePostLike"
            v-if="likestate == false"
            block
          >
            <template #icon>
              <n-icon size="28">
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
            {{ likeCount }}
          </n-button>
          <!--取消点赞按钮-->
          <n-button text @click="DeletePostLike" v-if="likestate == true" block>
            <template #icon>
              <n-icon size="28">
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
            >{{ likeCount }}
          </n-button>
        </n-space>
      </div>
      <!--二级评论区-->
      <div class="SecondaryCommentZone">
        <n-space vertical>
          <div v-for="item in comment_comment">
            <SecondaryCommentCard
              :data="item"
              @toSecondaryComment="toSecondaryComment"
            />
          </div>
          <SecondaryCommentInput
            v-if="showSecondaryCommentInput"
            :parent_id="data.id"
            :reply_id="reply_id"
            @RefreshSecondaryComment="getSecondaryComment(data.id)"
          />
        </n-space>
      </div>
    </n-space>
  </n-card>
</template>

<script setup>
import {
  ref,
  reactive,
  defineComponent,
  watch,
  onBeforeMount,
  toRefs,
  defineProps,
  computed,
} from "vue";
import axios from "axios";
import useAuthStore from "../stores/modules/AuthStore";
import { useRouter, useRoute } from "vue-router";
import SecondaryCommentCard from "./SecondaryCommentCard.vue";
import SecondaryCommentInput from "./SecondaryCommentInput.vue";
import {
  parseISO,
  format,
  sub,
  differenceInMinutes,
  differenceInHours,
  differenceInDays,
  addDays,
} from "date-fns";

const router = useRouter();
const route = useRoute();

const authStore = useAuthStore();

const showSecondaryCommentInput = ref(false); //二级评论输入框是否显示

const comment_comment = ref([]); //二级评论

const reply_id = ref(0); //回复的评论id

const formattedDate = computed(() => {
  const now = new Date();
  const oneHourAgo = sub(now, { hours: 1 });
  const oneDayAgo = addDays(now, -1);
  const oneWeekAgo = addDays(now, -7);

  // 解析ISO格式的日期字符串
  const date = parseISO(data.value.create_time);

  if (date > oneHourAgo) {
    const minutesAgo = differenceInMinutes(now, date);
    return `${minutesAgo} 分钟前`;
  } else if (date > oneDayAgo) {
    const hoursAgo = differenceInHours(now, date);
    return `${hoursAgo} 小时前`;
  } else if (date > oneWeekAgo) {
    const daysAgo = differenceInDays(now, date);
    return `${daysAgo} 天前`;
  }

  // 超过一周，显示为 'yyyy-MM-dd HH:mm:ss' 格式
  return format(date, "yyyy-MM-dd HH:mm:ss");
});

//定义axios请求头
const UserClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
  },
});

const SecondarycommentCount = ref(0); //二级评论数

//获取二级评论
function getSecondaryComment(comment_id) {
  axios
    .get(`/comment/reply/${comment_id}`)
    .then((res) => {
      comment_comment.value = res.data;
      SecondarycommentCount.value = res.data.length;
    })
    .catch((err) => {
      console.log(err);
    });
}

const props = defineProps({
  //子组件接收父组件传递过来的值
  data: {
    type: Object,
  },
});
const { data } = toRefs(props);

//获取当前评论的用户信息
const userData = ref({});

function getCommentUser(user_id) {
  axios
    .get(`/user/${user_id}`)
    .then((res) => {
      userData.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
}

//获取当前评论的点赞数
const likeCount = ref(0);

function getLikeCount(comment_id) {
  axios
    .get(`/like/comment/${comment_id}`)
    .then((res) => {
      likeCount.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
}

////组件挂载前获取数据
onBeforeMount(() => {
  getCommentUser(data.value.user_id);
  getSecondaryComment(data.value.id);
  getLikeState(data.value.post_id, data.value.id);
  getLikeCount(data.value.id);
});

//跳转到二级评论框
function toSecondaryComment(val) {
  //如果用户已经登录
  if (authStore.is_Authenticated) {
    showSecondaryCommentInput.value = !showSecondaryCommentInput.value;
    if (showSecondaryCommentInput.value == true) {
      reply_id.value = val; //如果显示二级评论框，就把回复的评论id赋值给reply_id
    } else reply_id.value = 0; //否则就把reply_id清空
  } else {
    alert("请先登录");
  }
}

const likestate = ref(false); //点赞状态
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
//点赞
function CreatePostLike() {
  UserClient.post(`/like/create`, {
    post_id: data.value.post_id,
    comment_id: data.value.id,
  })
    .then((res) => {
      likestate.value = true;
      //点赞数加一
      likeCount.value++;
    })
    .catch((err) => {
      console.log(err);
    });
}
//取消点赞
function DeletePostLike() {
  UserClient.delete(`/like/delete`, {
    data: {
      post_id: data.value.post_id,
      comment_id: data.value.id,
    },
  })
    .then((res) => {
      likestate.value = false;
      //点赞数减一
      likeCount.value--;
    })
    .catch((err) => {
      console.log(err);
    });
}
</script>

<style scoped lang="less">
.CommentContent {
  margin: 0 48px;
}
.CommentAction {
  margin: 1ch 48px;
}
.SecondaryCommentZone {
  margin: 1ch 48px;
  max-width: calc(100% - 48px);
}
</style>
