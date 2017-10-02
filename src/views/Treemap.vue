<template>
  <div class="section section--gray-bg">
    <div id="treemap" class="content">
      <div class="container">
        <div class="columns">
          <div class="column">
            <h2 class="has-text-centered">Доходы/Расходы по видам</h2>
            <div class="select">
              <select v-model="year">
                <option v-for="(year, index) in availableYears" :value="year" :key="index">{{ year }}</option>
              </select>
            </div>
            <div class="select">
              <select v-model="type">
                <option v-for="(item, index) in types" :value="item" :key="index">{{ item }}</option>
              </select>
            </div>
            <div class="select">
              <select v-model="budget">
                <option v-for="(item, index) in budgetList" :value="item" :key="index">{{ item }}</option>
              </select>
            </div>
          </div>
        </div>
        <div class="columns">
          <div class="column">
            <highcharts :options="sortedData" ref="highcharts"></highcharts>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import openData from '../openbudget.json'
  import _ from 'lodash'
  import Highcharts from 'highcharts'

  const filterData = (by, year, level) => {
    let data = _(openData)
      .filter((item) => {
        return item['Доходы / Расходы'] === by && item['Год'] === year && item['Уровень бюджета'] === level
      })
      .value()
    let group = _(openData)
      .filter((item) => {
        return item['Доходы / Расходы'] === by && item['Год'] === year && item['Уровень бюджета'] === level
      })
      .uniqBy('Наша классификация')
      .value()
//    console.log(data)
    let filteredData = []
    data.forEach((item) => {
      if (_.some(filteredData, {parent: item['Наша классификация'], name: item['Функциональная группа']})) {
        filteredData.forEach((i, idx) => {
          i.value += +item['Сумма']
        })
      } else {
        filteredData.push({
          value: +`${item['Сумма']}`,
          parent: item['Наша классификация'],
          name: item['Функциональная группа']
        })
      }
    })
    group = group.map((item, index) => {
      return {
        id: item['Наша классификация'],
        name: item['Наша классификация'],
        color: Highcharts.getOptions().colors[index]
      }
    })
    data = filteredData.concat(group)
    return data
  }

  export default {
    name: 'treemap',
    data () {
      return {
        series: {
          type: 'treemap',
          layoutAlgorithm: 'stripes',
          alternateStartingDirection: true,
          levels: [{
            level: 1,
            layoutAlgorithm: 'strip',
            dataLabels: {
              enabled: true,
              align: 'left',
              verticalAlign: 'top',
              style: {
                fontSize: '15px',
                fontWeight: 'bold'
              }
            }
          }],
          tooltip: {
            headerFormat: '<span style="font-size: 22px">{point.key}</span><br/>',
            pointFormat: '<span style="font-size: 13px">{point.value} </span>млрд. тенге'
          }
        },
        year: 2016,
        budget: 'Республиканский',
        budgetList: ['Республиканский', 'Государственный', 'Консолидированный'],
        type: 'Доходы',
        types: ['Доходы', 'Расходы']
      }
    },
    computed: {
      sortedData () {
        let options = {
          series: [{
            ...this.series,
            data: filterData(this.type, this.year, this.budget)
          }],
          title: {
            text: ''
          }
        }
        return options
      },
      availableYears () {
        return _(openData).map('Год').uniq().sort((a, b) => { return b - a }).forEach(item => { return { item } })
      }
    }
  }
</script>
