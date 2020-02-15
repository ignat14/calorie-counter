<template>
	<div v-if="is_mobile && right_menu_show" class="side-menu-mobile">
		<div class="icons-wrapper">
			<div>
				Change Password
			</div>
			<div @click="logout_clicked()">
				Log Out
			</div>
		</div>
		
		<i class="fas fa-times exit" @click="toggleRightMenu(false)"></i>
	</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
	name: "AccountMenuMobile",
  computed: {
		...mapGetters(['right_menu_show']),
    is_mobile: function() {
      return this.$mq === 'mobile' || this.$mq === 'tablet'
    }
	},
	methods: {
		...mapActions(['toggleRightMenu', 'logout']),
		logout_clicked: function() {
			this.logout();
			this.toggleRightMenu(false);
		}
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
	z-index: 20;
}

.icons-wrapper {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: flex-end;
	position: absolute;
	left: 50%;
	top: 50%;
	width: 80%;
	transform: translate(-50%, -50%);
	font-size: 20px;
	border-bottom: 1px solid #fff;
}

.icons-wrapper > div {
	text-decoration: none;
	color: #fff;
	border-top: 1px solid #fff;
	width: 100%;
	text-align: right;
	padding: 30px 0;
	cursor: pointer;
}

.exit {
	position: absolute;
	top: 5%;
	left: 85%;
	color: #fff;
	font-size: 30px;
}

</style>
