import http from "../utils/http/http.js";

const login = (data) => {
  return http.post("/admin/", data);
};
const getUserList = (data) => {
  return http.get("/admin/users");
};
const saveUser = (data) => {
  return http.post("/user/save", data);
};
const delUser = (data) => {
  const user_id = { user_id: data.id };
  return http.del("/admin/users/delete", user_id);
};
const getUserDetail = (data) => {
  return http.get("/user/detail", data);
};
export default {
  login,
  getUserList,
  saveUser,
  delUser,
  getUserDetail,
};
