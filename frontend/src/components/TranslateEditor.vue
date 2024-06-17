<template>
  <Toolbar
    style="border-bottom: 1px solid #ccc"
    :editor="editorRef"
    :defaultConfig="toolbarConfig"
    :mode="mode"
  />
  <Editor
    style="height: 500px; overflow-y: hidden"
    v-model="valueHtml"
    :defaultConfig="editorConfig"
    :mode="mode"
    @onCreated="handleCreated"
    @onChange="toFather"
  />
</template>

<script setup>
import "@wangeditor/editor/dist/css/style.css"; // 引入 css
import { onBeforeUnmount, ref, shallowRef, defineEmits } from "vue";
import { Editor, Toolbar } from "@wangeditor/editor-for-vue";
import { Boot } from "@wangeditor/editor";

// 编辑器实例，必须用 shallowRef
const editorRef = shallowRef();

// 内容 HTML
const valueHtml = ref("");
const status = ref("zh"); // 默认为中文输入
const type = ref("trans"); // 默认为翻译模式
const activeButton = ref("chineseToEnglish");

class AutoDetectLangMenu {
  constructor() {
    this.title = "自动检查语言"; // 自定义菜单标题
    this.tag = "button";
  }
  getValue(editor) {
    return editor.getText(); //获取编辑器内容
  }
  isActive(editor) {
    return false;
  }
  isDisabled(editor) {
    return false;
  }
  exec(editor, value) {
    if (this.isDisabled(editor)) return;
  }
}

//中译英
class ChineseToEnglishMenu {
  constructor() {
    this.title = "中文";
    this.tag = "button";
  }
  getValue(editor) {
    return editor.getText();
  }
  isActive(editor) {
    return status.value === "zh" && type.value === "trans";
  }
  isDisabled(editor) {
    return false;
  }
  exec(editor, value) {
    if (this.isDisabled(editor)) return;
    status.value = "zh";
    type.value = "trans";
    activeButton.value = "chineseToEnglish";
    emitToFather();
  }
}

//英译中
class EnglishToChineseMenu {
  constructor() {
    this.title = "英文";
    this.tag = "button";
  }
  getValue(editor) {
    return editor.getText();
  }
  isActive(editor) {
    return status.value === "en" && type.value === "trans";
  }
  isDisabled(editor) {
    return false;
  }
  exec(editor, value) {
    if (this.isDisabled(editor)) return;
    status.value = "en";
    type.value = "trans";
    activeButton.value = "englishToChinese";
    emitToFather();
  }
}

class AcademicPaperMenu {
  constructor() {
    this.title = "学术论文翻译"; // 自定义菜单标题
    this.tag = "button";
  }
  getValue(editor) {
    return editor.getText(); //获取编辑器内容
  }
  isActive(editor) {
    return type.value === "academic_paper";
  }
  isDisabled(editor) {
    return false;
  }
  exec(editor, value) {
    if (this.isDisabled(editor)) return;
    status.value = "zh"; // 学术论文翻译对应中文输入
    type.value = "academic_paper";
    activeButton.value = "academicPaper";
    emitToFather();
  }
}

class WriteMenu {
  constructor() {
    this.title = "写作润色"; // 自定义菜单标题
    this.tag = "button";
  }
  getValue(editor) {
    return editor.getText(); //获取编辑器内容
  }
  isActive(editor) {
    return type.value === "write";
  }
  isDisabled(editor) {
    return false;
  }
  exec(editor, value) {
    if (this.isDisabled(editor)) return;
    status.value = "en"; // 写作润色对应英文输入
    type.value = "write";
    activeButton.value = "write";
    emitToFather();
  }
}

class WordMenu {
  constructor() {
    this.title = "单词联想"; // 自定义菜单标题
    this.tag = "button";
  }
  getValue(editor) {
    return editor.getText(); //获取编辑器内容
  }
  isActive(editor) {
    return type.value === "word";
  }
  isDisabled(editor) {
    return false;
  }
  exec(editor, value) {
    if (this.isDisabled(editor)) return;
    status.value = "en"; // 单词联想对应英文输入
    type.value = "word";
    activeButton.value = "word";
    emitToFather();
  }
}

const AutoDetectLangMenuConf = {
  key: "autodetectLang",
  factory() {
    return new AutoDetectLangMenu();
  },
};

const ChineseToEnglishMenuConf = {
  key: "chineseToEnglish",
  factory() {
    return new ChineseToEnglishMenu();
  },
};

const EnglishToChineseMenuConf = {
  key: "englishToChinese",
  factory() {
    return new EnglishToChineseMenu();
  },
};

const AcademicPaperMenuConf = {
  key: "academicPaper",
  factory() {
    return new AcademicPaperMenu();
  },
};

const WriteMenuConf = {
  key: "write",
  factory() {
    return new WriteMenu();
  },
};

const WordMenuConf = {
  key: "word",
  factory() {
    return new WordMenu();
  },
};

Boot.registerMenu(AutoDetectLangMenuConf);
Boot.registerMenu(ChineseToEnglishMenuConf);
Boot.registerMenu(EnglishToChineseMenuConf);
Boot.registerMenu(AcademicPaperMenuConf);
Boot.registerMenu(WriteMenuConf);
Boot.registerMenu(WordMenuConf);

const toolbarConfig = {
  toolbarKeys: ["autodetectLang", "chineseToEnglish", "englishToChinese", "academicPaper", "write", "word"],
};

const editorConfig = { placeholder: "请输入内容..." };

// 组件销毁时，也及时销毁编辑器
onBeforeUnmount(() => {
  const editor = editorRef.value;
  if (editor == null) return;
  editor.destroy();
});

const handleCreated = (editor) => {
  editorRef.value = editor; // 记录 editor 实例，重要！
  status.value = "zh";
  type.value = "trans";
};

const emit = defineEmits(["toFather"]);
const emitToFather = () => {
  const content = editorRef.value.getText();
  let param = {
    content: content,
    status: status.value,
    type: type.value,
  };
  emit("toFather", param);
};

const mode = "default";
</script>

<style scoped>
.toolbar-button-active {
  background-color: #8a8a8a; /* 激活按钮背景色 */
}
</style>
