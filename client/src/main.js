import Vue from 'vue';
import VueRouter from 'vue-router';

import App from '@/App.vue';
import routes from '@/routes';
import '@/assets/css/global.css'

// remove this when a real login page exists
import http from '@/http-client';

Vue.config.productionTip = false;
Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});


// FIXME: move to a api and call on the login page
http.get('/api/session/login/client_user')
  .then((response) => {
    window.CURRENT_USER_ID = response.data.user.id
  })
  .catch((response) => console.log('response', response))


new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
