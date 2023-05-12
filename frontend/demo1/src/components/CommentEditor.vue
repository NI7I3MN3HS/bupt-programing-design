<template>
  <n-space vertical>
    <div style="border: 1px solid #ccc">
      <Toolbar
        style="border-bottom: 1px solid #ccc"
        :editor="editorRef"
        :defaultConfig="toolbarConfig"
        :mode="mode"
      />
      <Editor
        style="height: 5ch; overflow-y: hidden; width: 60ch"
        v-model="valueHtml"
        :defaultConfig="editorConfig"
        :mode="mode"
        @onCreated="handleCreated"
      />
    </div>
    <n-button>评论</n-button>
  </n-space>
</template>

<script setup>
import "@wangeditor/editor/dist/css/style.css"; // 引入 css
import { onBeforeUnmount, ref, shallowRef, onMounted } from "vue";
import { Editor, Toolbar } from "@wangeditor/editor-for-vue";

const editorRef = shallowRef();
// 内容 HTML
const valueHtml = ref("");

const toolbarConfig = { toolbarKeys: ["emotion", "codeBlock"] };
const editorConfig = {
  placeholder: "评论千万条，友善第一条",
};

editorConfig.onFocus = () => {
  style = "height: 20ch; overflow-y: hidden; width: 60ch";
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
