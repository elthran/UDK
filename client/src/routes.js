const CountyHome = () => import(/* webpackChunkName: "CountyHome" */ '@/components/CountyHome');
const CountyEconomy = () => import(/* webpackChunkName: "CountyEconomy" */ '@/components/CountyEconomy');
const CountyInfrastructure = () => import(/* webpackChunkName: "CountyInfrastructure" */ '@/components/CountyInfrastructure');
const Ping = () => import(/* webpackChunkName: "Ping" */ '@/components/Ping');

export default [
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/county/home',
    name: 'county.home',
    component: CountyHome,
  },
  {
    path: '/county/economy',
    name: 'county.economy',
    component: CountyEconomy,
  },
  {
    path: '/county/infrastructure',
    name: 'county.infrastructure',
    component: CountyInfrastructure,
  },
  {
    path: '*',
    redirect: { name: 'county.home' },
  },
];
