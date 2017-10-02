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
            <div class="content">
              <h2 class="has-text-centered">
                Доходы за 2016 год
              </h2>
            </div>
            <highcharts :options="sortedConsolidated" ref="highcharts"></highcharts>
          </div>
          <div class="column">
            <div class="content">
              <h2 class="has-text-centered">
                Расходы за 2016 год
              </h2>
            </div>
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
            type: 'pie',
            options3d: {
              enabled: true,
              alpha: 30
            }
          },
          tooltip: {
            pointFormat: '<b>{point.y} млрд. тг</b> <br><b>{point.percentage:.1f}%</b>'
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
            text: '<b>8 088 млрд. тг',
            verticalAlign: 'middle',
            floating: true,
            style: {
              'color': '#1A535C',
              'position': 'relative',
              'font-size': '2em'
            }
          },
          plotOptions: {
            pie: {
              innerSize: 200,
              depth: 0
            }
          },
          series: [{
            colorByPoint: true,
            data: [{
              name: 'Нац фонд',
              y: 1536.7
            },
            {
              name: 'Местные бюджеты',
              y: 2183.7
            },
            {
              name: 'Республиканский',
              y: 4691
            }]
          }]
        }
      },
      sortedRepublican () {
        return {
          ...this.options,
          title: {
            text: '<b>10 444 млрд. тг',
            verticalAlign: 'middle',
            floating: true,
            style: {
              'color': '#1A535C',
              'position': 'relative',
              'font-size': '2em'
            }
          },
          plotOptions: {
            pie: {
              innerSize: 240,
              depth: 45
            }
          },
          legend: {
            labelformatter () {
              return this.name + ' (' + this.y + '%)'
            }
          },
          series: [{
            colorByPoint: true,
            data: [{
              name: 'Местные бюджеты',
              y: 1671
            },
            {
              name: 'Республиканский бюджет',
              y: 8772
            }]
          }]
        }
      }
    }
  }
</script>
