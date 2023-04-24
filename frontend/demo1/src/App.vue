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
  <RouterView />
</template>

<style scoped></style>
