<template>
  <div class="body">
    <n-config-provider :theme-overrides="themeOverrides">
      <n-card
        ><div class="H1">找回密码</div>
        <div class="H2">验证码将会发送到你的邮箱</div>
        <n-form ref="formRef" :model="ResetValue" :rules="LoginRules">
          <n-form-item-row label="邮箱" path="">
            <n-input
              placeholder="请输入你的邮箱"
              ref="UsernameFormItemRef"
              @change=""
              v-model:value="ResetValue.data.email"
            />
          </n-form-item-row>
          <n-form-item-row v-if="is_sendcode" label="验证码"
            ><n-input placeholder="请输入验证码" />
            <n-button
              v-if="!is_resendcode"
              @click="ClickReSendCode"
              color="#056de8"
            >
              重新发送验证码
            </n-button>
            <n-button
              v-if="is_sendcode && is_resendcode"
              :disabled="SendcodeCountdown_active"
              @click="ClickSendCode"
              color="#056de8"
            >
              <n-countdown
                :duration="59000"
                :render="renderCountdown"
                :active="SendcodeCountdown_active"
                :on-finish="SendcodeCountdownFinish"
              />
            </n-button>
          </n-form-item-row>

          <n-form-item-row v-if="is_sendcode" label="密码"
            ><n-input placeholder="请输入密码" />
          </n-form-item-row>
        </n-form>
        <n-space justify="center">
          <n-button
            v-if="!is_sendcode"
            :disabled="!ResetValue.data.email"
            @click="ClickSendCode"
            color="#056de8"
          >
            下一步
          </n-button>
          <n-button v-if="is_sendcode" @click="ClickSendCode" color="#056de8">
            重设密码
          </n-button>
        </n-space>
      </n-card>
    </n-config-provider>
  </div>
</template>
<script setup>
import { reactive, ref } from "vue";

const themeOverrides = {
  Input: {
    borderFocus: "1px solid #8590a6",
    boxShadowFocus: "0 0 0 2px rgba(133, 144, 166, 0.2)",
    borderHover: "1px solid #8590a6",
    caretColor: "#8590a6FF",
  },
};
const formRef = ref(null);
const ResetValue = reactive({
  data: {
    email: "",
    extra_data: {
      code: "",
      password: "",
    },
  },
  detail: "",
});
const is_sendcode = ref(false); //是否已经发送过验证码
const is_resendcode = ref(true); //是否可以重发验证码
const SendcodeCountdown_active = ref(false); //倒计时是否激活

const renderCountdown = ({ seconds }) => {
  return `${String(seconds).padStart(2)}秒后可以重发`;
}; //倒计时渲染函数
function SendcodeCountdownFinish() {
  SendcodeCountdown_active.value = false;
  is_resendcode.value = false;
} //倒计时结束函数
function ClickSendCode() {
  SendcodeCountdown_active.value = true;
  is_sendcode.value = true;
}
function ClickReSendCode() {
  SendcodeCountdown_active.value = true;
  is_resendcode.value = true;
}
</script>
<style scoped lang="less">
.body {
  width: 50%;
  margin: 0 auto;
  margin-top: calc(50vh - 200px);
}
.H1 {
  font-size: 30px;
  font-weight: 700;
  color: #000;
  text-align: center;
}
.H2 {
  font-size: 14px;
  text-align: center;
  color: #8590a6;
}
</style>
