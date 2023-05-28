<template>
  <v-md-editor v-model="MarkdownText" height="400px"></v-md-editor>
</template>

<script setup>
import { ref, defineExpose, computed } from "vue";
import VMdEditor from "@kangc/v-md-editor/lib/codemirror-editor";
import "@kangc/v-md-editor/lib/style/codemirror-editor.css";
import githubTheme from "@kangc/v-md-editor/lib/theme/github.js";
import "@kangc/v-md-editor/lib/theme/style/github.css";

// highlightjs
import hljs from "highlight.js";
import MarkdownIt from "markdown-it";
// codemirror 编辑器的相关资源
import Codemirror from "codemirror";
// mode
import "codemirror/mode/markdown/markdown";
import "codemirror/mode/javascript/javascript";
import "codemirror/mode/css/css";
import "codemirror/mode/htmlmixed/htmlmixed";
import "codemirror/mode/vue/vue";
// edit
import "codemirror/addon/edit/closebrackets";
import "codemirror/addon/edit/closetag";
import "codemirror/addon/edit/matchbrackets";
// placeholder
import "codemirror/addon/display/placeholder";
// active-line
import "codemirror/addon/selection/active-line";
// scrollbar
import "codemirror/addon/scroll/simplescrollbars";
import "codemirror/addon/scroll/simplescrollbars.css";
// style
import "codemirror/lib/codemirror.css";

const md = MarkdownIt();

VMdEditor.Codemirror = Codemirror;
VMdEditor.use(githubTheme, {
  Hljs: hljs,
});

const MarkdownText = ref("");

//将markdown转换为html
const MarkdownToHtml = computed(() => {
  const result = md.render(MarkdownText.value);
  console.log(result);
  return result;
});

//暴露valueHtml给父组件使用
defineExpose({ MarkdownToHtml });
</script>

<style lang="less" scoped></style>
