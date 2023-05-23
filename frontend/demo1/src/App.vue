<script setup>
import { RouterLink, RouterView } from "vue-router";
import { defineComponent } from "vue";
import { NThemeEditor } from "naive-ui";

defineComponent({
  components: {
    NThemeEditor,
  },
});
</script>

<template>
  <n-dialog-provider>
    <n-message-provider>
      <RouterView />
    </n-message-provider>
  </n-dialog-provider>
</template>

<style scoped></style>
