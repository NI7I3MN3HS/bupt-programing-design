<template>
  <div class="Container">
    <div class="Editor">
      <n-card>
        <!--这里设置文章标题-->
        <!-- 这里是正文内容 -->
        <TranslateEditor @toFather="GetContentAndStatus" />
        <n-divider />
        <n-button @click="toTranslate" color="#056de8">翻译</n-button>
      </n-card>
    </div>
    <div class="Preview">
      <n-card>
        <!-- 这里是渲染内容-->
        <TranslatePreview ref="TPreview" />
      </n-card>
    </div>
  </div>
</template>
<script setup>
import axios from "axios";
import { useRouter } from "vue-router";
import TranslatePreview from "@/components/TranslatePreview.vue";
import TranslateEditor from "@/components/TranslateEditor.vue";
import { computed, ref } from "vue";
import { useMessage } from "naive-ui";

const router = useRouter();
const message = useMessage();

const GetContentAndStatus = (val) => {
  console.log(val);
  console.log(val.content);
  console.log(val.status);
};

const toTranslate = () => {
  /*
  const editor = MarkdownEditor.value;
  if (editor == null) return;
  const html = editor.getHtml();
  const text = editor.getText();
  const title = text.split("\n")[0];
  const content = text.split("\n").slice(1).join("\n");
  axios
    .post("/api/translate", {
      title,
      content,
    })
    .then((res) => {
      if (res.data.code === 200) {
        message.success("翻译成功");
        在这里把获取到的后端返回的数据传给TranslatePreview组件
        router.push(`/article/${res.data.data.id}`);
      } else {
        message.error("翻译失败");
      }
    });*/
};
</script>
<style scoped>
.Editor {
  width: 50%;
  float: left;
  padding: 10px;
}
.Preview {
  width: 50%;
  float: right;
  padding: 10px;
}
.Container {
  min-height: 100vh;
}

.n-card {
  min-height: calc(100vh - 144px);
}
</style>
