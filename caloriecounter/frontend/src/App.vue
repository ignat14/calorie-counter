<template>
  <div id="app">
    <HeaderMain v-if="$route.path !== '/login'" />
    <SideMenu v-if="$route.path !== '/login'" />
    <router-view class="main-view" />
  </div>
</template>

<script>
import HeaderMain from '@/components/HeaderMain.vue';
import SideMenu from '@/components/SideMenu.vue';

export default {
	name: 'MyMealsList',
	components: {
		HeaderMain,
		SideMenu
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  box-sizing: border-box;
  --main-blue: rgb(35, 92, 197);
}

.main-view {
  margin-top: 120px;
  margin-left: 80px;
  margin-right: 80px;
}

</style>
