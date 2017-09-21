<template>
  <div class="section section--gray-bg">
    <div id="levels">
      <div class="container">
        <div class="columns">
          <div class="column">
            <div class="content">
              <h2 class="has-text-centered">
                Уровни
              </h2>
            </div>
          </div>
        </div>
        <div class="columns">
          <div class="column">
            <highcharts :options="sortedConsolidated" ref="highcharts"></highcharts>
          </div>
          <div class="column">
            <highcharts :options="sortedRepublican" ref="highcharts"></highcharts>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//  import openData from '../converted-data.json'
//  import _ from 'lodash'
  import Highcharts from 'highcharts'

  export default {
    name: 'levels',
    data () {
      return {
        types: ['Доходы', 'Расходы'],

        budget: 'Республиканский',
        budgetList: ['Республиканский', 'Государственный', 'Консолидированный'],

        options: {
          chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
          },
          tooltip: {
            pointFormat: '<b>{point.y} млрд тг</b>'
          },
          plotOptions: {
            pie: {
              allowPointSelect: true,
              cursor: 'pointer',
              dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                style: {
                  color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                }
              }
            }
          }
        }
      }
    },
    computed: {
      sortedConsolidated () {
        return {
          ...this.options,
          title: {
            text: 'Доходы, 8 088 млрд тг, 2016 год'
          },
          series: [{
            colorByPoint: true,
            data: [{
              name: 'Нац фонд',
              y: 19
            },
            {
              name: 'Местные бюджеты',
              y: 23
            },
            {
              name: 'Республиканский',
              y: 58
            }]
          }]
        }
      },
      sortedRepublican () {
        return {
          ...this.options,
          title: {
            text: 'Расходы, 10 млрд тг 2016 год'
          },
          series: [{
            colorByPoint: true,
            data: [{
              name: 'Местные бюджеты',
              y: 16
            },
            {
              name: 'Республиканский бюджет',
              y: 84
            }]
          }]
        }
      }
    }
  }
</script>
