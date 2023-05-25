<template>
  <n-avatar></n-avatar>
</template>

<script setup>
import { ref, reactive, getCurrentInstance } from "vue";
import { useRouter, useRoute } from "vue-router";
const router = useRouter();
const route = useRoute();
const { proxy } = getCurrentInstance();

const props = defineProps({
  userID: {
    type: Number,
  },
  addLink: {
    type: Boolean,
    default: true,
  },
});

const GoToUser = () => {
  if (props.addLink) {
    router.push({
      name: "User",
      params: {
        id: props.userID,
      },
    });
  }
};
</script>
