<template>
  <v-md-preview-html
    :html="formattedPreview"
    preview-class="github-markdown-body"
  ></v-md-preview-html>
</template>

<script setup>
import VMdPreviewHtml from "@kangc/v-md-editor/lib/preview-html";
import "@kangc/v-md-editor/lib/style/preview-html.css";
import { ref, computed } from "vue";

// 引入使用主题的样式
import "@kangc/v-md-editor/lib/theme/style/github.css";

const PHtml = defineProps({
  toPreview: {
    type: String,
    default: ""
  }
});

// 处理换行符，将 \n 替换为 <br>
const formattedPreview = computed(() => {
  return PHtml.toPreview.replace(/\n/g, '<br>');
});
</script>

<style scoped></style>
