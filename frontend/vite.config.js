import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  publicPath: "/",
  cacheDir: "node_modules/.vite",
  base: "/",
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
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
