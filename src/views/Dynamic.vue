<template>
  <div class="section">
    <div id="dynamic">
      <div class="container">
        <div class="columns">
          <div class="column">
            <div class="content">
              <h2 class="has-text-centered">
                Динамика
              </h2>
            </div>
          </div>
        </div>
        <div class="columns">
          <div class="column is-12">
            <b-tabs type="is-boxed is-centered" size="is-medium">
              <b-tab-item label="Республиканский">
                <br>
                <div class="content">
                  <div class="columns">
                    <div class="column is-8 is-offset-2">
                      <div class="is-flex align-center">
                        <div class="field is-horizontal">
                          <div class="field-label is-normal">
                            <label class="label">Сравнить</label>
                          </div>
                          <div class="field-body">
                            <div class="field is-narrow">
                              <div class="control">
                                <div class="select">
                                  <select v-model="repubCompare.type">
                                    <option value="Доходы" selected>Доходы</option>
                                    <option value="Расходы">Расходы</option>
                                  </select>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <div class="field is-horizontal">
                          <div class="field-label is-normal">
                            <label class="label">между</label>
                          </div>
                          <div class="field-body">
                            <div class="field is-narrow">
                              <div class="control">
                                <div class="select">
                                  <select v-model="repubCompare.from">
                                    <option v-for="(year, index) in repubAvailableYears"
                                            :value="year"
                                            :key="index">{{ year }}</option>
                                  </select>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <div class="field is-horizontal">
                          <div class="field-label is-normal">
                            <label class="label">и</label>
                          </div>
                          <div class="field-body">
                            <div class="field is-narrow">
                              <div class="control">
                                <div class="select">
                                  <select v-model="repubCompare.to">
                                    <option v-for="(year, index) in repubAvailableYears" :value="year" :key="index">{{ year }}</option>
                                  </select>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="field is-horizontal">
                          <div class="field-label">
                            <!-- Left empty for spacing -->
                          </div>
                          <div class="field-body">
                            <div class="field">
                              <div class="control">
                                <button class="button is-primary" @click="showRepubComparision">
                                  Готово
                                </button>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div v-if="repubCompare.result && repubCompare.percents">
                        <br>
                        <div class="is-flex align-center">
                          <div>
                            <h2 class="is-marginless"><span class="Highlighted">{{ repubCompare.result }}</span> млрд тенге</h2>
                          </div>
                          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                          <div>
                            <h2 class="is-marginless"><span class="Highlighted">{{ repubCompare.percents }}</span> %</h2>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <highcharts :options="sortedRepublican" ref="highcharts"></highcharts>
                </div>
              </b-tab-item>
              <b-tab-item label="Государственный">
                <br>
                <div class="content">
                  <div class="columns">
                    <div class="column is-8 is-offset-2">
                      <div class="is-flex align-center">
                        <div class="field is-horizontal">
                          <div class="field-label is-normal">
                            <label class="label">Сравнить</label>
                          </div>
                          <div class="field-body">
                            <div class="field is-narrow">
                              <div class="control">
                                <div class="select">
                                  <select v-model="stateCompare.type">
                                    <option value="Доходы" selected>Доходы</option>
                                    <option value="Расходы">Расходы</option>
                                  </select>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <div class="field is-horizontal">
                          <div class="field-label is-normal">
                            <label class="label">между</label>
                          </div>
                          <div class="field-body">
                            <div class="field is-narrow">
                              <div class="control">
                                <div class="select">
                                  <select v-model="stateCompare.from">
                                    <option v-for="(year, index) in stateAvailableYears"
                                            :value="year"
                                            :key="index">{{ year }}</option>
                                  </select>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <div class="field is-horizontal">
                          <div class="field-label is-normal">
                            <label class="label">и</label>
                          </div>
                          <div class="field-body">
                            <div class="field is-narrow">
                              <div class="control">
                                <div class="select">
                                  <select v-model="stateCompare.to">
                                    <option v-for="(year, index) in stateAvailableYears" :value="year" :key="index">{{ year }}</option>
                                  </select>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="field is-horizontal">
                          <div class="field-label">
                            <!-- Left empty for spacing -->
                          </div>
                          <div class="field-body">
                            <div class="field">
                              <div class="control">
                                <button class="button is-primary" @click="showStateComparision">
                                  Готово
                                </button>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div v-if="stateCompare.result && stateCompare.percents">
                        <br>
                        <div class="is-flex align-center">
                          <div>
                            <h2 class="is-marginless"><span class="Highlighted">{{ stateCompare.result }}</span> млрд. тг</h2>
                          </div>
                          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                          <div>
                            <h2 class="is-marginless"><span class="Highlighted">{{ stateCompare.percents }}</span> %</h2>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <highcharts :options="sortedState" ref="highcharts"></highcharts>
                </div>
              </b-tab-item>
              <b-tab-item label="Консолидированный">
                <br>
                <div class="content">
                  <div class="columns">
                    <div class="column is-8 is-offset-2">
                      <div class="is-flex align-center">
                        <div class="field is-horizontal">
                          <div class="field-label is-normal">
                            <label class="label">Сравнить</label>
                          </div>
                          <div class="field-body">
                            <div class="field is-narrow">
                              <div class="control">
                                <div class="select">
                                  <select v-model="consCompare.type">
                                    <option value="Доходы" selected>Доходы</option>
                                    <option value="Расходы">Расходы</option>
                                  </select>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <div class="field is-horizontal">
                          <div class="field-label is-normal">
                            <label class="label">между</label>
                          </div>
                          <div class="field-body">
                            <div class="field is-narrow">
                              <div class="control">
                                <div class="select">
                                  <select v-model="consCompare.from">
                                    <option v-for="(year, index) in consAvailableYears"
                                            :value="year"
                                            :key="index">{{ year }}</option>
                                  </select>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <div class="field is-horizontal">
                          <div class="field-label is-normal">
                            <label class="label">и</label>
                          </div>
                          <div class="field-body">
                            <div class="field is-narrow">
                              <div class="control">
                                <div class="select">
                                  <select v-model="consCompare.to">
                                    <option v-for="(year, index) in consAvailableYears" :value="year" :key="index">{{ year }}</option>
                                  </select>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="field is-horizontal">
                          <div class="field-label">
                            <!-- Left empty for spacing -->
                          </div>
                          <div class="field-body">
                            <div class="field">
                              <div class="control">
                                <button class="button is-primary" @click="showConsComparision">
                                  Готово
                                </button>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div v-if="consCompare.result && consCompare.percents">
                        <br>
                        <div class="is-flex align-center">
                          <div>
                            <h2 class="is-marginless"><span class="Highlighted">{{ consCompare.result }}</span> млрд. тг</h2>
                          </div>
                          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                          <div>
                            <h2 class="is-marginless"><span class="Highlighted">{{ consCompare.percents }}</span> %</h2>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <highcharts :options="sortedConsolidated" ref="highcharts"></highcharts>
                </div>
              </b-tab-item>
            </b-tabs>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import openData from '../converted-data.json'
  import _ from 'lodash'

  const filterData = (by) => {
    let incomes = null
    let expenses = null
    let yearsIncomes = null
    let yearsExpenses = null
    yearsIncomes = _(openData).filter(item => item['Уровень бюджета'] === by)
      .filter(item => item['Доходы / Расходы'] === 'Расходы')
      .map('Год').uniq().value().sort((a, b) => { return a - b })
    yearsExpenses = _(openData).filter(item => item['Уровень бюджета'] === by)
      .filter(item => item['Доходы / Расходы'] === 'Доходы')
      .map('Год').uniq().value().sort((a, b) => { return a - b })

    incomes = _.filter(openData, item => item['Уровень бюджета'] === by)
    incomes = _.filter(incomes, item => item['Доходы / Расходы'] === 'Доходы')
    incomes = _.groupBy(incomes, item => item['Доходы / Расходы'])
    incomes = _.map(incomes, (item, key) => {
      let tmp = []
      item.forEach((e, i) => {
        yearsIncomes.forEach((y, i) => {
          if (y === e['Год']) {
            if (!tmp[i]) {
              tmp[i] = e['Сумма']
            } else {
              tmp[i] += e['Сумма']
            }
          }
        })
      })
      return {
        name: key,
        data: tmp
      }
    })

    expenses = _.filter(openData, item => item['Уровень бюджета'] === by)
    expenses = _.filter(expenses, item => item['Доходы / Расходы'] === 'Расходы')
    expenses = _.groupBy(expenses, item => item['Доходы / Расходы'])
    expenses = _.map(expenses, (item, key) => {
      let tmp = []
      item.forEach((e, i) => {
        yearsExpenses.forEach((y, i) => {
          if (y === e['Год']) {
            if (!tmp[i]) {
              tmp[i] = e['Сумма']
            } else {
              tmp[i] += e['Сумма']
            }
          }
        })
      })
      return {
        name: key,
        data: tmp
      }
    })
    const data = [...incomes, ...expenses]
    return data
  }

  export default {
    name: '',
    data () {
      return {
        types: ['Доходы', 'Расходы'],
        options: {
          chart: {
            type: 'line'
          },
          yAxis: {
            title: {
              text: 'млрд, тг'
            }
          },
          plotOptions: {
            line: {
              dataLabels: {
                enabled: true
              }
            }
          },
          title: {
            text: ''
          }
        },

        consCompare: {
          type: 'Доходы',
          from: 2016,
          to: 2015,
          result: null,
          percents: null
        },

        repubCompare: {
          type: 'Доходы',
          from: 2016,
          to: 2015,
          result: null,
          percents: null
        },

        stateCompare: {
          type: 'Доходы',
          from: 2016,
          to: 2015,
          result: null,
          percents: null
        }
      }
    },
    computed: {
      sortedConsolidated () {
        return {
          ...this.options,
          series: filterData('Консолидированный'),
          xAxis: {
            categories: _(openData).filter(item => item['Уровень бюджета'] === 'Консолидированный')
              .map('Год').uniq().value().sort((a, b) => { return a - b })
          }
        }
      },
      sortedRepublican () {
        return {
          ...this.options,
          series: filterData('Республиканский'),
          xAxis: {
            categories: _(openData).filter(item => item['Уровень бюджета'] === 'Республиканский')
              .map('Год').uniq().value().sort((a, b) => { return a - b })
          }
        }
      },
      sortedState () {
        return {
          ...this.options,
          series: filterData('Государственный'),
          xAxis: {
            categories: _(openData).filter(item => item['Уровень бюджета'] === 'Государственный')
              .map('Год').uniq().value().sort((a, b) => { return a - b })
          }
        }
      },

      consAvailableYears () {
        return _(openData).filter(item => item['Уровень бюджета'] === 'Консолидированный')
          .map('Год').uniq().value().sort((a, b) => { return b - a })
      },
      repubAvailableYears () {
        return _(openData).filter(item => item['Уровень бюджета'] === 'Республиканский')
          .map('Год').uniq().value().sort((a, b) => { return b - a })
      },
      stateAvailableYears () {
        return _(openData).filter(item => item['Уровень бюджета'] === 'Государственный')
          .map('Год').uniq().value().sort((a, b) => { return b - a })
      }
    },
    methods: {
      showConsComparision () {
        const dataF = _(openData).filter(item => item['Уровень бюджета'] === 'Консолидированный')
          .filter(item => item['Год'] === this.consCompare.from)
          .filter(item => item['Доходы / Расходы'] === this.consCompare.type)
          .sumBy((o) => { return o['Сумма'] })
        const dataT = _(openData).filter(item => item['Уровень бюджета'] === 'Консолидированный')
          .filter(item => item['Год'] === this.consCompare.to)
          .filter(item => item['Доходы / Расходы'] === this.consCompare.type)
          .sumBy((o) => { return o['Сумма'] })
        console.log(dataF, dataT)
        this.consCompare.result = dataF - dataT
        this.consCompare.percents = (((dataF - dataT) / (dataF)) * 100).toFixed(2)
      },
      showRepubComparision () {
        const dataF = _(openData).filter(item => item['Уровень бюджета'] === 'Республиканский')
          .filter(item => item['Год'] === this.repubCompare.from)
          .filter(item => item['Доходы / Расходы'] === this.repubCompare.type)
          .sumBy((o) => { return o['Сумма'] })
        const dataT = _(openData).filter(item => item['Уровень бюджета'] === 'Республиканский')
          .filter(item => item['Год'] === this.repubCompare.to)
          .filter(item => item['Доходы / Расходы'] === this.repubCompare.type)
          .sumBy((o) => { return o['Сумма'] })
        this.repubCompare.result = dataF - dataT
        this.repubCompare.percents = (((dataF - dataT) / (dataF)) * 100).toFixed(2)
      },
      showStateComparision () {
        const dataF = _(openData).filter(item => item['Уровень бюджета'] === 'Государственный')
          .filter(item => item['Год'] === this.stateCompare.from)
          .filter(item => item['Доходы / Расходы'] === this.stateCompare.type)
          .sumBy((o) => { return o['Сумма'] })
        const dataT = _(openData).filter(item => item['Уровень бюджета'] === 'Государственный')
          .filter(item => item['Год'] === this.stateCompare.to)
          .filter(item => item['Доходы / Расходы'] === this.stateCompare.type)
          .sumBy((o) => { return o['Сумма'] })
        this.stateCompare.result = dataF - dataT
        this.stateCompare.percents = (((dataF - dataT) / (dataF)) * 100).toFixed(2)
      }
    }
  }
</script>
<style>
.b-tabs {
  /*color: #F333FF !important;*/
column-rule-color: #ffffff;
}
.Highlighted{
  color: #1A535C;
  position: relative;
  font-size: 1.5em;
  font-weight:300;
}
</style>
