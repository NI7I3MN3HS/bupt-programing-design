<template>
  <n-result status="404" title="用户不存在" description="生活总归带点荒谬">
    <template #footer>
      <n-button color="#8590a6" @click="toIndex">找点乐子吧</n-button>
    </template>
  </n-result>
</template>

<script setup>
import { useRouter } from "vue-router";
const router = useRouter();

function toIndex() {
  router.push("/");
}
</script>
