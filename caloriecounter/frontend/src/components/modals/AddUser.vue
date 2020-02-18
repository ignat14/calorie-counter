<template>
	<div v-if="add_user_modal" class="modal-dark-backround">

		<form class="main-modal" @submit="createUserClicked">
			<h1>Add User</h1>
			<i class="fas fa-times exit-modal" @click="exitModal()"></i>

			<div class="modal-form">

				<div class="modal-form-item">
					<label for="email">Email</label>
					<input type="email" v-model="email"
									:class="{'invalid-input': error_email}">
					<div v-if="error_email" class="blank"></div>
					<p v-if="error_email" class="err-msg">{{error_email}}</p>
				</div>

				<div class="modal-form-item">
					<label for="password">Password</label>
					<input type="password" v-model="password1"
									:class="{'invalid-input': error_password1}">
					<div v-if="error_password1" class="blank"></div>
					<p v-if="error_password1" class="err-msg">{{error_password1}}</p>
				</div>

				<div class="modal-form-item">
					<label for="password">Repeat Password</label>
					<input type="password" v-model="password2"
									:class="{'invalid-input': error_password2}">
					<div v-if="error_password2" class="blank"></div>
					<p v-if="error_password2" class="err-msg">{{error_password2}}</p>
				</div>

				<div class="modal-form-item">
					<label for="email">Permission</label>
					<select v-model="permission"
									:class="{'invalid-input': error_permission}">
						<option>USER</option>
						<option>MANAGER</option>
						<option>ADMIN</option>
					</select>
					<div v-if="error_permission" class="blank"></div>
					<p v-if="error_permission" class="err-msg">{{error_permission}}</p>
				</div>

				<div class="error-message">
					{{ error_message }}
				</div>
				<div class="success-message">
					{{ success_message }}
				</div>

				<button type="submit" :disabled="$wait.any">
					<v-wait for="createUser">
						<template slot="waiting">
							<div class="loading">
								<Loader />
							</div>
						</template>

						<span >Add User</span>

					</v-wait>

				</button>
			</div>

		</form>

	</div>
</template>

<script>
import Loader from '@/components/utils/Loader.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
	name: "AddUserModal",
	components: {
		Loader
	},
	data() {
		return {
			email: "",
			password1: "",
			password2: "",
			permission: "USER",
			success_message: "",
			error_message: "",
			error_email: "",
			error_password1: "",
			error_password2: "",
			error_permission: ""
		}
	},
	computed: {
		...mapGetters(['add_user_modal', 'all_users'])
	},
	methods: {
		...mapActions(['toggleAddUserModal', 'createUser']),
		clearForm: function() {
			this.email = "";
			this.password1 = "";
			this.password2 = "";
			this.permission = "USER";
			this.success_message = "";
			this.error_message = "";
			this.error_email = "";
			this.error_password1 = "";
			this.error_password2 = "";
			this.error_permission = "";
		},
		exitModal: function() {
			this.toggleAddUserModal(false);
			this.clearForm();
		},
		createUserClicked: async function(e) {
			e.preventDefault();
			let data = {
				"email": this.email,
				"password1": this.password1,
				"password2": this.password2,
			}
			if (this.permission) {
				data.permission = this.permission;
			}

			try {
				this.$wait.start('createUser');
				await this.createUser(data);
				this.$wait.end('createUser');
				let success_message = "User created successfuly. Verification email sent to " + this.email;
				this.clearForm();
				this.success_message = success_message;
			}
			catch(err) {				
				if (err.response.data.email) { this.error_email = err.response.data.email[0]; }
				else { this.error_email = "" }
				if (err.response.data.password1) { this.error_password1 = err.response.data.password1[0]; }
				else { this.error_password1 = ""}
				if (err.response.data.password2) { this.error_password2 = err.response.data.password2[0]; }
				else { this.error_password2 = ""}
				if (err.response.data.permission) { this.error_permission = err.response.data.permission[0]; }
				else { this.error_permission = ""}
				if (err.response.data.non_field_errors) { this.error_message = err.response.data.non_field_errors[0] }
				else { this.error_message = "" }
				
				this.success_message = "";
				
			}
			finally {
				this.$wait.end('createUser');
			}
			
		}
	}
}
</script>

<style scoped>

.invalid-input {
	border: 1px solid red;
}

.err-msg {
	color: red;
	margin: 0;
	padding: 0;
	font-size: 0.8rem;
}

.error-message {
	margin: 10px;
	color: red;
}

.success-message {
	margin: 10px;
	color: green;
}

.loading .loader {
  border: 5px solid #f3f3f3;
  border-radius: 50%;
  border-top: 5px solid #3498db;
  width: 20px;
  height: 20px;
}

button[type=submit] {
	position: relative;
	height: 40px;
}

</style>
