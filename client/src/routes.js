const Ping = () => import(/* webpackChunkName: "Ping" */ '@/components/Ping');

export default [
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
];
