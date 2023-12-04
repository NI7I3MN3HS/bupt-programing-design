<template>
  <v-md-preview-html
    :html="PHtml.toPreview"
    preview-class="github-markdown-body"
  ></v-md-preview-html>
</template>
<script setup>
import VMdPreviewHtml from "@kangc/v-md-editor/lib/preview-html";
import "@kangc/v-md-editor/lib/style/preview-html.css";
import { ref } from "vue";

// 引入使用主题的样式
import "@kangc/v-md-editor/lib/theme/style/github.css";

const PHtml = defineProps({
  toPreview: {
    type: String,
    default:""
  },
});
</script>

<style scoped></style>
