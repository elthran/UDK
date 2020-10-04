import NotFoundComponent from '@/components/NotFoundComponent'

const CountyInterface = () =>
  import(/* webpackChunkName: "CountyInterface" */ '@/pages/CountyInterface')

export default [
  {
    path: '/',
    // redirect: { name: 'CountyInterface' },
  },
  {
    path: '/county/home',
    name: 'CountyInterface',
    component: CountyInterface,
  },
  {
    path: '*',
    name: '404',
    component: NotFoundComponent,
  },
]
