<template>
  <v-md-preview-html
    :html="html"
    preview-class="github-markdown-body"
  ></v-md-preview-html>
</template>
<script setup>
import VMdPreviewHtml from "@kangc/v-md-editor/lib/preview-html";
import "@kangc/v-md-editor/lib/style/preview-html.css";
import { ref } from "vue";

// 引入使用主题的样式
import "@kangc/v-md-editor/lib/theme/style/github.css";

const html = ref("111");
</script>

<style scoped></style>
