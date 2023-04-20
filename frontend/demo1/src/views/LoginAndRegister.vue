<template>
  <div class="body">
    <div class="func">
      <n-tabs
        class="card-tabs"
        default-value="signin"
        size="large"
        animated
        style="margin: 0 -4px"
        pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;"
      >
        <n-tab-pane name="signin" tab="登录">
          <n-form :model="LoginValue">
            <n-form-item-row label="用户名">
              <n-input v-model:value="LoginValue.username" />
            </n-form-item-row>
            <n-form-item-row label="密码">
              <n-input v-model:value="LoginValue.password" />
            </n-form-item-row>
          </n-form>
          <n-button type="primary" block secondary strong @click="clicklogin">
            登录
          </n-button>
        </n-tab-pane>
        <n-tab-pane name="signup" tab="注册">
          <n-form :model="RegisterValue">
            <n-form-item-row label="邮箱">
              <n-input v-model:value="RegisterValue.email" />
            </n-form-item-row>
            <n-button
              type="primary"
              block
              secondary
              strong
              @click="clicksendcode"
            >
              发送验证码
            </n-button>
            <n-form-item-row label="验证码">
              <n-input v-model:value="RegisterValue.verifycode" />
            </n-form-item-row>
            <n-form-item-row label="用户名">
              <n-input v-model:value="RegisterValue.username" />
            </n-form-item-row>
            <n-form-item-row label="密码">
              <n-input v-model:value="RegisterValue.password" />
            </n-form-item-row>
            <n-form-item-row label="重复密码">
              <n-input v-model:value="RegisterValue.password2" />
            </n-form-item-row>
          </n-form>
          <n-button
            type="primary"
            block
            secondary
            strong
            @click="clickregister"
          >
            注册
          </n-button>
        </n-tab-pane>
      </n-tabs>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { roundToNearestMinutes } from "date-fns";
import { reactive } from "vue";
import { useRoute, useRouter } from "vue-router";
const route = useRoute();
const router = useRouter();

export default {
  setup() {
    const LoginValue = reactive({
      username: "",
      password: "",
    });
    const RegisterValue = reactive({
      email: "",
      username: "",
      password: "",
      password2: "",
      verifycode: "",
    });
    return {
      LoginValue,
      clicklogin() {
        let form = new FormData();
        form.append("username", LoginValue.username);
        form.append("password", LoginValue.password);

        axios.post("/login/", form).then(() => {
          router.push("/profile");
        });
      },
      RegisterValue,
      clicksendcode() {
        axios.post("/register/VerifyCode", RegisterValue.email).then(() => {
          alert("发送成功");
        });
      },
      clickregister() {
        let form = new FormData();
        form.append("username", RegisterValue.username);
        form.append("password", RegisterValue.password);
        form.append("verifycode", RegisterValue.verifycode);
        axios.post("/register/", form).then(() => {
          alert("注册成功");
        });
      },
    };
  },
};
</script>

<style lang="less" scoped>
.body {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: #f0f2f5;
}
</style>
