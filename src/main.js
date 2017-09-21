// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// General
import SmoothScroll from 'smooth-scroll'
// eslint-disable-next-line
const scroll = new SmoothScroll('a[href*="#"]')
// Vue
import Vue from 'vue'
import router from './router'
// Buefy
import Buefy from 'buefy'
import 'buefy/lib/buefy.css'
Vue.use(Buefy)
// Highcharts
import VueHighcharts from 'vue-highcharts'
import Highcharts from 'highcharts/highcharts'
import HighchartsTheme from './hightcharts-theme'
import loadTreemap from 'highcharts/modules/treemap'
import noData from 'highcharts/modules/no-data-to-display.js'
Highcharts.setOptions(HighchartsTheme)
loadTreemap(Highcharts)
noData(Highcharts)
Highcharts.setOptions({
  lang: {
    noData: 'Нет данных для отображения'
  }
})
Vue.use(VueHighcharts)
// App
import App from './App'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
