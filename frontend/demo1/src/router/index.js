import { createRouter, createWebHistory } from "vue-router";
import useAuthStore from "../stores/modules/AuthStore";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "layout",
      component: () => import("../views/layout.vue"),
      children: [
        {
          path: "",
          name: "index",
          component: () => import("../views/Post/index.vue"),
        },
        {
          path: "/user/:id",
          component: () => import("../views/Profile/index.vue"),
        },
        {
          path: "/profile/edit1",
          component: () => import("../views/profileedit/userinformation.vue"),
        },
        {
          path: "/profile/edit2",
          component: () =>
            import("../views/profileedit/accountinformation.vue"),
        },
        {
          path: "/profile/edit3",
          component: () => import("../views/profileedit/password.vue"),
        },
        {
          path: "/WritePost",
          component: () => import("../views/WritePost.vue"),
          meta: { requiresAuth: true },
        },
        {
          path: "/post/:id",
          name: "post",
          component: () => import("../views/Post/Post.vue"),
        },
        {
          path: "/notice",
          component: () => import("../views/Notice/index.vue"),
        },
      ],
    },
    {
      path: "/loginandregister",
      name: "loginandregister",
      component: () => import("../views/LoginAndRegister.vue"),
    },
    {
      path: "/ResetPassword",
      name: "ResetPassword",
      component: () => import("../views/ResetPassword.vue"),
    },
    {
      path: "/upload",
      name: "upload",
      component: () => import("../views/upload.vue"),
    },
    {
      path: "/user/UserNotFound",
      name: "UserNotFound",
      component: () => import("../views/Profile/user404.vue"),
    },
  ],
});

router.beforeEach((to, from) => {
  const authStore = useAuthStore();
  // 而不是去检查每条路由记录
  // to.matched.some(record => record.meta.requiresAuth)
  if (to.meta.requiresAuth && !authStore.is_Authenticated) {
    // 此路由需要授权，请检查是否已登录
    // 如果没有，则重定向到登录页面
    return {
      path: "/loginandregister",
      // 保存我们所在的位置，以便以后再来
      query: { redirect: to.fullPath },
    };
  }
});

export default router;
