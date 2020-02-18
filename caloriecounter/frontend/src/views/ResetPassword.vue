<template>
  <div class="login">
		<form id="login-form" @submit="resetPassword">

			<h1>Calorie Counter</h1>

			<div class="textbox" :class="{'is-invalid': error_email}">
				<input type="text"
								v-model="email"
								:class="{'focus': email || email_focused}"
								@focus="email_focused = true"
								@blur="email_focused = false">
				<span data-placeholder="Email"></span>
				<div v-if="error_email" class="error-msg">{{error_email}}</div>
			</div>

			<div class="success-message">
				{{ success_message }}
			</div>
			<div class="error-message">
				{{ error_message }}
			</div>

			<div class="login-btn-div">
				<button type="submit" :disabled="$wait.any">
					<v-wait for="emailSent">
						<template slot="waiting">
							<div class="loading">
								<Loader />
							</div>
						</template>

						<span >Reset Password</span>

					</v-wait>
				</button>
			</div>

			<div class="bottom-line">
				<span>Don't have an account?</span> <router-link to="/signup">Sign Up</router-link>
			</div>

		</form>
  </div>
</template>

<script>
import AuthAPI from '@/services/api/auth.js';
import Loader from '@/components/utils/Loader.vue';
import { mapActions } from "vuex";

export default {
	name: 'ResetPassword',
	components: {
		Loader
	},
	data() {
		return {
			email: "",
			email_focused: false,
			success_message: "",
			error_message: "",
			error_email: "",
		};
	},
	methods: {
		...mapActions(['fetchUser']),
		resetPassword: async function(e) {
			e.preventDefault();

			try {
				this.$wait.start('emailSent');
				await AuthAPI.resetPassword({"email": this.email});
				this.$wait.end('emailSent');
				this.success_message = "Instructions for changing password sent to the provided Email"
				this.error_message = "";
				this.error_email = "";
				this.clearSuccessNotificationAndRedirect();
			}
			catch(err) {
				if (err.response.data.email) { this.error_email = err.response.data.email[0]; }
				else { this.error_email = "" }
				if (err.response.data.non_field_errors) { this.error_message = err.response.data.non_field_errors[0] }
				else { this.error_message = "" }
				this.success_message = "";
			}
			finally {
				this.$wait.end('emailSent');
			}
			
		},
		clearSuccessNotificationAndRedirect: function() {
			setTimeout(() => {
					this.success_message = "";
					this.$router.push('/login');
				}, 2000);
		},
	}
}
</script>

<style scoped>
#login-form {
	position: absolute;
	left: 50%;
	top: 50%;
	transform: translate(-50%, -50%);
	padding: 80px 40px;
	width: 250px;
	height: 400px;
}

#login-form h1 {
	font-family: 'Dancing Script', cursive;
	font-size: 35px;
}

.textbox {
	border-bottom: 2px solid #adadad;
	position: relative;
	margin: 10px 0;
}

.textbox input {
	font-size: 15px;
	color: #333;
	border: none;
	outline: none;
	width: 100%;
	background: none;
	padding: 0 5px;
	height: 40px;
	text-align: center;
}

.textbox span::before {
	content: attr(data-placeholder);
	position: absolute;
	top: 50%;
	left: 50%;
	color: #adadad;
	transform: translate(-50%, -50%);
	z-index: -1;
	opacity: 1;
	transition: .5s;
}

.textbox span::after {
	content: '';
	position: absolute;
	width: 0%;
	height: 2px;
	left: 0;
	top: 100%;
	background: blue;
	transition: .5s;
}

.focus + span::before {
	opacity: 0;
}

.focus + span::after {
	width: 100%;
}

.login-btn-div {
	position: relative;
	margin-top: 30px;
}

.login-btn-div button{
	padding: 10px 50px;
	background: gray;
	height: 40px;
	border: none;
	color: white;
	font-size: 16px;
	width: 100%;
	cursor: pointer;
}

.bottom-line {
	margin-top: 10px;
	font-size: 14px;
}

.bottom-line a {
	text-decoration: none;
	color: black;
}

.error-message {
	margin: 30px;
	color: red;
}

a {
	font-weight: bold;
}

.is-invalid {
	border-bottom: 2px solid red;
}

.error-msg {
	position: absolute;
	top: 102%;
	left: 0;
	color: red;
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

</style>

