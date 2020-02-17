<template>
  <div class="login">
		<form id="login-form" @submit="login">

			<h1>Calorie Counter</h1>

			<div class="textbox" :class="{'is-invalid': error_email}">
				<input type="text"
								v-model="email"
								@focus="email_focused = true"
								@blur="email_focused = false"
								:class="{'focus': email || email_focused}">
				<span data-placeholder="Email"></span>
				<div v-if="error_email" class="error-msg">{{error_email}}</div>
			</div>

			<div class="textbox" :class="{'is-invalid': error_password1}">
				<input type="password"
								v-model="password1"
								:class="{'focus': password1 || password1_focused}"
								@focus="password1_focused = true"
								@blur="password1_focused = false">
				<span data-placeholder="Password"></span>
				<div v-if="error_password1" class="error-msg">{{error_password1}}</div>
			</div>

			<div class="textbox" :class="{'is-invalid': error_password2}">
				<input type="password"
								v-model="password2"
								:class="{'focus': password2 || password2_focused}"
								@focus="password2_focused = true"
								@blur="password2_focused = false">
				<span data-placeholder="Repeat Password"></span>
				<div v-if="error_password2" class="error-msg">{{error_password2}}</div>
			</div>

			<div class="error-message">
				{{ error_message }}
			</div>
			<div class="success-message">
				{{ success_message }}
			</div>

			<div class="login-btn-div">
				<input type="submit" value="Sign Up">
			</div>

			<div class="bottom-line">
				<span>Already have an account?</span> <router-link to="/login">Log In</router-link>
			</div>

		</form>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import AuthApi from '@/services/api/auth.js';
// import router from '@/router/index.js';

export default {
	name: 'Login',
	data() {
		return {
			email: "",
			password1: "",
			password2: "",
			email_focused: false,
			password1_focused: false,
			password2_focused: false,
			error_message: "",
			success_message: "",
			error_email: "",
			error_password1: "",
			error_password2: ""
		};
	},
	methods: {
		...mapActions(['fetchUser']),
		login: async function(e) {
			e.preventDefault();
			let data = {
        "email": this.email,
				"password1": this.password1,
				"password2": this.password2
			}
			try {
				await AuthApi.signUp(data);
				this.success_message = "Activation Email sent. Please verify before log in";
				this.error_message = "";
				this.error_email = "";
				this.error_password1 = "";
				this.error_password2 = "";
			}
			catch(err) {
				if (err.response.data.email) { this.error_email = err.response.data.email[0]; }
				else { this.error_email = "" }
				if (err.response.data.password1) { this.error_password1 = err.response.data.password1[0]; }
				else { this.error_password1 = ""}
				if (err.response.data.password2) { this.error_password2 = err.response.data.password2[0]; }
				else { this.error_password2 = ""}
				if (err.response.data.non_field_errors) { this.error_message = err.response.data.non_field_errors[0] }
				else { this.error_message = "" }
				
				this.success_message = "";
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
	width: 80%;
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

.success-message {
	margin: 30px;
	color: green;
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

</style>

