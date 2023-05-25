<template>
  <div class="settingview">
    <div class="pagehead">
      <div class="pagetitle">
        <i class="icon">
          <n-icon size="40" :component="SettingsOutline" />
        </i>
        <span class="vm">账号设置</span>
        <!-- 高度不太合适 -->
      </div>
    </div>
    <div class="pagemain">
      <nav class="navigation">
        <!-- 点击后的after未实现 -->
        <ul class="swiper">
          <li class="slide">
            <router-link to="/profile/edit1">
              <span class="route exact"> 个人资料 </span>
            </router-link>
          </li>
          <li class="slide">
            <router-link to="/profile/edit3">
              <span class="route"> 修改密码 </span>
            </router-link>
          </li>
        </ul>
      </nav>
      <div class="pageview">
        <div class="pageview_view">
          <div class="_head">个人资料</div>
          <div class="_main">
            <div class="_left">
              <div class="_image">
                <div class="_img">
                  <n-avatar :size="100" :src="avatar_url" />
                </div>
                <div class="_imgupload">
                  <n-upload :custom-request="myUpload" :show-file-list="false">
                    <n-button text>
                      <template #icon>
                        <n-icon size="20" :component="PictureOutlined" />
                      </template>
                      上传头像
                    </n-button>
                  </n-upload>
                  <!-- <input>后端？ -->
                </div>
              </div>
            </div>
            <div class="_right">
              <n-form ref="formRef" :model="model" :rules="rules">
                <n-form-item path="username" label="昵称">
                  <n-input
                    v-model:value="model.username"
                    @keydown.enter.prevent
                  />
                </n-form-item>
                <n-form-item path="introduction" label="个人简介">
                  <n-input
                    v-model:value="model.introduction"
                    @keydown.enter.prevent
                    maxlength="20"
                  />
                </n-form-item>
                <n-form-item path="email" label="邮箱">
                  <n-input class="_special1"
                    v-model:value="model.email"
                    @keydown.enter.prevent
                    :disabled="!is_ChangeEmail"
                    @blur="is_ChangeEmail = false"
                  />
                  <n-button class="_special2" type="tertiary" @click="is_ChangeEmail = true">
                    修改邮箱</n-button
                  >
                </n-form-item>
              </n-form>
              <!--
              <label class="_item">
                <span class="_intro">昵称</span>
                <input class="_input" placeholder="请输入昵称" />
              </label>
              <label class="_item">
                <span class="_intro">个人简介</span>
                <input
                  class="_input"
                  placeholder="请介绍你自己"
                  maxlength="200"
                />
              </label>
              -->
              <div class="_button">
                <n-button type="tertiary" @click="UpdateUserInfo"
                  >确认提交</n-button
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
import { PictureOutlined } from "@vicons/antd";
import { ref } from "vue";
import axios from "axios";
import useAuthStore from "@/stores/modules/AuthStore";
import useUserStore from "@/stores/modules/UserStore";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";

const router = useRouter();

const authStore = useAuthStore();
const userStore = useUserStore();

const { avatar_url, username, email, introduction } = storeToRefs(userStore);

//使用信息提示
const message = useMessage();

//定义请求头
const UserClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
    headers: { "Content-Type": "multipart/form-data" },
  },
});

//上传头像
const myUpload = (file) => {
  const formData = new FormData();
  formData.append("avatar", file.file.file);
  UserClient.post("/user/upload_avatar", formData)
    .then((response) => {
      message.success("上传成功");
      //刷新页面
      window.location.reload();
    })
    .catch((error) => {
      message.error("上传失败");
    });
};

const formRef = ref(null);

const rules = {
  username: [
    {
      required: true,
      message: "用户名不可为空",
    },
  ],
  introduction: [
    {
      required: true,
      message: "请介绍下你自己",
    },
  ],
  email: [
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
};

const model = ref({
  username: username.value,
  introduction: introduction.value,
  email: email.value,
});

const is_ChangeEmail = ref(false);

//更新用户信息
function UpdateUserInfo() {
  UserClient.put("/user/update", {
    username: model.value.username,
    introduction: model.value.introduction,
    email: model.value.email,
  })
    .then((response) => {
      message.success("更新成功");
      userStore.setUserInfo();
      //如果用户名修改了，则需要重新登录
      if (model.value.username != username.value) {
        authStore.logout();
        userStore.$reset();
        router.push("/loginandregister");
        return;
      }
    })
    .catch((error) => {
      message.error("更新失败");
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
    display: flex; // 将容器指定为flex布局
    max-width: 948px;
    margin: auto; //重要？

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
      // background: #e4c0c0;//调色看位置用
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

          // background: #ebd0d0;//调色看位置用
          ._left {
            position: absolute;
            left: 40px;
            margin: 24px 40px 0 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;

            ._image {
              margin: 0 0 18px 0;
              display: inline-block;
              vertical-align: middle;
              line-height: normal; //没什
              position: relative; //么用

              ._imgupload {
                margin: 5px 0 0 10px;
              }
            }
          }

          ._right {
            padding: 24px 0 0 0;
            position: absolute;
            left: 180px;
            display: flex;
            flex-direction: column;
            flex: 1;

            .n-form-item {
              // width: calc(100%-200px);
              //在此处宽度值无效
              min-height: calc(15vh);

              // background: #e5e5e5;//调色看位置用
              ._intro {
                display: flex;
                width: 490px;
                font-weight: 500;
                color: #655e5e;
                margin-bottom: 8px;
              }
              ._special1{
                margin-right: 15px;
              }
              ._special2{
                margin-right: 15px;
              }
              .n-input {
                display: flex;
                width: 490px;
                padding: 10px 12px;
                background: #f7f7f8;
                border: none;
                outline-style: none;
                font-size: 16px;
                line-height: 22px;
              }

              //这里括号位置粗心大意>_<耽误好多时间
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
