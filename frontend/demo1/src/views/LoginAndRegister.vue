<template>
  <n-config-provider :theme-overrides="themeOverrides">
    <div class="body">
      <div class="BackGround" />

      <div class="SiderColumn" />
      <div class="MainColumn">
        <!--注册-->
        <div v-if="PageStatus == 1" class="ShowLRegister">
          <n-card content-style="padding:48px 48px 48px 48px;">
            <n-space vertical>
              <div class="H1">创建一个账户</div>
              <div class="H2">
                <span>已有账户？</span
                ><span
                  ><n-button
                    text
                    @click="SwitchToLoginAndRegister()"
                    text-color="#056de8"
                    >登录</n-button
                  ></span
                >
              </div></n-space
            >

            <n-form ref="formRef" :model="Email" :rules="MailRules">
              <n-form-item-row label="邮箱" path="data.email">
                <n-input
                  :disabled="!is_input_email"
                  ref="EmailFormItemRef"
                  @change="EmailInputChange"
                  v-model:value="Email.data.email"
                  placeholder="请输入邮箱"
                />
              </n-form-item-row>
            </n-form>

            <n-form ref="formRef" :model="RegisterValue" :rules="RegisterRules">
              <n-form-item-row label="验证码" path="data.Code.code">
                <n-input
                  @change="RegisterInputChange"
                  :disabled="!Email.data.email"
                  v-model:value="RegisterValue.data.Code.code"
                  ref="CodeFormItemRef"
                  placeholder="请输入验证码"
                />
                <n-button
                  v-if="!is_sendcode"
                  :disabled="!Email.data.email"
                  type="primary"
                  strong
                  @click="clicksendcode"
                  color="#056de8"
                >
                  获取验证码
                </n-button>
                <n-button
                  v-if="is_sendcode"
                  :disabled="SendcodeCountdown_active"
                  type="primary"
                  strong
                  @click="clicksendcode"
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
              <n-form-item-row label="用户名" path="data.user.username">
                <n-input
                  @change="RegisterInputChange"
                  v-model:value="RegisterValue.data.user.username"
                  ref="UsernameFormItemRef"
                  placeholder="请输入用户名"
                />
              </n-form-item-row>
              <n-form-item-row label="密码" path="data.user.password">
                <n-input
                  type="password"
                  show-password-on="click"
                  placeholder="请输入密码"
                  v-model:value="RegisterValue.data.user.password"
                  @input="handlePasswordInput"
                />
              </n-form-item-row>
              <n-form-item-row
                label="确认密码"
                path="confirmpassword"
                ref="rPasswordFormItemRef"
              >
                <n-input
                  type="password"
                  show-password-on="click"
                  placeholder="请再次输入密码"
                  v-model:value="RegisterValue.confirmpassword"
                />
              </n-form-item-row>
            </n-form>
            <n-space justify="center">
              <n-button color="#056de8" @click="clickregister">
                创建你的账户</n-button
              ></n-space
            >
          </n-card>
        </div>
        <!--登录-->
        <div v-if="PageStatus == 0" class="ShowLogin">
          <n-card content-style="padding:144px 64px 144px 64px;">
            <n-space vertical justify="center" :size="30">
              <n-space vertical>
                <div class="H1">登录你的账户</div>
                <div class="H2">
                  <span>未有账户？</span
                  ><span
                    ><n-button
                      text
                      @click="SwitchToLoginAndRegister()"
                      text-color="#056de8"
                      >注册</n-button
                    ></span
                  >
                </div>
              </n-space>
              <n-form ref="formRef" :model="LoginValue" :rules="LoginRules">
                <n-form-item-row label="用户名" path="">
                  <n-input
                    placeholder="请输入用户名或邮箱"
                    ref="UsernameFormItemRef"
                    @change=""
                    v-model:value="LoginValue.username"
                  />
                </n-form-item-row>
                <n-form-item-row label="密码">
                  <n-input
                    v-model:value="LoginValue.password"
                    placeholder="请输入密码"
                    type="password"
                    show-password-on="click"
                  />
                </n-form-item-row>
                <n-space justify="space-between">
                  <n-checkbox v-model:checked="value" text-color="#8590a6">
                    记住我
                  </n-checkbox>
                  <n-button
                    text
                    text-color="#8590a6"
                    @click="ClickToResetPassword()"
                    >忘记密码？</n-button
                  >
                </n-space>
              </n-form>
              <n-space justify="center">
                <n-button color="#056de8" @click="ClickLogin()">
                  登录
                </n-button></n-space
              >
            </n-space>
          </n-card>
        </div>
      </div>
    </div>
  </n-config-provider>
</template>

<script>
import axios from "axios";
import { roundToNearestMinutes } from "date-fns";
import { is } from "date-fns/locale";
import { reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";

export default {
  //暂时用不到
  /*
  mounted() {
    axios
      .get("https://api.unsplash.com/photos/random", {
        headers: {
          Authorization:
            "Client-ID uFDYVmDkMCw1agsWRfKpH5ks71EZImxvlVgcfqo_Gqo",
          "Accept-Version": "v1",
        },
        params: {
          query: "dark-design",
        },
      })
      .then((res) => {
        const unsplashImgURL = res.data.urls.raw + "&w=1920&h=1440&fit=fill";
        this.$refs.background.style.backgroundImage = `url(${unsplashImgURL})`;
        this.$refs.backgroundblur.style.backgroundImage = `url(${unsplashImgURL})`;
      });
  },*/
  setup() {
    const route = useRoute();
    const router = useRouter();
    const themeOverrides = {
      Input: {
        borderFocus: "1px solid #8590a6",
        boxShadowFocus: "0 0 0 2px rgba(133, 144, 166, 0.2)",
        borderHover: "1px solid #8590a6",
        caretColor: "#8590a6FF",
      },
      Checkbox: {
        textColor: "rgb(51, 54, 57)",
        colorChecked: "#056de8FF",
        borderChecked: "1px solid #056de8",
        borderFocus: "1px solid #056de8",
        boxShadowFocus: "0 0 0 2px solid rgba(5,109,232,0.3)",
      },
    }; //naive-ui主题覆盖
    function UsernameAlreadyUsed(rule, value) {
      return RegisterValue.detail != "Username already registered";
    } //验证用户名是否已经被注册
    function EmailAlreadyUsed(rule, value) {
      return Email.detail != "Email already registered";
    } //验证邮箱是否已经被注册
    function ErrorCode(rule, value) {
      return RegisterValue.detail != "Verification code error";
    } //验证验证码是否正确
    function validatePasswordSame(rule, value) {
      return value === RegisterValue.data.user.password;
    } //验证两次密码是否一致
    const EmailFormItemRef = ref(null); //邮箱输入框钩子
    const CodeFormItemRef = ref(null); //验证码输入框钩子
    const UsernameFormItemRef = ref(null); //用户名输入框钩子
    const rPasswordFormItemRef = ref(null); //确认密码输入框钩子
    const renderCountdown = ({ seconds }) => {
      return `${String(seconds).padStart(2)}秒后可以重发`;
    }; //倒计时渲染函数
    const SendcodeCountdown_active = ref(false); //倒计时是否激活
    const is_sendcode = ref(false); //是否已经发送过验证码
    const is_input_email = ref(true); //是否输入邮箱
    const formRef = ref(null); //表单钩子
    const PageStatus = ref(0); //页面状态
    const LoginValue = reactive({
      data: {
        username: "",
        password: "",
      },
      detail: "",
    }); //登录表单数据
    const Email = reactive({ data: { email: "" }, detail: "" }); //邮箱表单数据
    const MailRules = {
      data: {
        email: [
          {
            validator: EmailAlreadyUsed,
            message: "该邮箱已被注册",
            trigger: ["focus"],
          },
          {
            required: true,
            validator(rule, value) {
              if (!value) {
                return new Error("邮箱号不能为空");
              } else if (
                !/^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/.test(value)
              ) {
                return new Error("请输入正确的邮箱号");
              }
              return true;
            },
            trigger: ["blur", "input"],
          },
        ],
      },
    }; //邮箱表单验证规则
    const RegisterValue = reactive({
      data: {
        user: {
          username: "",
          password: "",
        },
        Code: { code: "" },
      },
      detail: "",
      confirmpassword: "",
    }); //注册表单数据
    const RegisterRules = {
      data: {
        Code: {
          code: [
            {
              required: true,
              validator(rule, value) {
                if (!value) {
                  return new Error("验证码不能为空！");
                } else if (!/^[0-9a-f]{4}$/.test(value)) {
                  return new Error("请输入正确的验证码！");
                }
                return true;
              },
              trigger: ["blur", "input"],
            },
            {
              validator: ErrorCode,
              message: "验证码错误",
              trigger: ["focus"],
            },
          ],
        },
        user: {
          username: [
            {
              required: true,
              validator(rule, value) {
                if (!value) {
                  return new Error("用户名不能为空");
                }
                return true;
              },
              trigger: ["blur", "input"],
            },
            {
              validator: UsernameAlreadyUsed,
              message: "该用户名已被注册",
              trigger: ["focus"],
            },
          ],
          password: [
            {
              required: true,
              validator(rule, value) {
                if (!value) {
                  return new Error("密码不能为空");
                } else if (!/^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/.test(value)) {
                  return new Error("请输入正确的密码格式");
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
    }; //注册表单验证规则
    return {
      is_input_email, //是否输入邮箱
      themeOverrides, //naive-ui主题覆盖
      RegisterRules, //注册表单验证规则
      EmailFormItemRef, //邮箱输入框钩子
      renderCountdown, //倒计时渲染函数
      SendcodeCountdown_active, //发送验证码的倒计时
      is_sendcode, //是否发送验证码
      formRef, //声明表单对象
      PageStatus, //页面状态
      LoginValue, //登录表单数据
      MailRules, //邮箱表单验证规则
      CodeFormItemRef, //验证码输入框钩子
      UsernameFormItemRef, //用户名输入框钩子
      rPasswordFormItemRef, //确认密码输入框钩子
      RegisterValue, //注册表单数据
      Email, //邮箱表单数据
      SendcodeCountdownFinish() {
        SendcodeCountdown_active.value = false;
        is_sendcode.value = false;
      },
      ClickLogin() {
        let form = new FormData();
        form.append("username", LoginValue.username);
        form.append("password", LoginValue.password);

        axios
          .post("/login/", form)
          .then((res) => {
            // Cookies.set("access_token", res.data.access_token, { expires: 1 });
            router.push("/");
          })
          .catch((err) => {
            const ErrorStatus = err.response.data.detail;
            LoginValue.detail = ErrorStatus;
            UsernameFormItemRef.value?.focus();
          });
      },
      //点击发送验证码
      clicksendcode() {
        is_sendcode.value = true;
        SendcodeCountdown_active.value = true;
        axios
          .post("/register/VerifyCode", Email.data)
          .then((res) => {
            is_input_email.value = false;
            alert("发送成功");
          })
          .catch((err) => {
            const ErrorStatus = err.response.data.detail;
            Email.detail = ErrorStatus;
            is_sendcode.value = false;
            EmailFormItemRef.value?.focus();
          });
      },

      //改变后清空错误信息
      EmailInputChange() {
        Email.detail = "";
      },
      RegisterInputChange() {
        RegisterValue.detail = "";
      },
      LoginInputChange() {
        LoginValue.detail = "";
      },

      handlePasswordInput() {
        if (RegisterValue.data.user.password) {
          rPasswordFormItemRef.value?.validate({ trigger: "password-input" });
        }
      },

      //点击注册按钮
      clickregister() {
        formRef.value?.validate((errors) => {
          if (!errors) {
            axios
              .post("/register/", RegisterValue.data)
              .then((res) => {
                alert("注册成功");
                PageStatus.value = 0;
              })
              .catch((err) => {
                const ErrorStatus = err.response.data.detail;
                RegisterValue.detail = ErrorStatus;
                is_send_form.value = false;
                if (ErrorStatus == "Verification code error")
                  CodeFormItemRef.value?.focus();
                else if (ErrorStatus == "Username already registered")
                  UsernameFormItemRef.value?.focus();
              });
          }
        });
      },

      //切换到登录/注册页面
      SwitchToLoginAndRegister() {
        if (PageStatus.value == 1) {
          PageStatus.value = 0;
        } else {
          PageStatus.value = 1;
        }
      },

      ClickToResetPassword() {
        router.push("/resetpassword");
      },
    };
  },
};
</script>

<style lang="less" scoped>
.body {
  height: 100vh;
  display: flex;
  width: 100%;
}
.BackGround {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-image: url("https://images.unsplash.com/photo-1487088678257-3a541e6e3922?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1548&q=80");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  filter: blur(10px);
}
.SiderColumn {
  position: absolute;
  top: 5%;
  bottom: 5%;
  left: 15%;
  width: 30%;
  height: 90%;
  background-image: url("https://images.unsplash.com/photo-1487088678257-3a541e6e3922?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1548&q=80");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  filter: blur(0px);
}
.MainColumn {
  position: absolute;
  top: 5%;
  bottom: 5%;
  right: 15%;
  width: 40%;
  height: 90%;
}
.ShowLRegister {
  height: 100%;
}
.ShowLogin {
  height: 100%;
}
.n-card {
  height: 100%;
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
