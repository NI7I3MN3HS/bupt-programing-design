<template>
  <div class="bbs">
    <div class="post">
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

export default defineComponent({
  setup() {
    return {
      page: ref(2),
    };
  },
});
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
    width: 70%;
    background-color: rgb(216, 54, 54);
    height: 100%;
    left: 15%;
    top: 2%;

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

    .first {
      width: 96%;
      height: 150px;

      left: 2%;
      top: 20px;
    }

    .second {
      width: 96%;
      height: 150px;
      left: 2%;
      top: 300px;
    }
  }
}
</style>
