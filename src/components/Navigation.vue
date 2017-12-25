<template>
  <nav class="navbar is-success [is-info, is-primary]">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <strong>OpenBudget</strong>&nbsp;&nbsp;
        <i class="material-icons">show_chart</i>
      </router-link>
    </div>
    <div id="navMenuTransparentExample" class="navbar-menu">
      <div class="navbar-start">
        <a data-scroll class="navbar-item" href="/#total">
          Бюджет
        </a>
        <a data-scroll class="navbar-item" href="/#treemap">
          По видам
        </a>
        <a data-scroll class="navbar-item" href="/#dynamic">
          Динамика
        </a>
        <a data-scroll class="navbar-item" href="/#levels">
          Уровни
        </a>
        <router-link to="/about" class="navbar-item">
          О проекте
        </router-link>
      </div>
    </div>
  </nav>
</template>
<style>
.navbar-brand {
  background-color: #1A535C;
}
.navbar-menu {
  background-color: #01D1B2;
}
.navbar-item:hover
{ background-color: #1A535C!important;}
/*.navbar-info {
  background-color: #01D1B2;
  color: #01D1B2;
}*/

/*a:hover {
  font-weight:bold;
  color: black;
  background-color: #01D1B2;
}*/

</style>
