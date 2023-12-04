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
import { onBeforeUnmount, ref, shallowRef, onMounted, defineEmits } from "vue";
import { Editor, Toolbar } from "@wangeditor/editor-for-vue";
import { Boot } from "@wangeditor/editor";
//import { IButtonMenu, IDomEditor } from "@wangeditor/editor";
// 编辑器实例，必须用 shallowRef
const editorRef = shallowRef();

// 内容 HTML
const valueHtml = ref("");

const status = ref("zh");

class AutoDetectLangMenu {
  constructor() {
    this.title = "自动检查语言"; // 自定义菜单标题
    // this.iconSvg = '<svg>...</svg>' // 可选
    this.tag = "button";
  }

  getValue(editor) {
    // JS 语法
    return editor.getText(); //获取编辑器内容
  }
  isActive(editor) {
    // JS 语法
    return false;
  }
  isDisabled(editor) {
    // JS 语法
    return false;
  }
  exec(editor, value) {
    // JS 语法
    if (this.isDisabled(editor)) return;
  }
}

//中译英
class ChineseToEnglishMenu {
  constructor() {
    this.title = "中文"; // 自定义菜单标题
    // this.iconSvg = '<svg>...</svg>' // 可选
    this.tag = "button";
  }

  getValue(editor) {
    // JS 语法
    return editor.getText(); //获取编辑器内容
  }
  isActive(editor) {
    // JS 语法
    return false;
  }
  isDisabled(editor) {
    // JS 语法
    return false;
  }
  exec(editor, value) {
    // JS 语法
    if (this.isDisabled(editor)) return;
    status.value = "zh";
    //editor.insertText(value); // value 即 this.value(editor) 的返回值
  }
}

//英译中
class EnglishToChineseMenu {
  constructor() {
    this.title = "英文"; // 自定义菜单标题
    // this.iconSvg = '<svg>...</svg>' // 可选
    this.tag = "button";
  }

  getValue(editor) {
    // JS 语法
    return "";
  }
  isActive(editor) {
    // JS 语法
    return false;
  }
  isDisabled(editor) {
    // JS 语法
    return false;
  }
  exec(editor, value) {
    // JS 语法
    if (this.isDisabled(editor)) return;
    status.value = "en";
  }
}

const AutoDetectLangMenuConf = {
  key: "autodetectLang", // 定义 menu key ：要保证唯一、不重复（重要）
  factory() {
    return new AutoDetectLangMenu(); // 把 `YourMenuClass` 替换为你菜单的 class
  },
};

const ChineseToEnglishMenuConf = {
  key: "chineseToEnglish", // 定义 menu key ：要保证唯一、不重复（重要）
  factory() {
    return new ChineseToEnglishMenu(); // 把 `YourMenuClass` 替换为你菜单的 class
  },
};

const EnglishToChineseMenuConf = {
  key: "englishToChinese", // 定义 menu key ：要保证唯一、不重复（重要）
  factory() {
    return new EnglishToChineseMenu(); // 把 `YourMenuClass` 替换为你菜单的 class
  },
};

Boot.registerMenu(AutoDetectLangMenuConf);
Boot.registerMenu(ChineseToEnglishMenuConf);
Boot.registerMenu(EnglishToChineseMenuConf);

const toolbarConfig = {
  toolbarKeys: [],
};

toolbarConfig.insertKeys = {
  index: 0, // 插入的位置，基于当前的 toolbarKeys
  keys: ["autodetectLang", "chineseToEnglish", "englishToChinese"], // 要插入的菜单 key
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
};

const mode = "default";

// 通过 emit 事件，把 editor 实例传递给父组件
const emit = defineEmits(["toFather"]);
const toFather = (editor) => {
  const content = editor.getText();
  let param = {
    content: content,
    status: status.value,
  };
  emit("toFather", param);
};
</script>
