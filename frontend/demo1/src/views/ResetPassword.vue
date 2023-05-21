<template>
  <div class="Container">
    <div class="Content">
      <n-config-provider :theme-overrides="themeOverrides">
        <n-watermark
          content="我知道你很急，但是请先别急"
          cross
          fullscreen
          :font-size="16"
          :line-height="16"
          :width="384"
          :height="384"
          :x-offset="12"
          :y-offset="60"
          :rotate="-15"
          z-index="-1"
        />
        <n-card
          ><div class="H1">找回密码</div>
          <div class="H2">验证码将会发送到你的邮箱</div>
          <n-form ref="formRef" :model="ResetValue" :rules="ResetRules">
            <n-form-item-row label="邮箱" path="Email.email">
              <n-input
                :disabled="is_sendcode"
                @change="EmailInputChange"
                placeholder="请输入你的邮箱"
                ref="EmailFormItemRef"
                v-model:value="ResetValue.Email.email"
                ><template v-if="is_sendcode" #suffix>
                  <n-button text text-color="#056de8" @click="BackToInputEmail"
                    >修改</n-button
                  >
                </template></n-input
              >
            </n-form-item-row>
            <n-form-item-row
              v-if="is_sendcode"
              label="验证码"
              path="Extra_data.Code.code"
              ><n-input
                ref="CodeFormItemRef"
                @change="CodeInputChange"
                placeholder="请输入验证码"
                v-model:value="ResetValue.Extra_data.Code.code"
              />
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

            <n-form-item-row
              v-if="is_sendcode"
              label="密码"
              path="Extra_data.password.password"
              ><n-input
                type="password"
                show-password-on="click"
                @input="handlePasswordInput"
                placeholder="请输入密码"
                v-model:value="ResetValue.Extra_data.password.password"
              />
            </n-form-item-row>
            <n-form-item-row
              v-if="is_sendcode"
              label="确认密码"
              path="confirmpassword"
              ref="rPasswordFormItemRef"
              ><n-input
                type="password"
                show-password-on="click"
                placeholder="请再次输入密码"
                v-model:value="ResetValue.confirmpassword"
              />
            </n-form-item-row>
          </n-form>
          <n-space justify="center">
            <n-button
              v-if="!is_sendcode"
              :disabled="!ResetValue.Email.email"
              @click="ClickSendCode"
              color="#056de8"
            >
              下一步
            </n-button>
            <n-button
              v-if="is_sendcode"
              @click="ClickResetPassword"
              color="#056de8"
            >
              重设密码
            </n-button>
          </n-space>
        </n-card>
      </n-config-provider>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const route = useRoute();

const themeOverrides = {
  Input: {
    borderFocus: "1px solid #8590a6",
    boxShadowFocus: "0 0 0 2px rgba(133, 144, 166, 0.2)",
    borderHover: "1px solid #8590a6",
    caretColor: "#8590a6FF",
  },
}; //naive-ui主题样式覆盖
const formRef = ref(null); //表单ref
const ResetValue = reactive({
  Email: { email: "" },
  Extra_data: {
    Code: { code: "" },
    password: { password: "" },
  },
  detail: "",
  confirmpassword: "",
}); //重置密码表单数据
const is_sendcode = ref(false); //是否已经发送过验证码
const is_resendcode = ref(true); //是否可以重发验证码
const SendcodeCountdown_active = ref(false); //倒计时是否激活
const EmailFormItemRef = ref(null); //邮箱输入框的ref
const CodeFormItemRef = ref(null); //验证码输入框的ref
const rPasswordFormItemRef = ref(null); //重复密码表单的ref
const renderCountdown = ({ seconds }) => {
  return `${String(seconds).padStart(2)}秒后可以重发`;
}; //倒计时渲染函数

const ResetRules = {
  Email: {
    email: [
      {
        required: true,
        message: "请输入邮箱",
        trigger: ["blur", "input"],
      },
      {
        type: "email",
        message: "请输入正确的邮箱",
        trigger: ["blur", "input"],
      },
      {
        validator: EmailNotRegistered,
        message: "该邮箱尚未注册",
        trigger: "focus",
      },
    ],
  },
  Extra_data: {
    Code: {
      code: [
        {
          required: true,
          message: "请输入验证码",
          trigger: ["blur", "input"],
        },
        {
          validator: CodeError,
          message: "验证码错误",
          trigger: "focus",
        },
      ],
    },
    password: {
      password: [
        {
          required: true,
          validator(rule, value) {
            if (!value) {
              return new Error("密码不能为空");
            } else if (!/^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/.test(value)) {
              return new Error(
                "请输入正确的密码格式:至少8位,包含一个大写字母和一个数字"
              );
            }
            return true;
          },
          trigger: ["blur", "input"],
        },
      ],
    },
  },
  confirmpassword: [
    {
      required: true,
      message: "请再次输入密码",
      trigger: ["input", "blur"],
    },
    {
      validator: validatePasswordSame,
      message: "两次密码输入不一致",
      trigger: ["blur", "password-input"],
    },
  ],
};

//邮箱未注册验证函数
function EmailNotRegistered(rule, value) {
  return ResetValue.detail != "Email not registered";
}

//验证码错误验证函数
function CodeError(rule, value) {
  return ResetValue.detail != "Verification code error";
}

//两次密码输入是否一致验证函数
function validatePasswordSame(rule, value) {
  return value === ResetValue.Extra_data.password.password;
}

//重新输入密码时的验证
function handlePasswordInput() {
  if (ResetValue.Extra_data.password.password) {
    rPasswordFormItemRef.value?.validate({ trigger: "password-input" });
  }
}

//邮箱输入框内容改变时清空错误信息
function EmailInputChange() {
  ResetValue.detail = "";
}

//验证码输入框内容改变时清空错误信息
function CodeInputChange() {
  ResetValue.detail = "";
}

//倒计时结束函数
function SendcodeCountdownFinish() {
  SendcodeCountdown_active.value = false;
  is_resendcode.value = false;
}

//发送邮箱验证码
function ClickSendCode() {
  formRef.value?.validate((errors) => {
    if (!errors) {
      axios
        .post("/register/find_password/VerifyCode", ResetValue.Email)
        .then((res) => {
          is_sendcode.value = true;
          SendcodeCountdown_active.value = true;
          alert("验证码已发送");
        })
        .catch((err) => {
          ResetValue.detail = err.response.data.detail;
          EmailFormItemRef.value?.focus();
        });
    }
  });
}

//重新发送邮箱验证码
function ClickReSendCode() {
  SendcodeCountdown_active.value = true;
  is_resendcode.value = true;
  axios
    .post("/register/find_password/VerifyCode", ResetValue.Email)
    .then((res) => {
      alert("验证码已发送");
    });
}

//重设密码
function ClickResetPassword() {
  formRef.value?.validate((errors) => {
    if (!errors) {
      axios
        .post("/register/find_password", ResetValue.Extra_data)
        .then((res) => {
          alert("重设密码成功");
          router.push("/loginandregister");
        })
        .catch((err) => {
          ResetValue.detail = err.response.data.detail;
          CodeFormItemRef.value?.focus();
        });
    }
  });
}

//修改邮箱
function BackToInputEmail() {
  is_sendcode.value = false;
  is_resendcode.value = true;
  SendcodeCountdown_active.value = false;
}
</script>
<style scoped lang="less">
.Container {
  min-height: calc(100vh);
}
.Content {
  top: 15%;
  width: 30%;
  position: absolute;
  left: 35%;
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
