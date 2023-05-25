<template>
  <n-card>
    <template #header>系统通知</template>
    {{ data.content }}
  </n-card>
</template>

<script setup>
import axios from "axios";
import { toRefs } from "vue";

const props = defineProps({
  //子组件接收父组件传递过来的值
  data: {
    type: Object,
  },
});
const { data } = toRefs(props);

console.log(data.value);
</script>
