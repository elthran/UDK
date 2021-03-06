const Kingdom = () => import(/* webpackChunkName: "Kingdom" */ '@/components/Kingdom');

const CountyHome = () => import(/* webpackChunkName: "CountyHome" */ '@/components/CountyHome');
const CountyEconomy = () => import(/* webpackChunkName: "CountyEconomy" */ '@/components/CountyEconomy');
const CountyInfrastructure = () => import(/* webpackChunkName: "CountyInfrastructure" */ '@/components/CountyInfrastructure');
const CountyMilitary = () => import(/*webpackChunkName: "CountyMilitary" */ '@/components/CountyMilitary');

const TempLogin = () => import(/* webpackChunkName: "TempLogin" */ '@/components/TempLogin');
const Ping = () => import(/* webpackChunkName: "Ping" */ '@/components/Ping');


export default [
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/kingdom',
    name: 'kingdom',
    component: Kingdom,
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
    path: '/county/military',
    name: 'county.military',
    component: CountyMilitary,
  },
  {
    path: '/authentication/login',
    name: 'authentication.login',
    component: TempLogin,
  },
  {
    path: '*',
    redirect: { name: 'county.home' },
  },
];
