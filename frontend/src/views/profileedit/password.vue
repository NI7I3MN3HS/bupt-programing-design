<template>
  <div class="settingview">
    <div class="pagehead">
      <div class="pagetitle">
        <i class="icon">
          <n-icon size="40" :component="SettingsOutline" />
        </i>
        <span class="vm">账号设置</span>
      </div>
    </div>
    <div class="pagemain">
      <nav class="navigation">
        <ul class="swiper">
          <li class="slide">
            <router-link to="/profile/edit1">
              <span class="route"> 个人资料 </span>
            </router-link>
          </li>
          <li class="slide">
            <router-link to="/profile/edit3">
              <span class="route exact"> 修改密码 </span>
            </router-link>
          </li>
        </ul>
      </nav>
      <div class="pageview">
        <div class="pageview_view">
          <div class="_head">修改密码</div>
          <div class="_main">
            <div class="_code">
              <n-form ref="formRef" :model="model" :rules="rules">
                <n-form-item path="origin_passowrd" label="当前密码">
                  <n-input
                    v-model:value="model.origin_passowrd"
                    @keydown.enter.prevent
                  />
                  <!-- :disabled="!is_Change"
                                    @blur="is_Change = false"        
                                  /> -->
                </n-form-item>
                <n-form-item path="new_password" label="新密码">
                  <n-input
                    v-model:value="model.new_password"
                    @keydown.enter.prevent
                  />
                </n-form-item>
                <n-form-item path="confirm" label="确认新密码">
                  <n-input
                    v-model:value="model.confirm"
                    @keydown.enter.prevent
                  />
                </n-form-item>
              </n-form>
              <!-- <label class="_item">
                                <span class="_intro">当前密码</span>
                                <input class="_input" placeholder="请输入原密码">
                            </label>
                            <label class="_item">
                                <span class="_intro">新密码</span>
                                <input class="_input" placeholder="请输入新密码">
                            </label>
                            <label class="_item">
                                <span class="_intro">确认新密码</span>
                                <input class="_input" placeholder="请再次输入新密码">
                            </label> -->
              <div class="_button">
                <n-button type="tertiary" @click="UpdateUserInfo"
                  >确认修改</n-button
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMessage } from "naive-ui";
import { SettingsOutline } from "@vicons/ionicons5";
import { ref } from "vue";
import axios from "axios";
import useAuthStore from "@/stores/modules/AuthStore";
import useUserStore from "@/stores/modules/UserStore";
import { storeToRefs } from "pinia";

//待查
const authStore = useAuthStore();
const userStore = useUserStore();

const { origin_passowrd, new_password } = storeToRefs(userStore);

//使用信息提示
const message = useMessage();

//定义请求头
//axios待写
const UserClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
    headers: { "Content-Type": "multipart/form-data" },
  },
});

const formRef = ref(null);

//定义规则
const rules = {
  origin_passowrd: [
    {
      required: true,
      message: "用户名不可为空",
      //固定原本密码 待改动
    },
  ],
  new_password: [
    {
      required: true,
      validator(rule, value) {
        if (!value) {
          return new Error("密码不能为空");
        } else if (!/^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/.test(value)) {
          return new Error(
            "请输入正确的密码格式:至少8位，包含一个大写字母和一个数字"
          );
        }
        return true;
      },
      trigger: ["blur", "input"],
    },
  ],
  confirm: [
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

function validatePasswordSame(rule, value) {
  return value === model.value.new_password;
}

//model中有三项，声明和初始化变量
const model = ref(
  {
    origin_passowrd: "",
    //password: ""
    new_password: "",
    //password: ""
  }
  // origin_passowrd: origin_passowrd.value,
  // new_password: new_password.value,
);

// const is_Change = ref(false);

//更新用户信息
function UpdateUserInfo() {
  //表单验证失败
  formRef.value?.validate((errors) => {
    if (errors) {
      message.error("请检查输入");
      return;
    }
    UserClient.put("/user/reset_password", {
      origin_passowrd: { password: model.value.origin_passowrd },
      new_password: { password: model.value.new_password },
    })
      .then((response) => {
        message.success("更新成功");
        userStore.setUserInfo();
      })
      .catch((error) => {
        if (error.response.data.detail == "Incorrect password")
          message.error("原密码错误");
        else message.error("更新失败");
      });
  });
}
</script>

<style lang="less" scoped>
.settingview {
  width: 100%;
  min-height: calc(100vh);
  display: block;
  background: #f3f3f4;
  .pagehead {
    margin: 0px 294px;
    padding: 40px 0px;
    .pagetitle {
      font-size: 28px;
      .icon {
        font-size: 48px;
        margin-right: 10px;
      }
      .vm {
        vertical-align: text-top;
      }
    }
  }
  .pagemain {
    min-height: calc(80vh);
    margin: 0px 294px;
    display: flex;
    max-width: 948px;
    margin: auto;
    .navigation {
      margin-right: 52px;
      .swiper {
        display: flex;
        flex-direction: column;
        list-style: none;
        width: 180px;
        .slide {
          margin: 0;
          text-align: left;
          border-bottom: 1px solid #e5e5e5;
          a {
            text-decoration: none;
          }
          .router-link-active {
            text-decoration: none;
          }
          .route {
            font-size: 16px;
            font-weight: 600;
            color: #8e8787;
            display: block;
            padding: 16px 0;
          }
          .exact {
            position: relative;
            color: #fd281a;
          }
        }
      }
    }
    .pageview {
      background: #ffffff;
      flex: 1;
      margin-top: 0;
      margin-bottom: 4px;
      .pageview_view {
        ._head {
          font-size: larger;
          font-weight: 1000;
          border-bottom: 1px solid #e5e5e5;
          padding: 24px 32px;
        }
        ._main {
          padding: 0 32px;
          display: flex;
          align-items: flex-start;
          min-height: calc(60vh);
          ._code {
            padding: 24px 0 0 0;
            display: flex;
            flex-direction: column;
            flex: 1;
            .n-form-item {
              min-height: calc(15vh);
              ._intro {
                display: flex;
                width: 650px;
                font-weight: 500;
                color: #655e5e;
                margin-bottom: 8px;
              }
              .n-input {
                display: flex;
                width: 650px;
                padding: 10px 12px;
                background: #f7f7f8;
                border: none;
                outline-style: none;
                font-size: 16px;
                line-height: 22px;
              }
              ._button {
                display: flex;
                width: 250px;
              }
            }
          }
        }
      }
    }
  }
}
</style>
