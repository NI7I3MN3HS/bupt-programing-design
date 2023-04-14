<template>
  <div class="bbs">
    <div class="main-column">
      <!---card模版-->
      <n-card title="标题" class="first">
        <template #header-extra> </template>
        <el-link class="content" href="https://element-plus.org">
          内容
        </el-link>
        <template #footer>
          <div class="author">发布人</div>
        </template>
        <template #action>
          <n-space>
            <n-button
              :class="
                is_likebutton_active === true ? 'like_active' : 'like_default'
              "
              :color="
                is_likebutton_active === true
                  ? '#056de8'
                  : 'rgba(5, 109, 232, 0.15)'
              "
              :text-color="is_likebutton_active === true ? 'white' : '#056de8'"
              @click="likebuttonclick"
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
              赞同
            </n-button>

            <n-button
              :class="
                is_dislikebutton_active === true
                  ? 'like_active'
                  : 'like_default'
              "
              :color="
                is_dislikebutton_active === true
                  ? '#056de8'
                  : 'rgba(5, 109, 232, 0.15)'
              "
              :text-color="
                is_dislikebutton_active === true ? 'white' : '#056de8'
              "
              @click="dislikebuttonclick"
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
              反对
            </n-button>
          </n-space>
        </template>
      </n-card>
      <!---分割线-->
      <n-card title="标题" class="first">
        <template #header-extra>
          <n-button strong secondary round type="error"> 点赞 </n-button>
        </template>
        <el-link class="content" href="https://element-plus.org">
          内容
        </el-link>
        <template #footer>
          <div class="author">发布人</div>
        </template>
        <template #action>
          <n-button strong secondary type="info"> 评论 </n-button>
        </template>
      </n-card>

      <n-card title="标题" class="second">
        <template #header-extra>
          <n-button strong secondary round type="error"> 点赞 </n-button>
        </template>
        <el-link class="content" href="https://element-plus.org">
          内容
        </el-link>
        <template #footer>
          <div class="author">发布人</div>
        </template>
        <template #action>
          <n-button strong secondary type="info"> 评论 </n-button>
        </template>
      </n-card>
    </div>

    <!-- <n-pagination v-model:page="page" :page-count="20" /> -->
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";

export default {
  data() {
    return {
      is_likebutton_active: false,
      is_dislikebutton_active: false,
    };
  },
  methods: {
    likebuttonclick() {
      this.is_likebutton_active = !this.is_likebutton_active;
    },
    dislikebuttonclick() {
      this.is_dislikebutton_active = !this.is_dislikebutton_active;
    },
  },
};
</script>

<style lang="less">
.bbs {
  background-color: rgb(233, 232, 235);

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

  .post {
    margin-bottom: 10px;
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
