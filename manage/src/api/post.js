import http from "../utils/http/http.js";

const getPostList = (data) => {
  return http.get("/admin/posts");
};
const delPost = (data) => {
  const post_id = { post_id: data.id };
  return http.del("/admin/posts/delete", post_id);
};
const getUserDetail = (data) => {
  return http.get("/user/detail", data);
};
export default {
  getPostList,
  delPost,
};
