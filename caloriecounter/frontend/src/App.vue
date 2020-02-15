<template>
  <div id="app">
    <HeaderMain v-if="$route.path !== '/login' && $route.path !== '/signup'" />
    <SideMenu v-if="$route.path !== '/login' && $route.path !== '/signup'" />
    <SideMenuMobile />
    <AccountMenuMobile />
    <router-view class="main-view" />
  </div>
</template>

<script>
import HeaderMain from '@/components/HeaderMain.vue';
import SideMenu from '@/components/menus/SideMenu.vue';
import SideMenuMobile from '@/components/menus/SideMenuMobile.vue';
import AccountMenuMobile from '@/components/menus/AccountMenuMobile.vue';

export default {
	name: 'MyMealsList',
	components: {
		HeaderMain,
    SideMenu,
    SideMenuMobile,
    AccountMenuMobile
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Dancing+Script&display=swap');
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  box-sizing: border-box;
  --main-blue: rgb(35, 92, 197);
}

body {
  font-size: 16px;
  margin: 0;
  padding: 0;
}

.main-settings-menu {
	background: #eee;
	position: sticky;
	left: 0;
	top: 59px;
	width: 100vw;
  border-bottom: 1px solid #ccc;
  margin-bottom: 20px;
	z-index: 2;
}

.main-settings-menu > h1 {
  margin: 0;
  padding: 10px;
  font-size: 1.6em;
}

input {
	border: 1px solid #aaa;
}

@media (max-width: 640px) {
  body {
    font-size: 12px;
  }
  .main-settings-menu {
    top: 50px;
  }
}

</style>



<style>
/* GLOABAL MODAL STYLES */

.main-modal {
	background: #fff;
	position: fixed;
	top: 50%;
	left: 50%;
	width: 90%;
	max-width: 600px;
	height: 90%;
	transform: translate(-50%, -50%);
	border: 1px solid #000;
	border-radius: 5%;
	z-index: 20;
}

.modal-dark-backround {
	content: '';
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background: rgba(0,0,0,0.5);
	z-index: 10;
}

.exit-modal {
	position: absolute;
	top: 0;
	left: 100%;
	transform: translateX(-100%);
	padding: 20px;
	color: #000;
	font-size: 30px;
	cursor: pointer;
}

.exit-modal:hover {
	color: var(--main-blue);
}

@media (min-width: 900px) {
	.main-modal {
		width: 50%;
		height: 50%;
	}
}


.open-modal-icon {
	position: absolute;
	left: 100%;
	top: 10px;
	width: 1rem;
	height: 1rem;
	display: flex;
	justify-content: center;
	align-items: center;
	transform: translateX(-200%);
	background: rgb(156, 156, 156);
  color: #fff;
	border-radius: 50%;
	padding: 7px 7px;
	cursor: pointer;
}

.open-modal-icon:hover {
	background: var(--main-blue);
}

.open-modal-icon i {
	font-size: 1rem;
	color: rgb(255, 255, 255);
}

@media (max-width: 640px) {
	.open-modal-icon {
		top: 6px;
		transform: translateX(-150%);
	}
}


.modal-form {
	display: flex;
	flex-direction: column;
	justify-content: center;
	margin-top: 50px;
}

.modal-form-item {
	display: grid;
	grid-template-columns: 1fr 1fr;
	/* justify-content: center;
	align-items: center; */
	margin: 0 20%;
	padding: 5px;
}

.modal-form-item > label {
	margin: 0 5px;
	justify-self: end;
	align-self: center;
	padding: 0 10px;
}

.modal-form-item > input {
	padding: 7px 0;
}

.modal-form-item > select {
	text-align: center;
	padding: 7px;
	background: #fff;
	border: 1px solid #999;
}

.modal-form > button {
	width: 100px;
	background: var(--main-blue);
	color: #fff;
	border: 1px solid #000;
	padding: 10px;
	margin-top: 20px;
	cursor: pointer;
	align-self: center;
}

@media (max-width: 640px) {
	.modal-form-item {
		display: flex;
		flex-direction: column;
	}
}

</style>
