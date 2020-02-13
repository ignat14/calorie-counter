<template>
	<div class="settings-main">
		<h1>Settings</h1>
		<div class="settings-list">
			<div class="settings-item">
				<label for="expected_calories">Expected Calories Per Day</label>
				<input type="number" name="expected_calories"
								v-model="expected_calories">
			</div>
			<button @click="patchProfile()">
				Save
			</button>
		</div>
	</div>
</template>

<script>
import UsersAPI from '@/services/api/users.js';
import { mapGetters } from "vuex";

export default {
	name: "Settings",
	data() {
		return {
			expected_calories: null
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
		patchProfile: async function() {
			await UsersAPI.patchProfile(this.logged_user.id, this.expected_calories);
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
	margin-right: 60px;
}

.settings-item input {
	padding: 7px;
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
	margin-left: 500px;
}

</style>
