<template>
	<div>
		<div class="managed-meal-main">
			<select v-model="meal.user" @change="userChange()" class="mm-input user"
							:class="{'invalid-input': error_user}">
				<option v-for="user in all_users" :key="user.id" :value="user.id">{{user.email}}</option>
			</select>
			<div class="date-time">
				<div class="mm-input date-picker-div">
					<VueCtkDateTimePicker v-model="meal.date"
																class="date-picker-input"
																:only-date="true"
																label="Select Date"
																format="YYYY-MM-DD"
																formatted="ll"
																:class="{'invalid-input': error_date}"
					></VueCtkDateTimePicker>
				</div>
				<div class="mm-input date-picker-div time">
					<VueCtkDateTimePicker v-model="meal.time"
																class="time-picker-input"
																:only-time="true"
																label="Select Time"
																format="HH:mm:ss"
																formatted="hh:mm a"
																:minuteInterval="10"
																:class="{'invalid-input': error_time}"
					></VueCtkDateTimePicker>
				</div>
			</div>
			<input class="mm-input desc" type="text" name="description" v-model="meal.description"
							:class="{'invalid-input': error_description}">
			<input class="mm-input cals" type="number" name="calories" v-model="meal.calories"
							:class="{'invalid-input': error_calories}">
			<div class="save-delete">

				<span class="btn-wrapper">
					<button class="save" @click="show_save_dialog = !show_save_dialog">Save</button>
					<ConfirmDialog
							v-if="show_save_dialog"
							text="Are you sure you want to save this meal?"
							@yes="updateMeal()"
							@no="show_save_dialog = false" 
						/>
				</span>

				<span class="btn-wrapper">
					<button class="delete" @click="show_delete_dialog = !show_delete_dialog">Delete</button>
					<ConfirmDialog
						v-if="show_delete_dialog"
						text="Are you sure you want to delete this meal?"
						@yes="deleteMeal()"
						@no="show_delete_dialog = false" 
					/>
				</span>

			</div>
		</div>

		<div class="error-message">
			{{ error_message }}
		</div>
		<div class="success-message">
			{{ success_message }}
		</div>

	</div>
	
</template>

<script>
import AllMealsAPI from '@/services/api/all_meals.js';
import ConfirmDialog from '@/components/utils/ConfirmDialog.vue';
import { mapGetters } from 'vuex';

export default {
	name: "ManagedMeal",
	components: {
		ConfirmDialog
	},
	props: {
		meal: Object
	},
	data() {
		return {
			show_save_dialog: false,
			show_delete_dialog: false,
			success_message: "",
			error_message: "",
			error_user: "",
			error_date: "",
			error_time: "",
			error_description: "",
			error_calories: ""
		}
	},
	computed: {
		...mapGetters(['all_users'])
	},
	methods: {
		cleanErrorMessages: function() {
			this.error_message = "";
			this.error_user = "";
			this.error_date = "";
			this.error_time = "";
			this.error_description = "";
			this.error_calories = "";
		},
		updateMeal: async function() {
			try {
				await AllMealsAPI.updateMeal(this.meal.id, this.meal);
				this.show_save_dialog = false;
				this.success_message = "Saved Sucessfully";
				this.cleanErrorMessages();
				this.clearSuccessNotification();
			}
			catch(err) {
				if (err.response.data.user) { this.error_user = err.response.data.user[0]; }
				else { this.error_user = ""}
				if (err.response.data.date) { this.error_date = err.response.data.date[0]; }
				else { this.error_date = ""}
				if (err.response.data.time) { this.error_time = err.response.data.time[0]; }
				else { this.error_time = ""}
				if (err.response.data.description) { this.error_description = err.response.data.description[0]; }
				else { this.error_description = ""}
				if (err.response.data.calories) { this.error_calories = err.response.data.calories[0]; }
				else { this.error_calories = ""}

				if (err.response.data.non_field_errors) { this.error_message = err.response.data.non_field_errors[0] }
				else { this.error_message = "" }
				if (this.error_user || this.error_date || this.error_time || this.error_description || this.error_calories) {
					this.error_message = "Invalid Input"
				}

				this.show_save_dialog = false;
				this.success_message = "";
				this.clearErrorNotification();
			}
		},
		deleteMeal: async function() {
			await AllMealsAPI.deleteMeal(this.meal.id);
			this.$emit("deleteMeal", this.meal.id);
		},
		clearSuccessNotification: function() {
			setTimeout(() => {
					this.success_message = "";
				}, 2000);
		},
		clearErrorNotification: function() {
			setTimeout(() => {
					this.cleanErrorMessages();
				}, 4000);
		},
	}
}
</script>

<style scoped>

.managed-meal-main {
	display: grid;
	grid-template-columns: 2fr 2fr 1fr 1fr 2fr;
	grid-template-areas: "user date-time desc cals save-del";
	justify-content: center;
	margin: 30px 500px;
	margin-bottom: 0;
}

.mm-input {
	margin: 2px;
	/* padding: 10px 5px; */
	text-align: center;
}

.user {
	grid-area: user;
	padding: 5px 2px;
	background: #fff;
}

.date-time {
	grid-area: date-time;
	display: flex;
}

.desc {
	grid-area: desc;
	width: 250px;
}

.cals {
	grid-area: cals;
	width: 100px;
}

.save-delete {
	grid-area: save-del;
	display: flex;
	align-items: center;
}

.date-picker-div {
	width: 150px;
}

.btn-wrapper {
	position: relative;
}

.save {
	background: rgb(59, 206, 83);
	width: 70px;
	padding: 12px;
	margin: 0 2px;
	border: 1px solid #999;
	color: #fff;
	cursor: pointer;
}

.delete {
	background: rgb(245, 94, 94);
	padding: 12px;
	margin: 0 2px;
	width: 70px;
	border: 1px solid #999;
	color: #fff;
	cursor: pointer;
}

@media (max-width: 1240px) {
	.managed-meal-main {
		grid-template-columns: 1fr 1fr 3fr;
		grid-template-areas: 
					"user date-time date-time"
					"desc cals save-del";
		margin: 30px 400px;
		margin-bottom: 0;
	}
	.desc {
		padding: 10px 0;
	}
}

@media (max-width: 780px) {
	.managed-meal-main {
		grid-template-columns: 1fr 1fr;
		grid-template-areas: 
					"user user"
					"date-time date-time"
					"desc desc"
					"cals save-del";
		margin: 30px 300px;
		margin-bottom: 0;
	}
	.cals {
		padding: 10px;
	}
}

@media (max-width: 615px) {
	.managed-meal-main {
		margin: 30px 200px;
		margin-bottom: 0;
	}
}

@media (max-width: 400px) {
	.managed-meal-main {
		margin: 30px 100px;
		margin-bottom: 0;
	}
}

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
	margin: 5px;
	color: red;
}

.success-message {
	margin: 5px;
	color: green;
}

</style>
