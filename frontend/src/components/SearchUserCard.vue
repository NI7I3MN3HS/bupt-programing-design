<template>
  <div>
    <n-card>
      <n-space align="center" justify="space-between">
        <div @click="toAuthorProfile" style="cursor: pointer">
          <n-space>
            <n-avatar :size="50" round :src="userData.avatar_url" />
            <div>
              <div class="UserName">{{ userData.username }}</div>
              <div>{{ userData.introduction }}</div>
            </div></n-space
          >
        </div>
        <n-button
          v-if="is_followed && userStore.id != data.id"
          @click="DeleteFollow"
          >取消关注</n-button
        >
        <n-button
          v-if="!is_followed && userStore.id != data.id"
          @click="CreateFollow"
          >关注</n-button
        >
      </n-space>
    </n-card>
  </div>
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
import useAuthStore from "@/stores/modules/AuthStore";
import useUserStore from "@/stores/modules/UserStore";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const userStore = useUserStore();

//获取路由
const router = useRouter();

const props = defineProps({
  //子组件接收父组件传递过来的值
  data: {
    type: Object,
  },
});
const { data } = toRefs(props);

console.log(data.value);

const userData = ref({});

const is_followed = ref();

//获取当前用户的关注用户信息
function getFollowedUser(user_id) {
  axios
    .get(`/user/${user_id}`)
    .then((response) => {
      userData.value = response.data;
      console.log(userData.value);
    })
    .catch((error) => {
      console.error(error);
    });
  if (authStore.is_Authenticated == true) {
    UserClient.get(`/follow/is_followed/${data.value.id}`)
      .then((response) => {
        console.log(response.data);
        is_followed.value = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
  }
}

//组件更新后获取数据
watch(data, () => {
  getFollowedUser(data.value.id);
});

//组件挂载前获取数据
onBeforeMount(() => {
  getFollowedUser(data.value.id);
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

//创建关注
function CreateFollow() {
  if (authStore.is_Authenticated == false) {
    alert("请先登录");
  } else {
    UserClient.post(`/follow/create`, { followed_id: data.value.id })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
    is_followed.value = true;
  }
}
//取消关注
function DeleteFollow() {
  UserClient.delete(`/follow/delete`, {
    data: { followed_id: data.value.id },
  })
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.error(error);
    });
  is_followed.value = false;
}

//进入用户主页
function toAuthorProfile() {
  router.push(`/user/${data.value.id}`);
}
</script>
<style lang="less" scoped>
.n-card {
  width: 40vw;
  min-height: 10vh;
}
.UserName {
  font-size: 20px;
  font-weight: 600;
  color: #000;
}
</style>
