<template>
	<div class="prompt-dialog">
		<p>{{text}}</p>
		<div class="btns-flex">
			<button class="dialog-btn confirm" @click="yes()">
				<i class="fa fa-check"></i>
			</button>
			<button class="dialog-btn cancel" @click="no()" >
				<i class="fa fa-times"></i>
			</button>
		</div>
	</div>
</template>

<script>
export default {
	name: "ConfirmDialog",
	props: {
		"text": String
	},
	methods: {
		yes() {
			this.$emit('yes')
		},
		no() {
			this.$emit('no')
		}
	}
}
</script>

<style scopped>
.prompt-dialog {
	position: absolute;
	background: rgba(131, 143, 148, 0.9);
	border: 1px solid #000;
	color: #fff;
	font-weight: bold;
	text-align: center;
	top: 1rem;
	right: 0;
	border-radius: 10px;
	padding: 10px;
	margin-top: 0.5rem;
	width: 200px;
	z-index: 20;
}

.btns-flex {
	display: flex;
}

.dialog-btn {
	background-color: rgba(39, 96, 104, 0.7);
	color: #fff;
	padding: 5px 10px;
	margin: 0 10px;
	border: none;
	border-radius: 5px;
	flex: 1;
}

.confirm:hover {
	cursor: pointer;
	background-color: rgba(107, 238, 122, 0.8);
}

.cancel:hover {
	cursor: pointer;
	background-color: rgba(255, 0, 0, 0.6);
}


@media (max-width: 640px) {
	.prompt-dialog {
		position: fixed;
		top: 50%;
		left: 50%;
		width: 80%;
		height: 20%;
		font-size: 1rem;
		transform: translate(-50%, -50%);
	}

	.dialog-btn {
		padding: 10px 10px;
		font-size: 1rem;
	}

}
</style>
