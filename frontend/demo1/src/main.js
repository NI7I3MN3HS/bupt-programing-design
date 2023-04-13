import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import naive from 'naive-ui'
import ElementPlus from 'element-plus'

import './assets/base.less'

const app = createApp(App)

app.use(createPinia())
   .use(router)
   .use(naive)
   .use(ElementPlus)
   .mount('#app')
