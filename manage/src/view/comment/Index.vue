<template>
  <div>
    <el-card>
      <!--
      <el-input
        style="width: 440px"
        @clear="searchUser"
        clearable
        v-model="searchForm.name"
        placeholder="请输入用户姓名"
        class="input-with-select"
      >
        <template #append>
          <el-button icon="Search" @click="searchUser" />
        </template>
      </el-input>
      -->
      <el-table :data="tableData" border style="width: 100%; margin-top: 20px">
        <el-table-column prop="id" label="评论id" width="80" />
        <el-table-column prop="content" label="评论内容" width="180" />
        <el-table-column prop="user_id" label="发布评论的用户id" width="180" />
        <el-table-column
          prop="post_id"
          label="该评论所属的帖子id"
          width="180"
        />
        <el-table-column label="操作" width="330">
          <template #default="scope">
            <el-button
              type="danger"
              size="small"
              @click="deleteUser(scope.row.id)"
              >删除</el-button
            >
            <!--
            <el-button
              size="small"
              @click="
                () =>
                  router.push({
                    path: '/user/detail',
                    query: { id: scope.row.id },
                  })
              "
              >详情</el-button
            >
            -->
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页 
      <el-pagination
        style="margin-top: 20px"
        :current-page="searchForm.current"
        :page-size="searchForm.size"
        :page-sizes="[10, 20, 30, 40]"
        layout="->,total, sizes, prev, pager, next, jumper"
        :total="total"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />
      -->
    </el-card>
  </div>
</template>

<script setup>
import commentApi from "../../api/comment";
import { onMounted, reactive, ref } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import { useRouter } from "vue-router";
const router = useRouter();
// Dom 挂载之后
onMounted(() => {
  getCommentList();
});
// 用户数据
let tableData = ref([]);
let total = ref(0);
// 搜索条件
const searchForm = reactive({
  current: 1,
  size: 10,
  name: "",
});
// 获取用户列表
const getCommentList = async () => {
  const res = await commentApi.getCommentList(searchForm);
  console.log(res);
  tableData.value = res.data;
  total.value = res.data.data.total;
};
const handleSizeChange = (size) => {
  searchForm.size = size;
  getUserList();
};
const handleCurrentChange = (current) => {
  searchForm.current = current;
  getUserList();
};
const searchUser = () => {
  searchForm.current = 1;
  getUserList();
};
// 删除用户
const deleteUser = (id) => {
  ElMessageBox.confirm("确定要删除该用户信息吗?", {
    confirmButtonText: "确定",
    cancelButtonText: "取消",
    type: "warning",
  })
    .then(async () => {
      const res = await commentApi.delComment({ id: id });
      if (res.data.success) {
        ElMessage.success("删除成功");
        getCommentList();
      } else {
        ElMessage.error("删除失败");
      }
    })
    .catch(() => {
      ElMessage({
        type: "info",
        message: "取消删除",
      });
    });
};
</script>

<style lang="scss" scoped></style>
