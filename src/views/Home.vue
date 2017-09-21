<template>
  <div class="home-page">
    <div class="hero">
      <div class="container">
        <div class="columns">
          <div class="column">
            <div class="content">
              <h1 class="has-text-centered">In 2016, the Kazakhstan government <br>spent {{ totalCount }} billion tenge</h1>
              <h3 class="has-text-centered">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
    <total></total>
    <expenses></expenses>
    <dynamic></dynamic>
    <levels></levels>
  </div>
</template>

<script>
  import Total from './Total'
  import Expenses from './Treemap'
  import Dynamic from './Dynamic'
  import Levels from './Levels'

  import openData from '../openbudget.json'

  import {sumBy, filter} from 'lodash'

  export default {
    name: 'home',
    components: {
      Total,
      Expenses,
      Dynamic,
      Levels
    },
    data () {
      return {
        total: 0
      }
    },
    computed: {
      totalCount () {
        return sumBy(filter(openData,
          (item) => {
            return item['Доходы / Расходы'] === 'Расходы' &&
              item['Год'] === 2016 &&
              item['Уровень бюджета'] === 'Республиканский'
          }), (o) => { return o['Сумма'] })
      }
    }
  }
</script>

<style lang="scss" type="text/scss" scoped>
  .hero {
    background: url("../assets/images/akorda.jpg") no-repeat center center;
    background-size: cover;
    height: 500px;
    display: flex;
    padding: 10% 0;
    position: relative;
    h1 {
      color: #ffffff;
      position: relative;
      z-index: 1;
      font-size: 3em;
    }
    h3 {
      color: #ffffff;
      position: relative;
      z-index: 1;
    }
    &:after {
      content: '';
      position: absolute;
      width: 100%;
      height: 100%;
      left: 0;
      top: 0;
      background: rgba(0, 0, 0, 0.58);
    }
  }
</style>
