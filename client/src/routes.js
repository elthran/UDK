const CountyHome = () => import(/* webpackChunkName: "CountyHome" */ '@/components/CountyHome');
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
    path: '*',
    redirect: { name: 'county.home' },
  },
];
