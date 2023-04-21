<template>
  <div class="body">
    <div class="BackGround" />
    <div class="SiderColumn" />
    <div class="MainColumn">
      <div v-if="PageStatus == 0" class="ShowLRegister">
        <n-card>
          <template #header>
            <div class="H1">创建一个账户</div>
            <div class="H2">
              <span>已有账户？</span
              ><span
                ><n-button text @click="switchtologin" text-color="#056de8"
                  >登录</n-button
                ></span
              >
            </div>
          </template>
          <n-form ref="formRef" :model="Email" :rules="MailRules">
            <n-form-item-row label="邮箱" path="data.email">
              <n-input
                ref="EmailFormItemRef"
                @change="EmailInputChange"
                v-model:value="Email.data.email"
              />
            </n-form-item-row>
          </n-form>
          <n-form :model="RegisterValue">
            <n-form-item-row label="验证码">
              <n-input
                :disabled="!Email.data.email"
                v-model:value="RegisterValue.Code.code"
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
            <n-form-item-row label="用户名">
              <n-input v-model:value="RegisterValue.user.username" />
            </n-form-item-row>
            <n-form-item-row label="密码">
              <n-input
                type="password"
                show-password-on="click"
                placeholder="密码"
                v-model:value="RegisterValue.user.password"
              />
            </n-form-item-row>
            <n-form-item-row label="再次输入密码">
              <n-input
                type="password"
                show-password-on="click"
                placeholder="密码"
                v-model:value="RegisterValue.user.password"
              />
            </n-form-item-row>
          </n-form>
          <n-space justify="center">
            <n-button color="#056de8">创建你的账户</n-button></n-space
          >
        </n-card>
      </div>
      <LoginForm />
      <div v-if="PageStatus == 1" class="ShowLogin">
        <n-card>
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
          </n-button></n-card
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { roundToNearestMinutes } from "date-fns";
import { is } from "date-fns/locale";
import { reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
const route = useRoute();
const router = useRouter();

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
    function EmailAlreadyUsed(rule, value) {
      return Email.detail != "Email already registered";
    } //验证邮箱是否已经被注册
    const EmailFormItemRef = ref(null); //邮箱输入框钩子
    const renderCountdown = ({ seconds }) => {
      return `${String(seconds).padStart(2)}秒后可以重发`;
    }; //倒计时渲染函数
    const SendcodeCountdown_active = ref(false); //倒计时是否激活
    const is_sendcode = ref(false); //是否已经发送过验证码
    const formRef = ref(null); //表单钩子
    const PageStatus = ref(0); //页面状态
    const LoginValue = reactive({
      username: "",
      password: "",
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
                return new Error("邮箱号不能为空！");
              } else if (
                !/^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/.test(value)
              ) {
                return new Error("请输入正确的邮箱号！");
              }
              return true;
            },
            trigger: ["blur", "input"],
          },
        ],
      },
    }; //邮箱表单验证规则
    const RegisterValue = reactive({
      user: {
        username: "",
        password: "",
      },
      Code: {
        code: "",
      },
    }); //注册表单数据
    return {
      EmailFormItemRef, //邮箱输入框钩子
      renderCountdown, //倒计时渲染函数
      SendcodeCountdown_active, //发送验证码的倒计时
      is_sendcode, //是否发送验证码
      formRef, //声明表单对象
      PageStatus, //页面状态
      LoginValue, //登录表单数据
      MailRules, //邮箱表单验证规则
      SendcodeCountdownFinish() {
        SendcodeCountdown_active.value = false;
        is_sendcode.value = false;
      },
      clicklogin() {
        let form = new FormData();
        form.append("username", LoginValue.username);
        form.append("password", LoginValue.password);

        axios.post("/login/", form).then(() => {
          alert("登录成功");
        });
      },
      RegisterValue,
      Email,
      clicksendcode() {
        is_sendcode.value = true;
        SendcodeCountdown_active.value = true;
        axios
          .post("/register/VerifyCode", Email.data)
          .then(() => {
            alert("发送成功");
          })
          .catch((err) => {
            const ErrorStatus = err.response.data.detail;
            Email.detail = ErrorStatus;
            is_sendcode.value = false;
            EmailFormItemRef.value?.focus();
          });
      },
      EmailInputChange() {
        Email.detail = "";
      },
      clickregister() {
        axios.post("/register/", RegisterValue).then(() => {
          alert("注册成功");
        });
      },
      switchtologin() {
        PageStatus.value = 1;
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
  left: 10%;
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
  right: 10%;
  width: 50%;
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
  .n-card__action {
    background-color: white;
  }
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
