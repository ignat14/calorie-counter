<template>
  <div class="login">
		<form id="login-form" @submit="login">

			<h1>Calorie Counter</h1>

			<div class="textbox" :class="{'is-invalid': error_email}">
				<input type="email"
								v-model="email"
								:class="{'focus': email || email_focused}"
								@focus="email_focused = true"
								@blur="email_focused = false">
				<span data-placeholder="Email"></span>
				<div v-if="error_email" class="error-msg">{{error_email}}</div>
			</div>
			<div class="textbox" :class="{'is-invalid': error_password}">
				<input type="password"
								v-model="password"
								:class="{'focus': password || password_focused}"
								@focus="password_focused = true"
								@blur="password_focused = false">
				<span data-placeholder="Password"></span>
				<div v-if="error_password" class="error-msg">{{error_password}}</div>
			</div>

			<div class="error-message">
				{{ error_message }}
			</div>

			<div class="login-btn-div">
				<input type="submit" value="Log In">
			</div>

			<div class="bottom-line">
				<router-link to="/reset_password">Forgot Password?</router-link> | <router-link to="/signup">Sign Up</router-link>
			</div>

		</form>
  </div>
</template>

<script>
import AuthAPI from '@/services/api/auth.js';

export default {
	name: 'Login',
	data() {
		return {
			email: "",
			password: "",
			email_focused: false,
			password_focused: false,
			error_message: "",
			error_email: "",
			error_password: "",
		};
	},
	methods: {
		login: async function(e) {
			e.preventDefault();

			let data = {
        "username": this.email,
        "password": this.password
			}
			try {
				await AuthAPI.login(data);
				this.error_message = "";
				this.$router.push('/');
			}
			catch(err) {
				if (err.response.data.username) { this.error_email = err.response.data.username[0]; }
				else { this.error_email = "" }
				if (err.response.data.password) { this.error_password = err.response.data.password[0]; }
				else { this.error_password = ""}
				if (err.response.data.non_field_errors) { this.error_message = err.response.data.non_field_errors[0] }
				else { this.error_message = "" }
				if (err.response.data.detail) { this.error_message = "Unable to log in with provided credentials." }
			}
			
		}
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
	margin-top: 30px;
}

.login-btn-div input{
	padding: 10px 50px;
	background: gray;
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

/* a {
	font-weight: bold;
} */

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

</style>

