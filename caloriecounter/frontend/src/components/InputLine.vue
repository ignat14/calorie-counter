<template>
<div>
	<div class="textbox">
		<input type="text"
						v-model="email"
						:class="{'focus': email || input_focused}"
						@focus="input_focused = true"
						@blur="input_focused = false">
		<span :data-placeholder="placeholder"></span>
	</div>
</div>
</template>

<script>
export default {
	name: "InputLine",
	props: {
		placeholder: String
	},
	data() {
		return {
			email: "",
			password: "",
			input_focused: false,
			error_message: ""
		};
	},
}
</script>

<style scoped>
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
</style>
