<template>
  <n-card>
    <template #header
      ><n-space
        ><n-avatar round :src="userData.avatar_url" />
        <div>{{ userData.username }}</div></n-space
      ></template
    >
    <div v-html="data.content"></div>
    <template #footer>
      <n-button>评论</n-button>
    </template>
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

const props = defineProps({
  //子组件接收父组件传递过来的值
  data: {
    type: Object,
  },
});
const { data } = toRefs(props);

//console.log(data.value);

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

////组件挂载前获取数据
onBeforeMount(() => {
  getCommentUser(data.value.user_id);
});
</script>

<style lang="less"></style>
