<template>
  <n-space vertical>
    <div>占个位置</div>
    <CommentEditor ref="comment_input" />
    <n-button @click="CreateSecondaryComment">回复</n-button>
  </n-space>
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
  defineEmits,
  computed,
} from "vue";
import useAuthStore from "../stores/modules/AuthStore";
import useUserStore from "../stores/modules/UserStore";
import usePostStore from "../stores/modules/PostStore";
import { useRouter, useRoute } from "vue-router";
import axios from "axios";
import CommentEditor from "./CommentEditor.vue";

const comment_input = ref(null); //评论输入框

const router = useRouter();
const route = useRoute();

const authStore = useAuthStore();
const userStore = useUserStore();
const postStore = usePostStore();

const props = defineProps({
  //子组件接收父组件传递过来的值
  parent_id: {
    type: Number,
  },
  reply_id: {
    type: Number,
    default: 0,
  },
});
const { parent_id, reply_id } = toRefs(props);

const emit = defineEmits(["RefreshSecondaryComment"]); //定义子组件向父组件传递的事件

//定义axios请求头
const UserClient = axios.create({
  //baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
  },
});

//创建二级评论
function CreateSecondaryComment() {
  console.log("创建二级评论");
  if (authStore.is_Authenticated) {
    //后期改一下路径
    UserClient.post("/comment/create", {
      content: comment_input.value.commentvalueHtml,
      post_id: postStore.post_id,
      parent_id: parent_id.value,
      reply_user_id: reply_id.value,
    })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
    comment_input.value.commentvalueHtml = ""; //清空评论框
    emit("RefreshSecondaryComment"); //触发父组件的事件
  } else {
    alert("请先登录");
    router.push("/loginandregister");
  }
}
</script>
