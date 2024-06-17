<template>
  <div class="Container">
    <div class="Editor">
      <n-card>
        <TranslateEditor @toFather="GetContentAndStatus" />
        <n-divider />
        <n-button @click="toTranslate" color="#056de8">翻译</n-button>
      </n-card>
    </div>
    <div class="Preview">
      <n-card>
        <TranslatePreview :toPreview="toPreview" />
      </n-card>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useMessage } from "naive-ui";
import TranslateEditor from "@/components/TranslateEditor.vue";
import TranslatePreview from "@/components/TranslatePreview.vue";

const message = useMessage();
const content = ref("");
const status = ref("zh");
const type = ref("trans");
const toPreview = ref("");

const GetContentAndStatus = (val) => {
  console.log(val);
  content.value = val.content;
  status.value = val.status;
  type.value = val.type;
};

const handleWriteOrWordResponse = (data) => { // 处理文本，将建议分点进行换行
  // 将文本按照换行符分割成数组
  const lines = data.split(/\d+\./).filter(line => line.trim() !== '');
  // 拼接成带有标号的格式
  const formattedText = lines.map((line, index) => `${index + 1}. ${line.trim()}`).join('\n');
  return formattedText;
};

const toTranslate = () => {
  if (type.value === "trans") {
    if (status.value === "zh") {
      axios.post("/translate/chinese2english", {}, {
        params: { text: content.value }
      }).then((res) => {
        toPreview.value = res.data;
      }).catch((error) => {
        message.error("翻译失败: " + error.message);
      });
    } else if (status.value === "en") {
      axios.post("/translate/english2chinese", {}, {
        params: { text: content.value }
      }).then((res) => {
        toPreview.value = res.data;
      }).catch((error) => {
        message.error("翻译失败: " + error.message);
      });
    }
  } else if (type.value === "academic_paper") {
    axios.post("/translate/academic_paper", {}, {
      params: { text: content.value }
    }).then((res) => {
      toPreview.value = res.data;
    }).catch((error) => {
      message.error("翻译失败: " + error.message);
    });
  } else if (type.value === "write") {
    axios.post("/translate/write", {}, {
      params: { text: content.value }
    }).then((res) => {
      // const formattedText = handleWriteOrWordResponse(res.data);
      // toPreview.value = formattedText;
      toPreview.value = res.data;
    }).catch((error) => {
      message.error("润色失败: " + error.message);
    });
  } else if (type.value === "word") {
    axios.post("/translate/word", {}, {
      params: { word: content.value }
    }).then((res) => {
      // const formattedText = handleWriteOrWordResponse(res.data);
      // toPreview.value = formattedText;
      toPreview.value = res.data;
    }).catch((error) => {
      message.error("联想失败: " + error.message);
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
