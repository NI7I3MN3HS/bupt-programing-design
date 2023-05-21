<template>
  <n-card header-style="padding:20px 24px 10px 24px">
    <template #header
      ><n-space
        ><n-avatar round :src="userData.avatar_url" :size="40" />
        <div style="font-weight: 600; font-size: 14px">
          {{ userData.username }}
        </div></n-space
      ></template
    >
    <n-space vertical>
      <!--评论区内容-->
      <div class="CommentContent" v-html="data.content"></div>
      <!--评论区操作-->
      <div class="CommentAction">
        <n-space align="center">
          <n-button text color="black" @click="toSecondaryComment(0)">
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
          <n-button text
            ><template #icon
              ><n-icon>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  xmlns:xlink="http://www.w3.org/1999/xlink"
                  viewBox="0 0 1024 1024"
                >
                  <path
                    d="M885.9 533.7c16.8-22.2 26.1-49.4 26.1-77.7c0-44.9-25.1-87.4-65.5-111.1a67.67 67.67 0 0 0-34.3-9.3H572.4l6-122.9c1.4-29.7-9.1-57.9-29.5-79.4A106.62 106.62 0 0 0 471 99.9c-52 0-98 35-111.8 85.1l-85.9 311H144c-17.7 0-32 14.3-32 32v364c0 17.7 14.3 32 32 32h601.3c9.2 0 18.2-1.8 26.5-5.4c47.6-20.3 78.3-66.8 78.3-118.4c0-12.6-1.8-25-5.4-37c16.8-22.2 26.1-49.4 26.1-77.7c0-12.6-1.8-25-5.4-37c16.8-22.2 26.1-49.4 26.1-77.7c-.2-12.6-2-25.1-5.6-37.1zM184 852V568h81v284h-81zm636.4-353l-21.9 19l13.9 25.4a56.2 56.2 0 0 1 6.9 27.3c0 16.5-7.2 32.2-19.6 43l-21.9 19l13.9 25.4a56.2 56.2 0 0 1 6.9 27.3c0 16.5-7.2 32.2-19.6 43l-21.9 19l13.9 25.4a56.2 56.2 0 0 1 6.9 27.3c0 22.4-13.2 42.6-33.6 51.8H329V564.8l99.5-360.5a44.1 44.1 0 0 1 42.2-32.3c7.6 0 15.1 2.2 21.1 6.7c9.9 7.4 15.2 18.6 14.6 30.5l-9.6 198.4h314.4C829 418.5 840 436.9 840 456c0 16.5-7.2 32.1-19.6 43z"
                    fill="currentColor"
                  ></path>
                </svg> </n-icon></template
          ></n-button>
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

const router = useRouter();
const route = useRoute();

const authStore = useAuthStore();

const showSecondaryCommentInput = ref(false); //二级评论输入框是否显示

const comment_comment = ref([]); //二级评论

const reply_id = ref(0); //回复的评论id

//获取二级评论
function getSecondaryComment(comment_id) {
  axios
    .get(`/comment/reply/${comment_id}`)
    .then((res) => {
      comment_comment.value = res.data;
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

console.log(data.value);

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
    .get(`/comment/${comment_id}/like/count`)
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
