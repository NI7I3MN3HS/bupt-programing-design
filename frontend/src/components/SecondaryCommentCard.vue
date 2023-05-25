<template>
  <n-card
    :bordered="false"
    header-style="padding:0 0 10px 0"
    content-style="padding: 0 0"
  >
    <template #header
      ><n-space>
        <n-avatar
          round
          :src="userData.avatar_url"
          :size="40"
          @click="toAuthorProfile"
          style="cursor: pointer"
        />
        <n-space vertical :size="0">
          <div
            style="font-size: 14px; font-weight: 600; cursor: pointer"
            @click="toAuthorProfile"
          >
            {{ userData.username }}
          </div>
          <div style="font-size: 12px; color: #c7ccda; font-weight: 400">
            {{ formattedDate }}
          </div>
        </n-space>

        <div v-if="data.reply_user_id != 0">
          <n-space
            ><div style="font-size: 14px; color: #8e8787">回复</div>
            <!--
            <n-avatar round :src="replyUserData.avatar_url" :size="40" />
          -->
            <div style="font-size: 14px; font-weight: 600">
              {{ replyUserData.username }}
            </div></n-space
          >
        </div>
      </n-space>
    </template>
    <n-space vertical>
      <div class="CommentContent" v-html="data.content"></div>
      <div class="CommentAction">
        <n-space align="center">
          <n-button text color="black" @click="toSecondaryComment" block>
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
                  </g></svg></n-icon></template
          ></n-button>

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
  defineExpose,
  computed,
  defineEmits,
} from "vue";
import axios from "axios";
import useAuthStore from "../stores/modules/AuthStore";
import {
  parseISO,
  format,
  sub,
  differenceInMinutes,
  differenceInHours,
  differenceInDays,
  addDays,
} from "date-fns";
import { useRouter } from "vue-router";

const router = useRouter();

const authStore = useAuthStore();

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

const props = defineProps({
  //子组件接收父组件传递过来的值
  data: {
    type: Object,
  },
});
const { data } = toRefs(props);

//调用父组件的方法
const emits = defineEmits(["toSecondaryComment"]);

function toSecondaryComment() {
  emits("toSecondaryComment", data.value.user_id);
}

//定义axios请求头
const UserClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
  },
});
//获取当前评论的用户信息
const userData = ref({});
//获取当前评论回复的用户信息
const replyUserData = ref({});

console.log(data.value);

//获取当前评论的用户信息
function getCommentUser(user_id) {
  axios
    .get(`/user/${user_id}`)
    .then((res) => {
      userData.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
  if (data.value.reply_user_id != 0) {
    axios
      .get(`/user/${data.value.reply_user_id}`)
      .then((res) => {
        replyUserData.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  }
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
  getLikeState(data.value.post_id, data.value.id);
  getLikeCount(data.value.id);
});

console.log(data.value);

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

//进入用户主页
function toAuthorProfile() {
  router.push(`/user/${data.value.user_id}`);
}
</script>

<style scoped lang="less">
.CommentContent {
  margin: 0 48px;
}
.CommentAction {
  margin: 1ch 48px;
}
</style>
