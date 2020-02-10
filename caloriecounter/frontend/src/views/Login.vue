<template>
  <div class="login">
		<form id="login-form" @submit="login">

			<h1>Calorie Counter</h1>

			<div class="textbox">
				<input type="text"
								v-model="email"
								:class="{'focus': email || email_focused}"
								@focus="email_focused = true"
								@blur="email_focused = false">
				<span data-placeholder="Email"></span>
			</div>
			<div class="textbox">
				<input type="password"
								v-model="password"
								:class="{'focus': password || password_focused}"
								@focus="password_focused = true"
								@blur="password_focused = false">
				<span data-placeholder="Password"></span>
			</div>

			<div class="error-message">
				{{ error_message }}
			</div>

			<div class="login-btn-div">
				<input type="submit" value="Log In">
			</div>

			<div class="bottom-line">
				<a href="#">Forgot Password</a> | <a href="#">Sign Up</a>
			</div>

		</form>
  </div>
</template>

<script>
import axios from 'axios';
import { mapActions } from "vuex";
// import router from '@/router/index.js';

export default {
	name: 'Login',
	data() {
		return {
			email: "",
			password: "",
			email_focused: false,
			password_focused: false,
			error_message: ""
		};
	},
	methods: {
		...mapActions(['fetchUser']),
		login: async function(e) {
			e.preventDefault();
			console.log("HERE");
			
			let data = {
        "username": this.email,
        "password": this.password
			}
			try {
				let response = await axios.post('http://localhost:8000/api-token-auth/', data);
				localStorage.drf_token = response.data.token;
				this.error_message = "";
				await this.fetchUser();
				this.$router.push('/');
				console.log(localStorage.getItem("drf_token"));
			}
			catch(err) {
				this.error_message = "Please make sure that the email and password are correct";
			}
			
		}
	}
}
</script>

<style>
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
	color: red;
}

</style>

