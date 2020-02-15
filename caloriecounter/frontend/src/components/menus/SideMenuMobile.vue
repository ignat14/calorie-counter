<template>
	<div v-if="is_mobile && left_menu_show" class="side-menu-mobile">
		<div class="icons-wrapper">
			<router-link to="/" @click.native="toggleLeftMenu(false)">
				<i class="far fa-clipboard menu-icon"></i>
				<span>Diary</span>
			</router-link>
			
			<router-link to="/settings" @click.native="toggleLeftMenu(false)">
				<i class="fas fa-cog menu-icon"></i>
				<span>Settings</span>
			</router-link>
			
			<router-link to="/manage_users" @click.native="toggleLeftMenu(false)" v-if="logged_user.permission != 'USER'">
				<i class="fas fa-users menu-icon"></i>
				<span>Manage Users</span>
			</router-link>

			<router-link to="/manage_meals" @click.native="toggleLeftMenu(false)" v-if="logged_user.permission == 'ADMIN'">
				<i class="fas fa-drumstick-bite menu-icon"></i>
				<span>Manage Meals</span>
			</router-link>
		</div>

		<i class="fas fa-times exit" @click="toggleLeftMenu(false)"></i>
	</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
	name: "SideMenuMobile",
  computed: {
		...mapGetters(['left_menu_show', 'logged_user']),
    is_mobile: function() {
      return this.$mq === 'mobile' || this.$mq === 'tablet'
    }
	},
	methods: {
		...mapActions(['toggleLeftMenu'])
	}
}
</script>

<style scoped>

.side-menu-mobile {
	background: rgba(0,20,80,0.92);
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 10;
}

.icons-wrapper {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: flex-start;
	position: absolute;
	left: 50%;
	top: 50%;
	width: 80%;
	transform: translate(-50%, -50%);
	font-size: 20px;
	border-bottom: 1px solid #fff;
}

.icons-wrapper i {
	font-size: 30px;
}

.menu-icon {
	color: #fff;
	padding: 30px 15px;
}

a {
	text-decoration: none;
	color: #fff;
	border-top: 1px solid #fff;
	width: 100%;
	text-align: left;
}

.exit {
	position: absolute;
	top: 5%;
	left: 85%;
	color: #fff;
	font-size: 30px;
}


</style>
