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
        <TranslatePreview :toPreview="toPreview" />
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
const content = ref("");
const status = ref("");
const toPreview = ref("");

const GetContentAndStatus = (val) => {
  console.log(val);
  console.log(val.content);
  console.log(val.status);
  content.value = val.content;
  status.value = val.status;
};

const toTranslate = () => {
  if(status.value === "zh"){
    axios.post("/translate/chinese2english", {
    },
      {
        params: {
          text: content.value,
        },
      })
      .then((res) => {
      toPreview.value = res.data;
      });
  }

  else if(status.value === "en"){
    axios.post("/translate/english2chinese", {
    },
      {
        params: {
          text: content.value,
        },
      })
      .then((res) => {
      toPreview.value = res.data;
    });
  }

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
