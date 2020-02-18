<template>
	<div>
		<v-wait for="my list is to load">
			<template slot="waiting">
				<div class="loading">
					<Loader />
				</div>
			</template>
		</v-wait>
		
		<div v-for="user in all_users" :key="user.id">
			<User :user="user" @deleteUser="deleteUser"/>
		</div>



	</div>
</template>

<script>
import User from '@/components/users/User.vue';
import Loader from '@/components/utils/Loader.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
	name: "UsersList",
	components: {
		User,
		Loader
	},
	computed: {
		...mapGetters(['all_users'])
	},
	methods: {
		...mapActions(['fetchAllUsers']),
		deleteUser: function(id) {
			for (let i = 0; i < this.all_users.length; i++) {
				if (this.all_users[i].id === id) {
					this.all_users.splice(i, 1);
					break
				}
			}
		}
	},
	created: async function() {
		this.$wait.start('my list is to load');
		await this.fetchAllUsers();
		this.$wait.end('my list is to load');
	}
}
</script>

<style scoped>
.loading {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
}
</style>
