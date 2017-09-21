<template>
  <div id="app">
    <navigation></navigation>
    <router-view></router-view>
  </div>
</template>

<script>
import Navigation from './components/Navigation'
import openData from './openbudget.json'
import { handleData, doingStaff } from './utility'

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
//    console.log(data)
    // eslint-disable-next-line
    let test = doingStaff(data)
//    console.log(test)
  }
}
</script>

<style lang="scss">
// Import Bulma's core
@import "~bulma/sass/utilities/_all"; // Set your colors
@import "~bulma";
@import "~buefy/src/scss/buefy";
  .section--gray-bg {
    background-color: #f5f5f5;
  }

  .align-center {
    justify-content: center;
  }
</style>

