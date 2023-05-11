<template>
  <n-config-provider :theme-overrides="themeOverrides">
    <div class="Container">
      <n-card>
        <!--这里设置文章标题-->
        <n-input
          size:large
          v-model:value="Title"
          type="text"
          :bordered="false"
          placeholder="给文章起个标题"
          minlength="1"
          maxlength="64"
          style="font-size: 30px"
          :input-props="{
            style: { fontWeight: 'bold' },
          }"
        />
        <n-divider />
        <n-space justify="end">
          <n-button text color="#056de8" @click="SwitchEditor">{{
            SwitchEditorText
          }}</n-button>
        </n-space>
        <!-- 这里是正文内容 -->
        <WangEditor v-if="EditorStatus == 0" />
        <Markdown v-if="EditorStatus == 1" />
        <n-divider />
        <n-button @click="Post" color="#056de8">发布</n-button>
      </n-card>
    </div>
  </n-config-provider>
</template>

<script setup>
import WangEditor from "@/components/WangEditor.vue";
import Markdown from "@/components/Markdown.vue";
import { ref } from "vue";
import { storeToRefs } from "pinia";
import usePostStore from "../stores/modules/PostStore";

const postStore = usePostStore();

const { post_title } = storeToRefs(postStore);

const Title = ref(post_title);

function Post() {
  postStore.CreatePost();
}

const EditorStatus = ref(0);
const SwitchEditorText = ref("切换到Markdown编辑器");

function SwitchEditor() {
  if (EditorStatus.value == 0) {
    EditorStatus.value = 1;
    SwitchEditorText.value = "切换到富文本编辑器";
  } else {
    EditorStatus.value = 0;
    SwitchEditorText.value = "切换到Markdown编辑器";
  }
}

const themeOverrides = {
  Input: {
    borderFocus: "1px solid #8590a6",
    boxShadowFocus: "0 0 0 2px rgba(133, 144, 166, 0.2)",
    borderHover: "1px solid #8590a6",
    caretColor: "#8590A6FF",
  },
};
</script>

<style lang="less" scoped>
.Container {
  min-height: calc(100vh);
}
</style>
