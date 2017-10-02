<template>
  <div class="section">
    <div id="maps">
      <div class="container">
        <div class="content">
          <h2 class="has-text-centered">
            Местные бюджеты за
          </h2>
          <div class="field has-addons has-addons-centered">
          <div class="select">
          <select v-model="year">
            <option v-for="(year, index) in availableYears" :value="year" :key="index">{{ year }} год</option>
          </select>
          </div></div>

        </div>
        <div class="columns">
          <div class="column">
            <div class="content">
            <highmaps :options="sortedConsolidated" ref="highmaps"></highmaps>
          </div>
          </div>

        </div>
      </div>
    </div>
  </div>

</template>

<script>
//  import openData from '../converted-data.json'
//  import _ from 'lodash'
  import Highcharts from 'highcharts/highmaps'
  import localData from '../localData.json'
  // import datamap from '../datamap.js'
  const localDataHandle = (year) => {
    for (let i = 0; i < localData.length; i++) {
      var q = localData[i]
      if (q['year'] === year) {
        let o = [['kz-qo', q['kz-qo']],  // Qyzylorda
                ['kz-ac', q['kz-ac']],  // almaty
                ['kz-as', q['kz-as']],  // astana
                ['kz-qs', q['kz-qs']],  // kustanai
                ['kz-nk', q['kz-nk']], // Severo-Kazakhstan
                ['kz-pa', q['kz-pa']], // Pavlodar
                ['kz-am', q['kz-am']], // Akmolinsk
                ['kz-zm', q['kz-zm']], // Zhambyl
                ['kz-ek', q['kz-ek']], // Vostochno-Kazakhstan
                ['kz-ar', q['kz-ar']], // Atyrau Oblasy
                ['kz-mg', q['kz-mg']], // Mangistau
                ['kz-aa', q['kz-aa']], // almaty Oblasy
                ['kz-at', q['kz-at']], // Aqtobe Oblasy
                ['kz-wk', q['kz-wk']], // zapadno kz
                ['kz-qg', q['kz-qg']], // Karaganda
                ['kz-sk', q['kz-sk']]]
        console.log(o)
        return (o)
      }
    }
    return [['kz-qo', 80.71],  // Qyzylorda
            ['kz-ac', -97.6],  // almaty
            ['kz-as', -17.25],  // astana
            ['kz-qs', 50.9],  // kustanai
            ['kz-nk', 57.47], // Severo-Kazakhstan
            ['kz-pa', 7.28], // Pavlodar
            ['kz-am', 52.7], // Akmolinsk
            ['kz-zm', 94], // Zhambyl
            ['kz-ek', 80.124], // Vostochno-Kazakhstan
            ['kz-ar', -73.207], // Atyrau Oblasy
            ['kz-mg', -25.713], // Mangistau
            ['kz-aa', 91.008], // almaty Oblasy
            ['kz-at', 8.6], // Aqtobe Oblasy
            ['kz-wk', 37], // zapadno kz
            ['kz-qg', 16.3], // Karaganda
            ['kz-sk', 255.8]] // yuzhnokz
  }
  export default {
    name: 'maps',
    data () {
      return {
        year: 2015,
        options: {
          chart: {
            map: Highcharts.maps['kz/all'],
            height: '56%'
          },
          title: {
            text: 'Трансферты общего характера'
          },
          legend: {
            title: {
              text: 'Бюджетные изъятия  /  Субвенции'
            },
            layout: 'horizontal',
            borderWidth: 2,
            borderColor: '#1A535C',
            borderRadius: 5,
            backgroundColor: 'rgba(255,255,255,0.85)',
            floating: true,
            verticalAlign: 'top',
            y: 25,
            labelFormat: '{name}'
          },
          subtitle: {
            text: 'По областям Казахстана, <a href="http://talap.org/">Источник</a>'
          },
          mapNavigation: {
            enabled: true,
            buttonOptions: {
              verticalAlign: 'bottom'
            }
          },
          colorAxis: {
            stops: [
                [0, '#E71D36'],
                [0.2, '#FF9F1C'],
                [0.3, '#01D1B2'],
                [0.75, '#1A535C'],
                [1, '#011627']
            ]
          }
        }
      }
    },
    computed: {
      availableYears () {
        var years = []
        for (let i = 0; i < localData.length; i++) {
          var q = localData[i]
          years.push(q['year'])
        }
        return years
      },
      sortedConsolidated () {
        return {
          ...this.options,
          series: [{
            animation: true,
            data: localDataHandle(this.year), // yuzhnokz
            name: 'ТРАНСФЕРТЫ ОБЩЕГО ХАРАКТЕРА',
            states: {
              hover: {
                color: '#BADA66'
              }
            },
            dataLabels: {
              enabled: true,
              format: '{point.name}'
            }
          }],
          tooltip: {
            animation: true,
            valueSuffix: ' млрд. тенге'
          }
        }
      }
    }
  }
</script>
<style>
</style>
