<template>
	<div>
		<h1>
			Change Password
		</h1>
		<form @submit="ChangePassword">
			<div>
				<label for="old_password">Old Password</label>
				<input type="password" v-model="data.old_password" :class="{'invalid-input': error_old_password}">
				<p v-if="error_old_password">{{error_old_password}}</p>
			</div>

			<div>
				<label for="new_password1">New Password</label>
				<input type="password" v-model="data.new_password1" :class="{'invalid-input': error_new_password1}">
				<p v-if="error_new_password1">{{error_new_password1}}</p>
			</div>

			<div>
				<label for="new_password2">Repeat Password</label>
				<input type="password" v-model="data.new_password2" :class="{'invalid-input': error_new_password2}">
				<p v-if="error_new_password2">{{error_new_password2}}</p>
			</div>

			<div>
				<input type="submit" class="submit-btn" value="Change Password">
			</div>

			<div class="error-message">
				{{ error_message }}
			</div>
			<div class="success-message">
				{{ success_message }}
			</div>

		</form>
		
	</div>
</template>

<script>
import UsersAPI from '@/services/api/users.js';

export default {
	name: "ChangePassword",
	data() {
		return {
			data: {
				old_password: "",
				new_password1: "",
				new_password2: "",
			},
			success_message: "",
			error_message: "",
			error_old_password: "",
			error_new_password1: "",
			error_new_password2: ""
		}
	},
	methods: {
		ChangePassword: async function(e) {
			e.preventDefault();

			if (this.data.new_password1 != this.data.new_password2) {
				this.error_new_password2 = "The passwords did not match.";
				this.success_message = "";
				return
			}
			try {
				await UsersAPI.changePassword(this.data);
				this.success_message = "Password changed successfully."
				this.error_message = "";
				this.error_old_password = "";
				this.error_new_password1 = "";
				this.error_new_password2 = "";
				this.data = {
					old_password: "",
					new_password1: "",
					new_password2: "",
				}
				this.clearSuccessNotification();
			}
			catch(err) {
				if (err.response.data.old_password) { this.error_old_password = err.response.data.old_password[0]; }
				else { this.error_old_password = "" }
				if (err.response.data.new_password1) { this.error_new_password1 = err.response.data.new_password1[0] }
				else { this.error_new_password1 = ""}
				if (err.response.data.new_password2) { this.error_new_password2 = err.response.data.new_password2[0] }
				else { this.error_new_password2 = ""}
				if (err.response.data.non_field_errors) { this.error_message = err.response.data.non_field_errors[0] }
				else { this.error_message = "" }

				this.success_message = "";
			}

		},
		clearSuccessNotification: function() {
			setTimeout(() => {
					this.success_message = "";
				}, 2000);
		},
	}
}
</script>

<style scoped>
form {
    width: 80%;
    margin: 0 auto;
}

label, input {
    display: inline-block;
}

label {
    width: 32%;
    text-align: right;
}

label + input {
    width: 30%;
    margin: 5px 30% 5px 4%;
		padding: 10px;
}

@media (max-width: 685px) {
	label {
			text-align: center;
	}
	label + input {
		width: 50%;
    margin: 5px 0 5px 4%;
	}
}


.submit-btn {
	padding: 10px;
	background: var(--main-blue);
	color: #fff;
	font-size: 1rem;
	cursor: pointer;
	margin: 20px;
}

p {
	margin-top: 4px;
	color: red;
}

.invalid-input {
	border: 1px solid red;
}

.error-message {
	margin: 10px;
	color: red;
}

.success-message {
	margin: 10px;
	color: green;
}

</style>
