import { createRouter, createWebHashHistory } from "vue-router";
import Cookies from "js-cookie";
const routes = [
  {
    path: "/",
    redirect: "/home",
  },
  {
    path: "/login",
    name: "login",
    meta: {
      title: "登录",
    },
    component: () => import("../view/Login.vue"),
  },
  {
    path: "/home",
    name: "主页",
    meta: {
      title: "主页",
    },
    component: () => import("../view/Home.vue"),
    redirect: "/index",
    children: [
      {
        path: "/index",
        meta: {
          title: "首页",
        },
        component: () => import("../view/Welcome.vue"),
      },
      {
        path: "/user/list",
        meta: {
          title: "用户管理",
        },
        component: () => import("../view/user/Index.vue"),
      },
      {
        path: "/post/list",
        meta: {
          title: "帖子管理",
        },
        component: () => import("../view/post/Index.vue"),
      },
      {
        path: "/comment/list",
        meta: {
          title: "评论管理",
        },
        component: () => import("../view/comment/Index.vue"),
      },
      {
        path: "/user/detail",
        meta: {
          title: "用户详情",
        },
        component: () => import("../view/user/Detail.vue"),
      },
    ],
  },
];
const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
// 挂载路由导航守卫：to表示将要访问的路径，from表示从哪里来，next是下一个要做的操作
router.beforeEach((to, from, next) => {
  // 修改页面 title
  if (to.meta.title) {
    document.title = "BUPTHUB MANAGER - " + to.meta.title;
  }
  // 放行登录页面
  if (to.path === "/login") {
    return next();
  }
  // 获取token
  const token = Cookies.get("access_token");
  if (!token) {
    return next("/login");
  } else {
    next();
  }
  return next();
});

// 导出路由
export default router;
