<template>
  <n-config-provider :theme="theme">
    <div class="bbs">
      <div class="main-column">
        <!---card模版-->
        <div v-for="card in cards">
          <n-card class="first">
            <template #header>占个位置 </template>
            <n-ellipsis
              :expand-trigger="is_active_expand === false ? 'click' : 'unclick'"
              line-clamp="2"
              :tooltip="false"
            >
              电灯熄灭 物换星移 泥牛入海<br />
              黑暗好像 一颗巨石 按在胸口<br />
              独脚大盗 百万富翁 摸爬滚打<br />
              黑暗好像 一颗巨石 按在胸口
            </n-ellipsis>
            <template #footer>
              <div class="author">编辑于---</div>
            </template>
            <template #action>
              <n-space>
                <n-button
                  :color="
                    is_likebutton_active === true
                      ? '#056de8'
                      : 'rgba(5, 109, 232, 0.15)'
                  "
                  :text-color="
                    is_likebutton_active === true ? 'white' : '#056de8'
                  "
                  @click="likebuttonclick()"
                >
                  <template #icon>
                    <n-icon
                      ><svg
                        t="1681457768550"
                        class="icon"
                        viewBox="0 0 1024 1024"
                        version="1.1"
                        xmlns="http://www.w3.org/2000/svg"
                        p-id="2016"
                        width="200"
                        height="200"
                      >
                        <path
                          d="M511.997952 268.025732 146.975708 755.974268l730.048584 0L511.997952 268.025732"
                          p-id="2017"
                        ></path>
                      </svg>
                    </n-icon>
                  </template>
                  <span v-if="is_likebutton_active === true">已赞成</span>
                  <span v-else>赞成</span>
                </n-button>

                <n-button
                  :color="
                    is_dislikebutton_active === true
                      ? '#056de8'
                      : 'rgba(5, 109, 232, 0.15)'
                  "
                  :text-color="
                    is_dislikebutton_active === true ? 'white' : '#056de8'
                  "
                  @click="dislikebuttonclick()"
                >
                  <template #icon>
                    <n-icon
                      ><svg
                        t="1681458252944"
                        class="icon"
                        viewBox="0 0 1024 1024"
                        version="1.1"
                        xmlns="http://www.w3.org/2000/svg"
                        p-id="1472"
                        width="200"
                        height="200"
                      >
                        <path
                          d="M511.997952 755.974268l365.02634-487.950584L146.975708 268.023684 511.997952 755.974268"
                          p-id="1473"
                        ></path>
                      </svg>
                    </n-icon>
                  </template>
                  <span v-if="is_dislikebutton_active === true">已反对</span>
                  <span v-else>反对</span>
                </n-button>

                <n-button
                  ghost
                  text-color="black"
                  color="transparent"
                  :bordered="false"
                  @click="commentsclick()"
                >
                  <template #icon>
                    <svg
                      t="1681465953088"
                      class="icon"
                      viewBox="0 0 1024 1024"
                      version="1.1"
                      xmlns="http://www.w3.org/2000/svg"
                      p-id="4712"
                      width="200"
                      height="200"
                    >
                      <path
                        d="M157.568 751.296c-11.008-18.688-18.219-31.221-21.803-37.91A424.885 424.885 0 0 1 85.333 512c0-235.637 191.03-426.667 426.667-426.667S938.667 276.363 938.667 512 747.637 938.667 512 938.667a424.779 424.779 0 0 1-219.125-60.502A2786.56 2786.56 0 0 0 272.82 866.4l-104.405 28.48c-23.893 6.507-45.803-15.413-39.285-39.296l28.437-104.288z m65.301 3.787l-17.258 63.306 63.306-17.258a32 32 0 0 1 24.523 3.21 4515.84 4515.84 0 0 1 32.352 18.944A360.79 360.79 0 0 0 512 874.667c200.299 0 362.667-162.368 362.667-362.667S712.299 149.333 512 149.333 149.333 311.701 149.333 512c0 60.587 14.848 118.955 42.827 171.136 3.712 6.912 12.928 22.827 27.37 47.232a32 32 0 0 1 3.34 24.715z m145.995-70.774a32 32 0 1 1 40.917-49.205A159.19 159.19 0 0 0 512 672c37.888 0 73.675-13.173 102.187-36.885a32 32 0 0 1 40.917 49.216A223.179 223.179 0 0 1 512 736a223.179 223.179 0 0 1-143.136-51.69z"
                        p-id="4713"
                      ></path>
                    </svg>
                  </template>
                  评论
                </n-button>

                <n-button
                  color="transparent"
                  text-color="black"
                  ghost
                  :bordered="false"
                  @click="showModal1 = true"
                >
                  <template #icon
                    ><svg
                      xmlns="http://www.w3.org/2000/svg"
                      xmlns:xlink="http://www.w3.org/1999/xlink"
                      viewBox="0 0 24 24"
                    >
                      <path
                        d="M16.5 3c-1.74 0-3.41.81-4.5 2.09C10.91 3.81 9.24 3 7.5 3C4.42 3 2 5.42 2 8.5c0 3.78 3.4 6.86 8.55 11.54L12 21.35l1.45-1.32C18.6 15.36 22 12.28 22 8.5C22 5.42 19.58 3 16.5 3zm-4.4 15.55l-.1.1l-.1-.1C7.14 14.24 4 11.39 4 8.5C4 6.5 5.5 5 7.5 5c1.54 0 3.04.99 3.57 2.36h1.87C13.46 5.99 14.96 5 16.5 5c2 0 3.5 1.5 3.5 3.5c0 2.89-3.14 5.74-7.9 10.05z"
                        fill="currentColor"
                      ></path>
                    </svg> </template
                  >收藏
                </n-button>

                <!---收藏模态框1-->
                <n-modal v-model:show="showModal1">
                  <n-card :style="FavoriteModalCard">
                    <template #header>
                      <div class="FavoriteModalCardHeaderH1">
                        添加收藏
                        <span class="FavoriteModalCloseButton">
                          <n-button
                            @click="showModal1 = false"
                            ghost
                            :bordered="false"
                            text-color="black"
                            color="transparent"
                            ><template #icon
                              ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                xmlns:xlink="http://www.w3.org/1999/xlink"
                                viewBox="0 0 24 24"
                              >
                                <path
                                  d="M18.3 5.71a.996.996 0 0 0-1.41 0L12 10.59L7.11 5.7A.996.996 0 1 0 5.7 7.11L10.59 12L5.7 16.89a.996.996 0 1 0 1.41 1.41L12 13.41l4.89 4.89a.996.996 0 1 0 1.41-1.41L13.41 12l4.89-4.89c.38-.38.38-1.02 0-1.4z"
                                  fill="currentColor"
                                ></path></svg></template
                          ></n-button>
                        </span>
                      </div>
                      <div class="FavoriteModalCardHeaderH2">
                        请选择你喜欢的收藏夹
                      </div>
                    </template>
                    <n-list>
                      <n-list-item v-for="item in items" :key="item.id">
                        <n-space justify="space-between">
                          <span>{{ item.title }}</span>
                          <span class="FavoriteModalFavoriteButton">
                            <n-button
                              @click="favoritebuttonclick(item)"
                              :color="
                                item.is_favoritebutton_active === true
                                  ? '#8590a6'
                                  : '#056de8'
                              "
                              :text-color="
                                item.is_favoritebutton_active === true
                                  ? 'white'
                                  : '#056de8'
                              "
                              :ghost="!item.is_favoritebutton_active"
                            >
                              <span
                                v-if="item.is_favoritebutton_active === true"
                                >已收藏
                              </span>
                              <span v-else>收藏</span></n-button
                            >
                          </span>
                        </n-space>
                      </n-list-item>
                      <n-list-item
                        v-if="items.length === 0"
                        style="text-align: center"
                        >暂无收藏</n-list-item
                      >
                    </n-list>
                    <template #footer>
                      <div class="FavoriteModalCardFooter">
                        <n-button
                          color="#056de8"
                          text-color="white"
                          @click="ShowCreateFavoriteInfo"
                          >创建收藏夹</n-button
                        >
                      </div>
                    </template>
                  </n-card>
                </n-modal>

                <!--收藏模态框2-->
                <n-config-provider :theme-overrides="themeOverrides">
                  <n-modal v-model:show="showModal2">
                    <n-card :style="FavoriteModalCard">
                      <template #header>
                        <div class="FavoriteModalCardHeaderH1">
                          创建新收藏夹
                        </div>
                      </template>
                      <n-space vertical>
                        <n-input
                          v-model:value="favoriteTitle"
                          type="text"
                          placeholder="收藏标题"
                        />

                        <n-input
                          v-model:value="favoriteDescribe"
                          type="textarea"
                          placeholder="收藏描述"
                        />
                      </n-space>
                      <template #footer>
                        <n-space justify="center">
                          <span
                            ><n-button
                              text-color="#8590a6"
                              color="#8590a6"
                              ghost
                              @click="backtomodal1"
                              >返回
                            </n-button></span
                          >
                          <span
                            ><n-button
                              text-color="white"
                              color="#056de8"
                              :disabled="!favoriteTitle"
                              @click="CreateNewFavorite(favoriteTitle)"
                              >创建</n-button
                            >
                          </span>
                        </n-space>
                      </template>
                    </n-card>
                  </n-modal>
                </n-config-provider>

                <n-button v-if="is_active_expand === true">收起 </n-button>
              </n-space>
            </template>
          </n-card>
        </div>

        <!---分割线-->
      </div>

      <!-- <n-pagination v-model:page="page" :page-count="20" /> -->
    </div>
  </n-config-provider>
</template>

<script>
import { is } from "date-fns/locale";
import { defineComponent, ref } from "vue";

export default {
  setup() {
    const themeOverrides = {
      Input: {
        borderFocus: "1px solid #8590a6",
        boxShadowFocus: "0 0 0 2px rgba(133, 144, 166, 0.2)",
        borderHover: "1px solid #8590a6",
        caretColor: "#8590a6FF",
      },
    };
    const items = ref([
      { id: 1, title: "收藏夹1", is_favoritebutton_active: false },
      { id: 2, title: "收藏夹2", is_favoritebutton_active: false },
      { id: 3, title: "收藏夹3", is_favoritebutton_active: false },
    ]);
    const cards = ref([1, 2, 3, 4]);

    return {
      items,
      themeOverrides,
      cards,
      showModal1: ref(false),
      showModal2: ref(false),
      favoriteTitle: ref(null),
      favoriteDescribe: ref(null),
    };
  },
  data() {
    return {
      is_active_expand: false,
      is_likebutton_active: false,
      is_dislikebutton_active: false,
      FavoriteModalCard: {
        width: "400px",
        height: "400px",
        overflow: "auto",
      },
    };
  },
  methods: {
    likebuttonclick() {
      this.is_likebutton_active = !this.is_likebutton_active;
      if (this.is_dislikebutton_active === true) {
        this.is_dislikebutton_active = false;
      }
    },
    dislikebuttonclick() {
      this.is_dislikebutton_active = !this.is_dislikebutton_active;
      if (this.is_likebutton_active === true) {
        this.is_likebutton_active = false;
      }
    },
    expandclick() {
      this.is_active_expand = !this.is_active_expand;
    },
    collapsebuttonclick() {
      this.is_active_expand = !this.is_active_expand;
    },
    commentsclick() {},
    favoritebuttonclick(item) {
      item.is_favoritebutton_active = !item.is_favoritebutton_active;
    },
    ShowCreateFavoriteInfo() {
      this.showModal1 = false;
      //打开新modal
      this.$nextTick(() => {
        this.showModal2 = true;
      });
    },
    backtomodal1() {
      this.showModal2 = false;
      this.$nextTick(() => {
        this.showModal1 = true;
      });
    },
    CreateNewFavorite(titlename) {
      this.items.push({
        id: this.items.length + 1, //当前收藏夹数量+1
        title: titlename,
        is_favoritebutton_active: false,
      });
      this.backtomodal1();
    },
  },
};
</script>

<style lang="less">
.FavoriteModalCardHeaderH1 {
  font-size: 25px;
  font-weight: bold;
  text-align: center;
}
.FavoriteModalCardHeaderH2 {
  font-size: 14px;
  text-align: center;
  color: #8590a6;
}
.FavoriteModalCardFooter {
  text-align: center;
}
.FavoriteModalCloseButton {
  position: absolute;
  right: 0px;
}
.bbs {
  background-color: rgb(233, 232, 235);
  min-height: calc(100vh);

  // 换页
  // .n-pagination{
  //   justify-content: center;
  //   align-items: center;
  //   // width: 40%;
  //   // background-color: rgb(255, 255, 255);
  //   height: 10%;
  //   // left: 30%;
  //   top: 800px;
  // }
  .n-card__action {
    align-items: center;
    background-color: white;
  }
  .main-column {
    margin-bottom: 0px;
    width: 70%;
    left: 15%;

    // .title{
    //   font-weight: bold;
    // }

    // 按钮
    .el-link {
      margin-right: 8px;
    }
    .el-link .el-icon--right.el-icon {
      vertical-align: text-bottom;
    }

    // 文字
    .content {
      font-size: medium;
      text-decoration: none;
    }
    .author {
      font-size: smaller;
    }
  }
}
</style>
