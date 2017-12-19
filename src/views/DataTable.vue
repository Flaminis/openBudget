<template>
  <section class="section section--gray-bg">
    <div id="data-table">
      <div class="container">
        <div class="columns">
          <div class="column">
            <div class="content">
              <h2 class="has-text-centered">
                Таблица
              </h2>
            </div>
            <b-table :data="dataCollection" 
              :striped="true" 
              :narrowed="true"
              :loading="loading"

              paginated
              backend-pagination
              :total="total"
              :per-page="perPage"
              @page-change="onPageChange"

              default-sort="user.first_name">

              <template slot-scope="props">
                <b-table-column label="Бюджетная программа"
                  width="220">
                    {{ props.row.budget_programm | truncate(80) }}
                </b-table-column>

                <b-table-column label="Вид соц реализаций"
                  width="80">
                    {{ props.row.vid_soc_real | truncate(80) }}
                </b-table-column>

                <b-table-column label="Вид гос сод"
                  width="320">
                    {{ props.row.vid_gos_sod }}
                </b-table-column>

                <b-table-column label="Текущие или развитие"
                  width="120">
                    {{ props.row.tekushee_ili_razvitie }}
                </b-table-column>

                <b-table-column label="Администратор бюджетной программы"
                  width="320">
                    {{ props.row.administrator_budget_program }}
                </b-table-column>

                <b-table-column label="Год" numeric>
                    {{ props.row.year }}
                </b-table-column>
                <b-table-column label="2016" numeric>
                    {{ props.row.budget_2016 }}
                </b-table-column>
                <b-table-column label="2017" numeric>
                    {{ props.row.budget_2017 }}
                </b-table-column>
                <b-table-column label="2018" numeric>
                    {{ props.row.budget_2018 }}
                </b-table-column>
              </template>
            </b-table>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Parse from 'parse'

// const uri = 'https://astanasu.herokuapp.com/parse/classes/Message'
// const headers = {
//   'X-Parse-Application-Id': 'AberdeenGirl',
//   'X-Parse-Master-Key': 'AberdeenMasterKey'
// }

Parse.initialize('AberdeenGirl', 'AberdeenGirlJS')
Parse.serverURL = 'https://astanasu.herokuapp.com/parse'

export default {
  name: 'DataTable',

  data () {
    return {
      dataCollection: [],
      total: 0,
      loading: false,
      sortField: 'vote_count',
      sortOrder: 'desc',
      defaultSortOrder: 'desc',
      page: 1,
      perPage: 20,

      ParseData: Parse.Object.extend('Programme'),
      ParseQuery: null
    }
  },

  methods: {
    /**
     * Load async data
     */
    loadAsyncData () {
      const ctx = this
      this.loading = true
      this.ParseQuery = new Parse.Query(this.ParseData)
      this.ParseQuery.select(
        'budget_programm',
        'vid_soc_real',
        'vid_gos_sod',
        'tekushee_ili_razvitie',
        'administrator_budget_program',
        'year',
        'budget_2016',
        'budget_2017',
        'budget_2018',
        )
      this.ParseQuery.limit(this.perPage)
      this.ParseQuery.skip(this.perPage * this.page)

      this.ParseQuery.count({
        success (count) {
          let currentTotal = count
          if (count / ctx.perPage > 1000) {
            currentTotal = ctx.perPage * 1000
          }
          ctx.total = currentTotal
        },
        error (error) {
          console.log(error)
        }
      })

      this.ParseQuery.find().then((results) => {
        for (let i = 0; i < results.length; i++) {
          ctx.dataCollection.push({
            budget_programm: results[i].get('budget_programm'),
            vid_soc_real: results[i].get('vid_soc_real'),
            vid_gos_sod: results[i].get('vid_gos_sod'),
            tekushee_ili_razvitie: results[i].get('tekushee_ili_razvitie'),
            administrator_budget_program: results[i].get('administrator_budget_program'),
            year: results[i].get('year'),
            budget_2016: results[i].get('budget_2016'),
            budget_2017: results[i].get('budget_2017'),
            budget_2018: results[i].get('budget_2018')
          })
        }
        this.loading = false
      })
    },
    /**
    * Handle page-change event
    */
    onPageChange (page) {
      this.page = page
      this.loadAsyncData()
    }
  },

  mounted () {
    this.loadAsyncData()
  }
}
</script>
