import http from "../utils/http/http.js";

const getCommentList = (data) => {
  return http.get("/admin/comments");
};
const delComment = (data) => {
  const comment_id = { comment_id: data.id };
  return http.del("/admin/comments/delete", comment_id);
};
const getUserDetail = (data) => {
  return http.get("/user/detail", data);
};
export default {
  getCommentList,
  delComment,
};
