<template>
  <div class="background">
    <div class="ProfileBGImage" />
    <div class="Avatar">
      <n-avatar :size="140" :src="userData.avatar_url" />
    </div>
    <div class="ProfileHeader">
      <div class="UserMain">
        <n-card content-style="padding:0 24px 20px 24px">
          <div>
            <span class="UserName">{{ userData.username }}</span>
            <span class="UserPersonalizedSignature">{{
              userData.introduction
            }}</span>
            <span class="EditorProfileButton"
              ><router-link to="/profile/edit1"
                ><n-button
                  ghost
                  color="#056de8"
                  text-color="#056de8"
                  v-if="userStore.id == userData.id"
                  >编辑个人资料</n-button
                ></router-link
              ></span
            >
          </div>
          <div class="FollowsAndFans">
            <n-space>
              <n-button text>
                <template #icon>
                  <n-icon>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      xmlns:xlink="http://www.w3.org/1999/xlink"
                      viewBox="0 0 512 512"
                    >
                      <path
                        d="M336 256c-20.56 0-40.44-9.18-56-25.84c-15.13-16.25-24.37-37.92-26-61c-1.74-24.62 5.77-47.26 21.14-63.76S312 80 336 80c23.83 0 45.38 9.06 60.7 25.52c15.47 16.62 23 39.22 21.26 63.63c-1.67 23.11-10.9 44.77-26 61C376.44 246.82 356.57 256 336 256zm66-88z"
                        fill="currentColor"
                      ></path>
                      <path
                        d="M467.83 432H204.18a27.71 27.71 0 0 1-22-10.67a30.22 30.22 0 0 1-5.26-25.79c8.42-33.81 29.28-61.85 60.32-81.08C264.79 297.4 299.86 288 336 288c36.85 0 71 9 98.71 26.05c31.11 19.13 52 47.33 60.38 81.55a30.27 30.27 0 0 1-5.32 25.78A27.68 27.68 0 0 1 467.83 432z"
                        fill="currentColor"
                      ></path>
                      <path
                        d="M147 260c-35.19 0-66.13-32.72-69-72.93c-1.42-20.6 5-39.65 18-53.62c12.86-13.83 31-21.45 51-21.45s38 7.66 50.93 21.57c13.1 14.08 19.5 33.09 18 53.52c-2.87 40.2-33.8 72.91-68.93 72.91z"
                        fill="currentColor"
                      ></path>
                      <path
                        d="M212.66 291.45c-17.59-8.6-40.42-12.9-65.65-12.9c-29.46 0-58.07 7.68-80.57 21.62c-25.51 15.83-42.67 38.88-49.6 66.71a27.39 27.39 0 0 0 4.79 23.36A25.32 25.32 0 0 0 41.72 400h111a8 8 0 0 0 7.87-6.57c.11-.63.25-1.26.41-1.88c8.48-34.06 28.35-62.84 57.71-83.82a8 8 0 0 0-.63-13.39c-1.57-.92-3.37-1.89-5.42-2.89z"
                        fill="currentColor"
                      ></path>
                    </svg>
                  </n-icon>
                </template>
                {{ userData.follow_count }}关注
              </n-button>
              <n-button text>
                <template #icon>
                  <n-icon>
                    <svg
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
                        d="M458,210.409l-145.267-12.476L256,64l-56.743,133.934L54,210.409l110.192,95.524L131.161,448L256,372.686L380.83,448
	l-33.021-142.066L458,210.409z M272.531,345.286L256,335.312l-16.53,9.973l-59.988,36.191l15.879-68.296l4.369-18.79l-14.577-12.637
	l-52.994-45.939l69.836-5.998l19.206-1.65l7.521-17.75l27.276-64.381l27.27,64.379l7.52,17.751l19.208,1.65l69.846,5.998
	l-52.993,45.939l-14.576,12.636l4.367,18.788l15.875,68.299L272.531,345.286z"
                      ></path>
                    </svg>
                  </n-icon>
                </template>
                {{ userData.follower_count }}粉丝
              </n-button></n-space
            >
          </div>
        </n-card>
      </div>
    </div>
    <div class="ProfileContent"></div>
  </div>
</template>

<script setup>
import { ref, reactive, defineComponent, watch, onBeforeMount } from "vue";
import { useRoute, useRouter } from "vue-router";
import useUserStore from "@/stores/modules/UserStore";
import axios from "axios";
const route = useRoute();
const router = useRouter();

const userStore = useUserStore();

const userData = reactive({
  avatar_url: null,
  username: null,
  introduction: null,
  follow_count: null,
  follower_count: null,
});

function fetchUser(user_id) {
  axios
    .get(`/user/${user_id}`)
    .then((response) => {
      console.log(response.data);
      userData.avatar_url = response.data.avatar_url;
      userData.username = response.data.username;
      userData.introduction = response.data.introduction;
    })
    .catch((error) => {
      console.error(error);
    });
  axios
    .get(`/follow/get_followed/${user_id}`)
    .then((response) => {
      console.log(response.data);
      userData.follow_count = response.data.count;
    })
    .catch((error) => {
      console.error(error);
    });
  axios
    .get(`/follow/get_follower/${user_id}`)
    .then((response) => {
      console.log(response.data);
      userData.follower_count = response.data.count;
    })
    .catch((error) => {
      console.error(error);
    });
}

//组件挂载前获取数据
onBeforeMount(() => {
  fetchUser(route.params.id);
  //路由参数更新时，重新获取数据
  watch(
    () => route.params.id,
    async (newId) => {
      fetchUser(newId);
    }
  );
});
</script>

<style lang="less" scoped>
.n-card {
  width: 100%;
  height: 120px;
}
.light-green {
  height: 108px;
  background-color: rgba(0, 128, 0, 0.12);
}
.green {
  height: 108px;
  background-color: rgba(0, 128, 0, 0.24);
}

.background {
  width: 100%;
  background-color: rgb(233, 232, 235);
  min-height: calc(100vh);
  display: block;
  .ProfileBGImage {
    height: 250px;
    background-image: url(https://pic1.zhimg.com/80/v2-c9ccad67cdbdfaceaee4edca8b17f710_1440w.webp);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    z-index: 0;
  }
  .Avatar {
    position: absolute;
    left: 15%;
    width: 140px;
    top: 200px;
    z-index: 10;
  }
  .ProfileHeader {
    width: 100%;
  }
  .ProfileContent {
    width: 70%;
    margin: 0 auto;
  }
}
.UserName {
  font-size: 40px;
  font-weight: 700;
  left: calc(15% + 140px + 20px);
}
.UserPersonalizedSignature {
  font-size: 14px;
  font-weight: 400;
  left: calc(15% + 140px + 30px);
}
.EditorProfileButton {
  left: calc(15% + 140px + 500px);
}
.FollowsAndFans {
  left: calc(15% + 140px + 20px);
}
</style>
