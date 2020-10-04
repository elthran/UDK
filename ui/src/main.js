import Vue from 'vue'
import VueRouter from 'vue-router'

import App from '@/App'
import routes from '@/routes.js'

Vue.use(VueRouter)

const router = new VueRouter({
  routes,
  base: process.env.BASE_URL || '/',
  mode: 'history',
})

const app = new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
