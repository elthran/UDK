import Vue from 'vue';
import VueRouter from 'vue-router';

import App from '@/App';
import routes from '@/routes';

Vue.config.productionTip = false;
Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
