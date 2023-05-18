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
      post_user_id: 0, //发帖用户id
      post_author_name: "", //发帖用户名
      post_author_avatar_url: "", //发帖用户头像
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
    //获取帖子信息：异步写法
    async GetPostInfoAsync(postid) {
      const response = await axios.get(`/post/${postid}`);
      this.post_id = response.data.id;
      this.post_user_id = response.data.user_id;
      this.post_title = response.data.title;
      this.post_content = response.data.content;
      this.post_comment = response.data.post_comment;
      this.post_like = response.data.post_like;
      this.post_dislike = response.data.post_dislike;
      this.post_create_time = response.data.create_time;
      this.post_update_time = response.data.update_time;
      const comment = await axios.get(`/comment/${postid}`);
      this.post_comment = comment.data;
      const author = await axios.get(`/user/${response.data.user_id}`);
      this.post_author_name = author.data.username;
      this.post_author_avatar_url = author.data.avatar_url;
    },
  },
});

export default usePostStore;
