<template>
	<div>
		<div v-for="user in all_users" :key="user.id">
			<User :user="user" @deleteUser="deleteUser"/>
		</div>
	</div>
</template>

<script>
import UsersAPI from '@/services/api/users.js';
import User from '@/components/users/User.vue';

export default {
	name: "UsersList",
	components: {
		User
	},
	data() {
		return {
			all_users: []
		};
	},
	methods: {
		fetchAllUsers: async function() {
			let response = await UsersAPI.getAllUsers();
			this.all_users = response.data;
		},
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
