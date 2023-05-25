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
        <WangEditor ref="Editor" v-if="EditorStatus == 0" />
        <Markdown ref="MarkdownEditor" v-if="EditorStatus == 1" />
        <n-divider />
        <n-button @click="CreatePost" color="#056de8">发布</n-button>
      </n-card>
    </div>
  </n-config-provider>
</template>

<script setup>
import WangEditor from "@/components/WangEditor.vue";
import Markdown from "@/components/Markdown.vue";
import { computed, ref } from "vue";
import useAuthStore from "../stores/modules/AuthStore";
import axios from "axios";
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const route = useRoute();

const authStore = useAuthStore();

const Title = ref();

//富文本编辑器
const Editor = ref();
//Markdown编辑器
const MarkdownEditor = ref();

//文章内容
const ContentInput = computed(() => {
  if (EditorStatus.value == 0) {
    return Editor.value.valueHtml;
  } else {
    return MarkdownEditor.value;
  }
});

//定义请求头
const UserClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
  },
});

//创建帖子
function CreatePost() {
  if (authStore.is_Authenticated) {
    //后期改一下路径
    UserClient.post("/post/create", {
      title: Title.value,
      content: ContentInput.value,
    })
      .then((response) => {
        //跳转到帖子详情页
        router.push(`/post/${response.data.id}`);
      })
      .catch((error) => {
        console.error(error);
      });
    //清空标题和内容
    Title.value = "";
    Editor.value = "";
    MarkdownEditor.value = "";
  } else {
    alert("请先登录");
  }
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
