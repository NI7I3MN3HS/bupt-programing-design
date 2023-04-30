<template>
  <n-upload ref="uploadRef" action="#" :custom-request="myUpload">
    <n-button>点击选择文件</n-button>
  </n-upload>
</template>

<script setup>
const myUpload = (file) => {
  const formData = new FormData();
};
</script>

<style scoped></style>
