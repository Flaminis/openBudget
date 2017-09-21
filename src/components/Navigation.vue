<template>
  <nav class="navbar is-info">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <strong>OpenBudget</strong>&nbsp;&nbsp;
        <i class="material-icons">show_chart</i>
      </router-link>
    </div>
    <div id="navMenuTransparentExample" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item" href="/#total">
          Бюджет
        </a>
        <a class="navbar-item" href="/#treemap">
          По видам
        </a>
        <a class="navbar-item" href="/#dynamic">
          Динамика
        </a>
        <a class="navbar-item" href="/#levels">
          Уровни
        </a>
        <router-link to="/about" class="navbar-item">
          О проекте
        </router-link>
      </div>
    </div>
  </nav>
</template>
