import Vue from 'vue'
import VueRouter from 'vue-router'

import App from '@/App.vue'
import routes from '@/routes'
import '@/assets/css/global.css'

Vue.config.productionTip = false
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.name !== 'authentication.login' && !window.localStorage.getItem('currentUserId')) {
    next({ name: 'authentication.login' })
  } else {
    next()
  }
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
