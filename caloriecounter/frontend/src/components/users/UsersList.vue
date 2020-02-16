<template>
	<div>
		<div v-for="user in all_users" :key="user.id">
			<User :user="user" @deleteUser="deleteUser"/>
		</div>
	</div>
</template>

<script>
import User from '@/components/users/User.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
	name: "UsersList",
	components: {
		User
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
	created: function() {
		this.fetchAllUsers();
	}
}
</script>

<style>

</style>
