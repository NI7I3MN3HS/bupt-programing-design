//帖子状态管理
import { defineStore } from "pinia";
import axios from "axios";
import useAuthStore from "@/stores/modules/AuthStore";
import useUserStore from "@/stores/modules/UserStore";

//导入请求状态
const authStore = useAuthStore();
//导入个人用户状态
const userStore = useUserStore();

//定义请求头
const UserClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${authStore.token}`,
  },
});

const usePostStore = defineStore("post", {
  state: () => {
    return {
      post_id: 0, //帖子id
      post_user_id: "", //发帖用户id
      post_title: "", //帖子标题
      post_content: "", //帖子内容
      post_comment: [], //评论
      post_like: 0, //点赞数
      post_dislike: 0, //点踩数
      post_create_time: "", //创建时间
      post_update_time: "", //更新时间
    };
  },
  actions: {
    //设置帖子标题
    SetPostTitle(title) {
      this.post_title = title;
    },
    //设置帖子内容
    SetPostContent(content) {
      this.post_content = content;
    },
    //获取帖子信息
    GetPostInfo(postid) {
      axios
        .get(`/post/${postid}`)
        .then((response) => {
          this.post_id = response.data.id;
          this.post_user_id = response.data.user_id;
          this.post_title = response.data.title;
          this.post_content = response.data.content;
          this.post_comment = response.data.post_comment;
          this.post_like = response.data.post_like;
          this.post_dislike = response.data.post_dislike;
          this.post_create_time = response.data.create_time;
          this.post_update_time = response.data.update_time;
        })
        .catch((error) => {
          console.error(error);
        });
      axios
        .get(`/comment/${postid}`)
        .then((response) => {
          this.post_comment = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    //创建帖子
    CreatePost() {
      if (authStore.is_Authenticated) {
        //后期改一下路径
        UserClient.post("/post/create", {
          title: this.post_title,
          content: this.post_content,
        })
          .then((response) => {
            console.log(response);
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        alert("请先登录");
      }
    },
  },
});

export default usePostStore;
