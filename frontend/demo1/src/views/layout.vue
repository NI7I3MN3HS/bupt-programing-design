<template>
  <div>
    <div class="header">
      <div class="header-content">
        <router-link to="/" class="header-left">
          <div class="homelogo">
            <span class="logo-text"> BuptHub </span>
          </div>
        </router-link>
        <div class="header-right">
          <n-space align="center" size="large">
            <!--搜索按钮-->
            <n-button @click="activate('top')" text block>
              <template #icon>
                <n-icon size="36">
                  <svg
                    t="1679069498934"
                    class="icon"
                    viewBox="0 0 1024 1024"
                    version="1.1"
                    xmlns="http://www.w3.org/2000/svg"
                    p-id="9562"
                    width="200"
                    height="200"
                  >
                    <path
                      d="M416 192C537.6 192 640 294.4 640 416S537.6 640 416 640 192 537.6 192 416 294.4 192 416 192M416 128C256 128 128 256 128 416S256 704 416 704 704 576 704 416 576 128 416 128L416 128z"
                      fill="#272636"
                      p-id="9563"
                    ></path>
                    <path
                      d="M832 864c-6.4 0-19.2 0-25.6-6.4l-192-192c-12.8-12.8-12.8-32 0-44.8s32-12.8 44.8 0l192 192c12.8 12.8 12.8 32 0 44.8C851.2 864 838.4 864 832 864z"
                      fill="#272636"
                      p-id="9564"
                    ></path>
                  </svg>
                </n-icon>
              </template>
            </n-button>

            <!--信息按钮-->
            <n-badge :value="NoticeNumber" :max="15">
              <n-icon size="31" color="black">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  xmlns:xlink="http://www.w3.org/1999/xlink"
                  viewBox="0 0 24 24"
                >
                  <g
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path
                      d="M10 5a2 2 0 0 1 4 0a7 7 0 0 1 4 6v3a4 4 0 0 0 2 3H4a4 4 0 0 0 2-3v-3a7 7 0 0 1 4-6"
                    ></path>
                    <path d="M9 17v1a3 3 0 0 0 6 0v-1"></path>
                  </g>
                </svg>
              </n-icon>
            </n-badge>

            <!--头像下拉菜单-->
            <n-dropdown trigger="click" :options="options">
              <n-avatar
                round
                :size="36"
                :src="avatar_url"
                fallback-src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
              />
            </n-dropdown>
            <n-button
              v-if="is_Authenticated"
              block
              @click="toWritePost"
              color="#056de8"
            >
              发帖
            </n-button>
          </n-space>
        </div>
      </div>
    </div>

    <div class="body-content">
      <!--嵌套路由-->
      <router-view></router-view>
    </div>
    <div class="footer">
      <div class="footer-content">
        <div class="footer-first">
          <div class="introduction">
            <div style="font-weight: bolder">欢迎来到BUPTHUB</div>
            Welcome!
          </div>
          <div class="about-us">
            <div style="font-weight: bolder">关于我们</div>
            <div>
              <n-button
                text
                tag="a"
                href="https://anyway.fm/news.php"
                target="_blank"
                text-color="black"
              >
                团队介绍
              </n-button>
            </div>
          </div>
        </div>
        <n-divider />
        <div class="footer-second">
          <div class="footer-rights">© 2023 BUPTHub.All rights reserved.</div>
          <div class="github-link">
            <n-button
              text
              style="font-size: 24px"
              tag="a"
              href="https://github.com/alantu123/bupt-programing-design"
              target="_blank"
              type="primary"
            >
              <n-icon color="black"
                ><svg
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  xmlns:xlink="http://www.w3.org/1999/xlink"
                  x="0px"
                  y="0px"
                  viewBox="0 0 512 512"
                  enable-background="new 0 0 512 512"
                  xml:space="preserve"
                >
                  <path
                    d="M256,32C132.3,32,32,134.9,32,261.7c0,101.5,64.2,187.5,153.2,217.9c1.4,0.3,2.6,0.4,3.8,0.4c8.3,0,11.5-6.1,11.5-11.4
	c0-5.5-0.2-19.9-0.3-39.1c-8.4,1.9-15.9,2.7-22.6,2.7c-43.1,0-52.9-33.5-52.9-33.5c-10.2-26.5-24.9-33.6-24.9-33.6
	c-19.5-13.7-0.1-14.1,1.4-14.1c0.1,0,0.1,0,0.1,0c22.5,2,34.3,23.8,34.3,23.8c11.2,19.6,26.2,25.1,39.6,25.1c10.5,0,20-3.4,25.6-6
	c2-14.8,7.8-24.9,14.2-30.7c-49.7-5.8-102-25.5-102-113.5c0-25.1,8.7-45.6,23-61.6c-2.3-5.8-10-29.2,2.2-60.8c0,0,1.6-0.5,5-0.5
	c8.1,0,26.4,3.1,56.6,24.1c17.9-5.1,37-7.6,56.1-7.7c19,0.1,38.2,2.6,56.1,7.7c30.2-21,48.5-24.1,56.6-24.1c3.4,0,5,0.5,5,0.5
	c12.2,31.6,4.5,55,2.2,60.8c14.3,16.1,23,36.6,23,61.6c0,88.2-52.4,107.6-102.3,113.3c8,7.1,15.2,21.1,15.2,42.5
	c0,30.7-0.3,55.5-0.3,63c0,5.4,3.1,11.5,11.4,11.5c1.2,0,2.6-0.1,4-0.4C415.9,449.2,480,363.1,480,261.7C480,134.9,379.7,32,256,32z
	"
                  ></path>
                </svg>
              </n-icon>
            </n-button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!--搜索抽屉-->
  <n-drawer v-model:show="active" :height="180" :placement="placement">
    <n-drawer-content>
      <n-input
        v-model:value="searchValue"
        size="large"
        round
        placeholder="搜索"
        passively-activated
        @keyup="toSearch"
      />
      热门搜索
      <SearchCard />
    </n-drawer-content>
  </n-drawer>

  <!--回到顶部 可视高度50-->
  <div class="BackTop">
    <n-back-top :bottom="150" :visibility-height="50" iconColorHover="black">
    </n-back-top>
  </div>

  <n-button
    type="info"
    round
    style="position: fixed; right: 20px; bottom: 20px"
  >
    浮动按钮
  </n-button>
</template>

<script setup>
import Cookies from "js-cookie";
import { useRoute, useRouter } from "vue-router";
import {
  ref,
  reactive,
  defineComponent,
  onBeforeMount,
  onMounted,
  computed,
} from "vue";
import { useMessage } from "naive-ui";
import { property } from "lodash";
import useAuthStore from "@/stores/modules/AuthStore";
import useUserStore from "@/stores/modules/UserStore";
import { storeToRefs } from "pinia";
import SearchCard from "@/components/SearchCard.vue";
const route = useRoute();
const router = useRouter();

//导入请求状态
const authStore = useAuthStore();
//导入用户状态
const userStore = useUserStore();

const { is_Authenticated } = storeToRefs(authStore);
const { avatar_url } = storeToRefs(userStore);

onMounted(() => {
  if (is_Authenticated.value) {
    userStore.setUserInfo();
  }
});

const options = [
  {
    show: is_Authenticated.value ? false : true,
    label: "登录/注册",
    key: "LoginandRegister",
    props: {
      onClick: () => {
        router.push("/loginandregister");
      },
    },
  },
  {
    show: is_Authenticated.value ? true : false,
    label: "用户资料",
    key: "Profile",
    props: {
      onClick: () => {
        router.push(`/user/${userStore.id}`);
      },
    },
  },
  {
    show: is_Authenticated.value ? true : false,
    label: "退出登录",
    key: "logout",
    props: {
      onClick: () => {
        authStore.logout();
        authStore.$reset();
        userStore.$reset();
        router.push("/loginandregister");
      },
    },
  },
];

const active = ref(false);
const placement = ref("right");
const activate = (place) => {
  active.value = true;
  placement.value = place;
};

const NoticeNumber = ref(5);

function toWritePost() {
  if (is_Authenticated.value) {
    router.push("/WritePost");
  } else {
    router.push("/loginandregister");
  }
}

const searchValue = ref("");

function toSearch() {
  router.push({
    path: "/search/post/",
    query: {
      keyword: searchValue.value,
    },
  });
}
</script>

<style lang="less" scoped>
.header {
  height: 60px;
  top: 0px;
  width: 100%;
  position: fixed;
  z-index: 1000; //设置z轴置顶
  background: #fff;

  box-shadow: 0 2px 6px 0 #ddd;

  .header-content {
    height: 100%;
    width: 90%;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .header-left {
      height: 60px;
      display: flex;
      align-items: center;
      text-decoration: none;

      .logo-text {
        font-size: 30px;
        font-weight: bolder;
        color: #333;
        margin-left: 5px;
      }
    }

    .header-right {
      height: 60px;
      display: flex;
      align-items: center;

      .user-notice {
        margin-right: 20px;
      }

      .header-search {
        margin-right: 20px;
      }
    }
  }
}
.body-content {
  position: relative;
  min-height: calc(100vh - 220px);
  margin-top: 60px;
}
.footer {
  height: 160px;
  width: 100%;
  background-color: #f6f6f6;

  .footer-content {
    width: 90%;
    margin: 0 auto;
    justify-content: space-between;
    .footer-first {
      display: flex;
      padding: 10px 2px 10px 2px;
      .introduction {
        flex: 1;
      }
    }
    .n-divider {
      margin: 5px 0 15px 0;
    }
    .footer-second {
      display: flex;
      .footer-rights {
        flex: 1;
      }
    }
  }
}
</style>
