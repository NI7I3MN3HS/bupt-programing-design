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
            <n-form-item-row label="邮箱" path="email">
              <n-input v-model:value="Email.email" />
            </n-form-item-row>
          </n-form>
          <n-form :model="RegisterValue">
            <n-form-item-row label="验证码">
              <n-input
                :disabled="!Email.email"
                v-model:value="RegisterValue.Code.code"
              />
              <n-button
                v-if="!is_sendcode"
                :disabled="!Email.email"
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
      <div v-if="PageStatus == 1" class="ShowLogin">
        <n-card>222</n-card>
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
    const renderCountdown = ({ seconds }) => {
      return `${String(seconds).padStart(2)}秒后可以重发`;
    };
    const SendcodeCountdown_active = ref(false);
    const is_sendcode = ref(false);
    const formRef = ref(null);
    const PageStatus = ref(0);
    const LoginValue = reactive({
      username: "",
      password: "",
    });
    const Email = reactive({ email: "" });
    const MailRules = {
      email: [
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
          trigger: ["input", "blur"],
        },
      ],
    };
    const RegisterValue = reactive({
      user: {
        username: "",
        password: "",
      },
      Code: {
        code: "",
      },
    });
    return {
      renderCountdown, //倒计时渲染函数
      SendcodeCountdown_active, //发送验证码的倒计时
      is_sendcode, //是否发送验证码
      formRef, //声明表单对象
      PageStatus,
      LoginValue,
      MailRules,
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
        axios.post("/register/VerifyCode", Email).then(() => {
          alert("发送成功");
        });
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
