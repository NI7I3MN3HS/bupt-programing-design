<template>
  <div style="border: 1px solid #ccc">
    <Toolbar
      style="border-bottom: 1px solid #ccc"
      :editor="editorRef"
      :defaultConfig="toolbarConfig"
      :mode="mode"
    />
    <Editor
      style="height: 6ch; overflow-y: hidden"
      v-model="commentvalueHtml"
      :defaultConfig="editorConfig"
      :mode="mode"
      @onCreated="handleCreated"
    />
  </div>
</template>

<script setup>
import "@wangeditor/editor/dist/css/style.css"; // 引入 css
import { onBeforeUnmount, ref, shallowRef, onMounted, defineExpose } from "vue";
import { Editor, Toolbar } from "@wangeditor/editor-for-vue";

const editorRef = shallowRef();

// 内容 HTML
const commentvalueHtml = ref("");

//暴露commentvalueHtml给父组件使用
defineExpose({ commentvalueHtml });

const toolbarConfig = { toolbarKeys: ["emotion", "codeBlock"] };
const editorConfig = {
  placeholder: "评论千万条，友善第一条",
};

// 组件销毁时，也及时销毁编辑器
onBeforeUnmount(() => {
  const editor = editorRef.value;
  if (editor == null) return;
  editor.destroy();
});

const handleCreated = (editor) => {
  editorRef.value = editor; // 记录 editor 实例，重要！
};

const mode = "simple"; // 或 'simple'
</script>

<style scoped></style>
