<template>
	<div v-if="add_user_modal" class="modal-dark-backround">

		<div class="main-modal">
			<h1>Add User</h1>
			<i class="fas fa-times exit-modal" @click="toggleAddUserModal(false)"></i>

			<div class="modal-form">

				<div class="modal-form-item">
					<label for="email">Email</label>
					<input type="email" v-model="email">
				</div>

				<div class="modal-form-item">
					<label for="password">Password</label>
					<input type="password" v-model="password1">
				</div>

				<div class="modal-form-item">
					<label for="password">Repeat Password</label>
					<input type="password" v-model="password2">
				</div>

				<div class="modal-form-item">
					<label for="email">Permission</label>
					<select v-model="permission">
						<option>USER</option>
						<option>MANAGER</option>
						<option>ADMIN</option>
					</select>
				</div>

				<button @click="createUserClicked()">Add User</button>
			</div>

		</div>

	</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
	name: "AddUserModal",
	data() {
		return {
			email: "",
			password1: "",
			password2: "",
			permission: ""
		}
	},
	computed: {
		...mapGetters(['add_user_modal', 'all_users'])
	},
	methods: {
		...mapActions(['toggleAddUserModal', 'createUser']),
		createUserClicked: async function() {
			let data = {
				"email": this.email,
				"password1": this.password1,
				"password2": this.password2,
			}
			if (this.permission) {
				data.permission = this.permission;
			}
			this.createUser(data);
			this.toggleAddUserModal(false);
			
		}
	}
}
</script>

<style scoped>

</style>
