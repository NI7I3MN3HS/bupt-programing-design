<template>
  <div class="PageContainer">
    <n-result
      status="404"
      title="用户不存在"
      description="蓦然回首，那人却在灯火阑珊处"
      style="top: 5ch"
    >
      <template #footer>
        <n-button color="#8590a6" @click="toIndex">到别处看看</n-button>
      </template>
    </n-result>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
const router = useRouter();

function toIndex() {
  router.push("/");
}
</script>

<style lang="less">
.PageContainer {
  width: 100%;
  height: calc(100ch - 60px);
}
</style>
