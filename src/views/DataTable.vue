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
            <div class="field has-addons">
              <p class="control">
                <span class="select">
                  <b-select v-model="searchCategory" placeholder="Выбирите одну">
                      <option
                          v-for="(option, index) in searchFields"
                          :value="option.machine_name"
                          :key="index">
                          {{ option.name }}
                      </option>
                  </b-select>
                </span>
              </p>
              <p class="control is-expanded">
                <b-input v-model="search"></b-input>
              </p>
              <p class="control">
                <button @click="onSearch" class="button is-primary">
                  Поиск
                </button>
              </p>
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

              backend-sorting
              :default-sort-direction="defaultSortOrder"
              :default-sort="[sortField, sortOrder]"
              @sort="onSort">

              <template slot-scope="props">
                <b-table-column 
                  label="Бюджетная программа"
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

                <b-table-column field="year" label="Год" numeric sortable>
                    {{ props.row.year }}
                </b-table-column>
                <b-table-column field="budget_2016" label="2016" numeric sortable>
                    {{ props.row.budget_2016 }}
                </b-table-column>
                <b-table-column field="budget_2017" label="2017" numeric sortable>
                    {{ props.row.budget_2017 }}
                </b-table-column>
                <b-table-column field="budget_2018" label="2018" numeric sortable>
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
      sortField: 'year',
      sortOrder: 'desc',
      defaultSortOrder: 'desc',
      page: 1,
      perPage: 20,

      search: '',
      searchCategory: 'budget_programm',
      searchFields: [
        { name: 'Бюджетная программа', machine_name: 'budget_programm' },
        { name: 'Вид соц реализаций', machine_name: 'vid_soc_real' },
        { name: 'Вид гос сод', machine_name: 'vid_gos_sod' },
        { name: 'Текущие или развитие', machine_name: 'tekushee_ili_razvitie' },
        { name: 'Администратор бюджетной программы', machine_name: 'administrator_budget_program' }
        // { name: 'year', machine_name: 'year' },
        // { name: 'budget_2016', machine_name: 'budget_2016' },
        // { name: 'budget_2017', machine_name: 'budget_2017' },
        // { name: 'budget_2018', machine_name: 'budget_2018' }
      ],

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
      this.ParseQuery.skip((this.page * this.perPage) - this.perPage)
      if (this.sortOrder === 'asc') {
        this.ParseQuery.ascending(this.sortField)
      } else {
        this.ParseQuery.descending(this.sortField)
      }

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
        let data = []
        for (let i = 0; i < results.length; i++) {
          data.push({
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
        ctx.dataCollection = data
        this.loading = false
      })
    },
    /**
    * Handle page-change event
    */
    onPageChange (page) {
      this.page = page
      this.loadAsyncData()
    },
    /*
    * Handle sort event
    */
    onSort (field, order) {
      this.sortField = field
      this.sortOrder = order
      this.loadAsyncData()
    },
    /**
     * Handle search request
     */
    onSearch () {
      const ctx = this
      this.loading = true
      if (this.sortOrder === 'asc') {
        this.ParseQuery.ascending(this.sortField)
      } else {
        this.ParseQuery.descending(this.sortField)
      }

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
      this.ParseQuery.contains(this.searchCategory, this.search)
      this.ParseQuery.find().then((results) => {
        let data = []
        for (let i = 0; i < results.length; i++) {
          data.push({
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
        ctx.dataCollection = data
        this.loading = false
      })
    }
  },

  mounted () {
    this.loadAsyncData()
  }
}
</script>
