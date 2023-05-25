import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],

  publicPath: "./",
  base: "./",
  server: {
    open: false,
    port: 3000,
    proxy: {
      "/api": {
        target: "/api", //
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
  // 构建输出配置
  build: {
    outDir: "./dist",
    target: "modules",
    assetsDir: "assets",
    assetsInlineLimit: 360000,
  },
});
