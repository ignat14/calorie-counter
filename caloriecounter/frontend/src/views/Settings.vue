<template>
	<div class="settings-main">
		<div class="main-settings-menu">
			<h1>Settings</h1>
		</div>
		<form class="settings-list" @submit="patchProfile">
			<div class="settings-item">
				<label for="expected_calories">Expected Calories Per Day</label>
				<input type="number" name="expected_calories"
								v-model.number="expected_calories">
			</div>

			<button type="submit">
				Save
			</button>


			<div class="success-message">
				{{ success_message }}
			</div>
			<div class="error-message">
				{{ error_message }}
			</div>

		</form>
	</div>
</template>

<script>
import UsersAPI from '@/services/api/users.js';
import { mapGetters } from "vuex";

export default {
	name: "Settings",
	data() {
		return {
			expected_calories: null,
			error_message: "",
			success_message: ""
		};
	},
	computed: {
		...mapGetters(["logged_user"])
	},
	methods: {
		getProfile: async function() {
			let response = await UsersAPI.getProfile(this.logged_user.id);
			this.expected_calories = response.data.expected_calories_per_day;
		},
		patchProfile: async function(e) {
			e.preventDefault();
			try {
				await UsersAPI.patchProfile(this.logged_user.id, this.expected_calories);
				this.success_message = "Updated";
				this.error_message = "";
				this.clearMessages();
			}
			catch (err) {
				this.error_message = "Plese enter valid data.";
				this.success_message = "";
				this.clearMessages()
			}
		},
		clearMessages: function() {
			setTimeout(() => {
					this.error_message = "";
					this.success_message = "";
				}, 2000);
		},
	},
	watch: {
		'expected_calories': function() {
			if (this.expected_calories == "" || this.expected_calories < 0) {
				this.expected_calories = 0;
			}
		}
	},
	created() {
		this.getProfile();
	}
}
</script>

<style scoped>

.settings-list {
	display: flex;
	flex-direction: column;
}

.settings-item {
	margin: 10px;
}

.settings-item label {
	padding: 30px;
}

.settings-item input {
	padding: 7px;
	margin: 10px;
	font-size: 17px;
	width: 160px;
}

.settings-list button {
	width: 200px;
	background: var(--main-blue);
	color: #fff;
	border: 1px solid #000;
	padding: 10px;
	cursor: pointer;
	align-self: center;
	margin-top: 100px;
}


.success-message {
	margin: 30px;
	color: green;
}

.error-message {
	margin: 30px;
	color: red;
}

</style>
