import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import NotFound from '@/views/NotFound'
import About from '@/views/About'
// import DataTable from '@/views/DataTable'
// import Table from '@/views/TestTable'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    { path: '*', name: 'notfound', component: NotFound },
    { path: '/about', name: 'notfound', component: About }
    // { path: '/test', name: 'test', component: DataTable },
    // { path: '/table', name: 'table', component: Table }
  ]
})
