<template>
  <div id="app">
    <navigation></navigation>
    <router-view></router-view>
  </div>
</template>

<script>
import Navigation from './components/Navigation'
import openData from './openbudget.json'
import { handleData, doingStaff, setupMap } from './utility'
export default {
  name: 'app',
  components: {
    Navigation
  },
  data () {
    return {
      income: null,
      expenses: null,
      deficit: null
    }
  },
  methods: {
  },
  created () {
    let data = handleData(openData)
    let q = setupMap()
    console.log(q)
    doingStaff(data)
  }
}
</script>

<style lang="scss">
// Import Bulma's core
@import "~bulma/sass/utilities/_all"; // Set your colors
@import "~bulma";
@import "~buefy/src/scss/buefy";
$primary: #FFFFFF;
$primary-invert: findColorInvert($primary);
$table-cell-heading-color: red;
$table-head-cell-color: blue;
.section--gray-bg {
  background-color: #f5f5f5;
}

.align-center {
  justify-content: center;
}
table.table {
  font-size: 13px;
  th {
    background-color: #1A535C;
    color: #ffffff;
  }
  &.is-striped tbody tr:not(.is-selected):nth-child(even) {
    background-color: #f3fffd;
  }
}
</style>
