<template>
  <div class="home-page">
    <parallax sectionHeight=20>
    <div class="hero">
      <div class="container">
        <div class="columns">
          <div class="column">
            <div class="content">
              <h1 class="has-text-centered">В 2016 государство Республики Казахстан <br>из бюджета потратило <span class="highlight">{{ totalCount }}</span> миллиарда тенге</h1>
              <h3 class="has-text-centered">OpenBudget.kz нацелен на обеспечение доступа к информации о бюджетной системе Республики Казахстан, бюджетном процессе в Республике Казахстан, данным бюджетной системы, Национального фонда Республики Казахстана, внебюджетных фондов (ЕНПФ, ГФСС, ФСМС), квазигосударственного сектора.</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
    </parallax>
    <total></total>
    <expenses></expenses>
    <dynamic></dynamic>
    <levels></levels>
    <maps></maps>
  </div>
</template>

<script>
  import Total from './Total'
  import Expenses from './Treemap'
  import Dynamic from './Dynamic'
  import Levels from './Levels'
  import Parallax from 'vue-parallaxy'
  import Maps from './Maps'
  import openData from '../openbudget.json'

  import {sumBy, filter} from 'lodash'

  export default {
    name: 'home',
    components: {
      Parallax,
      Total,
      Expenses,
      Dynamic,
      Levels,
      Maps
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
              item['Уровень бюджета'] === 'Государственный'
          }), (o) => { return o['Сумма'] })
      }
    }
  }
</script>

<style lang="scss" type="text/scss" scoped>
  .hero {
    background: url("../assets/images/Khan-Shatyr.jpg") no-repeat center center;
    background-size: cover;
    height: 700px;
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
    .highlight {
      color: #01D1B2;
      position: relative;
      font-size: 1.5em;
      font-weight: bold;
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
