<template>
  <div class="Container">
    <WangEditor />
    <div>这里是发布设置</div>
  </div>
</template>

<script setup>
import WangEditor from "@/components/WangEditor.vue";
</script>

<style lang="less" scoped>
.Container {
  min-height: calc(100vh);
}
</style>
