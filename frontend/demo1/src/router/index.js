import { createRouter, createWebHistory } from "vue-router";

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
          component: () => import("../views/bbs.vue"),
        },
        {
          path: "/profile",
          component: () => import("../views/profile.vue"),
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
  ],
});

export default router;
