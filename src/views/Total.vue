<template>
  <div class="section">
    <div id="total">
      <div class="container">
        <div class="columns">
          <div class="column">
            <div class="content">
              <h2 class="has-text-centered">
                Бюджет
              </h2>
            </div>
          </div>
        </div>

        <b-tabs type="is-boxed is-centered" size="is-medium">
          <b-tab-item label="Республиканский">
            <br>
            <div class="columns">
              <div class="column is-2">
                <br>
                <b-field>
                  <b-radio-button
                    v-model="republicanType"
                    native-value="Доходы">
                    <span>Доходы</span>
                  </b-radio-button>
                  <b-radio-button
                    v-model="republicanType"
                    native-value="Расходы">
                    <span>Расходы</span>
                  </b-radio-button>
                </b-field>
                <br>
                <div class="columns">
                  <div class="column">
                    <b-checkbox @input="repubCheckAll">Отметить все</b-checkbox>
                  </div>
                </div>
                <div class="columns is-multiline">
                  <div class="column is-half" v-for="(year, index) in repubAvailableYears" :value="year" :key="index">
                    <b-checkbox v-model="republicanYears" :native-value="year">{{ year }}</b-checkbox>
                  </div>
                </div>
              </div>

              <div class="column is-10">
                <div class="content">
                  <highcharts :options="sortedRepublican" ref="highcharts"></highcharts>
                </div>
              </div>
            </div>
          </b-tab-item>
          <b-tab-item label="Государственный">
            <br>
            <div class="columns">
              <div class="column is-2">
                <br>
                <b-field>
                  <b-radio-button
                    v-model="stateType"
                    native-value="Доходы">
                    <span>Доходы</span>
                  </b-radio-button>
                  <b-radio-button
                    v-model="stateType"
                    native-value="Расходы">
                    <span>Расходы</span>
                  </b-radio-button>
                </b-field>
                <br>
                <div class="columns">
                  <div class="column">
                    <b-checkbox @input="stateCheckAll">Отметить все</b-checkbox>
                  </div>
                </div>
                <div class="columns is-multiline">
                  <div class="column is-half" v-for="(year, index) in stateAvailableYears" :value="year" :key="index">
                    <b-checkbox v-model="stateYears" :native-value="year">{{ year }}</b-checkbox>
                  </div>
                </div>
              </div>
              <div class="column is-10">
                <div class="content">
                  <highcharts :options="sortedState" ref="highcharts"></highcharts>
                </div>
              </div>
            </div>
          </b-tab-item>
          <b-tab-item label="Консолидированный">
            <br>
            <div class="columns">
              <div class="column is-2">
                <br>
                <b-field>
                  <b-radio-button
                    v-model="consolidatedType"
                    native-value="Доходы">
                    <span>Доходы</span>
                  </b-radio-button>
                  <b-radio-button
                    v-model="consolidatedType"
                    native-value="Расходы">
                    <span>Расходы</span>
                  </b-radio-button>
                </b-field>
                <br>
                <div class="columns">
                  <div class="column">
                    <b-checkbox @input="consCheckAll">Отметить все</b-checkbox>
                  </div>
                </div>
                <div class="columns is-multiline">
                  <div class="column is-half" v-for="(year, index) in consAvailableYears" :value="year" :key="index">
                    <b-checkbox v-model="consolidatedYears" :native-value="year">{{ year }}</b-checkbox>
                  </div>
                </div>
              </div>

              <div class="column is-10">
                <div class="content">
                  <!--<div class="select">-->
                  <!--<select v-model="incomesYear">-->
                  <!--<option v-for="(year, index) in availableYears" :value="year" :key="index">{{ year }}</option>-->
                  <!--</select>-->
                  <!--</div>-->
                  <highcharts :options="sortedConsolidated" ref="highcharts"></highcharts>
                </div>
              </div>
            </div>
          </b-tab-item>
        </b-tabs>
      </div>
    </div>
  </div>
</template>

<script>
  import openData from '../converted-data.json'
  import _ from 'lodash'

  const filterData = (by, type, year) => {
    let sortedYears = year.sort((a, b) => { return b - a })
    let data = null
    data = _.filter(openData, item => item['Уровень бюджета'] === by)
    data = _.filter(data, item => item['Доходы / Расходы'] === type)
    data = _.filter(data, item => {
      return sortedYears.includes(item['Год'])
    })
    data = _.groupBy(data, item => item['Наша классификация'])
    data = _.map(data, (item, key) => {
      let tmp = []
      item.forEach(e => {
        sortedYears.forEach((y, i) => {
          if (y === e['Год']) {
            if (!tmp[i]) {
              tmp[i] = e['Сумма'] ? e['Сумма'] : 0
            } else {
              tmp[i] += e['Сумма'] ? e['Сумма'] : 0
            }
          } else {
            if (!tmp[i]) {
              tmp[i] = 0
            } else {
              tmp[i] += 0
            }
          }
        })
      })
      return {
        name: key,
        data: tmp.reverse()
      }
    })
    return data
  }

  export default {
    name: 'total',
    data () {
      return {
        types: ['Доходы', 'Расходы'],

        budget: 'Республиканский',
        budgetList: ['Республиканский', 'Государственный', 'Консолидированный'],

        chart: {
          chart: {
            type: 'column',
            height: 700
          },
          xAxis: {
            labels: {
              enabled: false
            }
          },
          yAxis: {
            title: {
              text: null
            },
            labels: {
              format: '{value} млрд. тг'
              // enabled: false
            },
            stackLabels: {
              enabled: true,
              format: '{total} млрд. тг'
            }
          },
          legend: {
            enabled: true,
            align: 'right',
            borderColor: '#01D1B2',
            borderRadius: 4,
            borderWidth: 1
          },
          tooltip: {
            headerFormat: '<b>{series.name}</b><br/>',
            pointFormat: '{point.y} млрд. тг'
          },
          plotOptions: {
            column: {
              stacking: 'normal',
              dataLabels: {
                enabled: true,
                color: 'white',
                formatter () {
                  var val = this.y
                  if (val < 1) {
                    return ''
                  }
                  return val
                }
              }
            }
          }
        },

        consolidatedYears: [2016],
        republicanYears: [2016],
        stateYears: [2016],

        consolidatedType: 'Доходы',
        republicanType: 'Доходы',
        stateType: 'Доходы'
      }
    },
    computed: {
      consAvailableYears () {
        return _(openData).filter(item => item['Уровень бюджета'] === 'Консолидированный')
          .filter(item => item['Доходы / Расходы'] === this.consolidatedType)
          .map('Год').uniq().value().sort((a, b) => { return b - a })
      },
      repubAvailableYears () {
        return _(openData).filter(item => item['Уровень бюджета'] === 'Республиканский')
          .filter(item => item['Доходы / Расходы'] === this.republicanType)
          .map('Год').uniq().value().sort((a, b) => { return b - a })
      },
      stateAvailableYears () {
        return _(openData).filter(item => item['Уровень бюджета'] === 'Государственный')
          .filter(item => item['Доходы / Расходы'] === this.stateType)
          .map('Год').uniq().value().sort((a, b) => { return b - a })
      },
      sortedConsolidated () {
        return {
          ...this.chart,
          series: filterData('Консолидированный', this.consolidatedType, this.consolidatedYears),
          xAxis: {
            categories: this.consolidatedYears.sort((a, b) => { return a - b })
          },
          title: {
            text: this.consolidatedType
          }
        }
      },
      sortedConsolidated1 () {
        return {
          ...this.chart,
          series: filterData('Консолидированный', 'Доходы', this.consolidatedYears),
          xAxis: {
            categories: this.consolidatedYears.sort((a, b) => { return a - b })
          },
          title: {
            text: this.consolidatedType
          }
        }
      },
      sortedConsolidated2 () {
        return {
          ...this.chart,
          series: filterData('Консолидированный', 'Расходы', this.consolidatedYears),
          xAxis: {
            categories: this.consolidatedYears.sort((a, b) => { return a - b })
          },
          title: {
            text: this.consolidatedType
          }
        }
      },
      sortedRepublican () {
        return {
          ...this.chart,
          series: filterData('Республиканский', this.republicanType, this.republicanYears),
          xAxis: {
            categories: this.republicanYears.sort((a, b) => { return a - b })
          },
          title: {
            text: this.republicanType
          }
        }
      },
      sortedState () {
        return {
          ...this.chart,
          series: filterData('Государственный', this.stateType, this.stateYears),
          xAxis: {
            categories: this.stateYears.sort((a, b) => { return a - b })
          },
          title: {
            text: this.stateType
          }
        }
      }
    },
    methods: {
      consCheckAll (val) {
        if (val) {
          this.consolidatedYears = []
          this.consAvailableYears.forEach(i => {
            this.consolidatedYears.push(i)
          })
        } else {
          this.consolidatedYears = [2016]
        }
      },
      repubCheckAll (val) {
        if (val) {
          this.republicanYears = []
          this.repubAvailableYears.forEach(i => {
            this.republicanYears.push(i)
          })
        } else {
          this.republicanYears = [2016]
        }
      },
      stateCheckAll (val) {
        if (val) {
          this.stateYears = []
          this.stateAvailableYears.forEach(i => {
            this.stateYears.push(i)
          })
        } else {
          this.stateYears = [2016]
        }
      }
    }
  }
</script>
