<template>
	<div>
		<mq-layout mq="laptop+">
			<div class="side-menu"
						:class="{open: is_open, closed: !is_open}">

				<div class="toggle-btn" @click="is_open = !is_open">
					<i v-if="!is_open" class="fas fa-chevron-right toggle-icon"/>
					<i v-if="is_open" class="fas fa-chevron-left toggle-icon"/>
				</div>

				<div class="icons-wrapper">
					<router-link to="/">
						<i class="far fa-clipboard menu-icon"></i>
						<span v-if="is_open">Diary</span>
					</router-link>
					
					<router-link to="/settings">
						<i class="fas fa-cog menu-icon"></i>
						<span v-if="is_open">Settings</span>
					</router-link>
					
					<router-link to="/manage_users" v-if="logged_user.permission != 'USER'">
						<i class="fas fa-users"></i>
						<span v-if="is_open">Manage Users</span>
					</router-link>

					<router-link to="/manage_meals" v-if="logged_user.permission == 'ADMIN'">
						<i class="fas fa-drumstick-bite"></i>
						<span v-if="is_open">Manage Meals</span>
					</router-link>
				</div>
				
			</div>
		</mq-layout>

	</div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
	name: "SideMenu",
	data() {
		return {
			is_open: false
		};
	},
	computed: {
		...mapGetters(['logged_user'])
	}
}
</script>

<style scoped>
.side-menu {
	position: fixed;
	left: 0;
	top: 0;
	background: var(--main-blue);
	height: 100vh;
	z-index: 4;
}

.closed {
	width: 55px;
}

.open {
	width: 200px;
}

.icons-wrapper {
	margin-top: 80px;
	display: flex;
	flex-direction: column;
	position: fixed;
}

.icons-wrapper i {
	font-size: 30px;
	padding: 0 5px;
	color: #fff;
	cursor: pointer;
}

.icons-wrapper i:hover {
	color: #000;
}

.toggle-btn {
	display: flex;
	justify-content: center;
	align-items: center;
	background: #fff;
	position: relative;
	top: 8.5%;
	left: 100%;
	width: 20px;
	height: 20px;
	transform: translateX(-12px);
	border-radius: 50%;
	border: 1px solid black;
	z-index: 5;
	cursor: pointer;
}

.toggle-btn:hover {
	background: #000;
	color: #fff;
}

.toggle-icon {
	font-size: 12px;
}

a {
	width: 180px;
	padding: 2px;
	margin-top: 20px;
	text-decoration: none;
	color: white;
	display: flex;
	justify-content: flex-start;
	align-items: center;
}

a:hover {
	color: #000;
}

a i {
	width: 40px;
}

a span {
	display: flex;
	justify-content: center;
}

</style>
