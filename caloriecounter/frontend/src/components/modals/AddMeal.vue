<template>
	<div v-if="add_meal_modal" class="modal-dark-backround">

		<div class="main-modal">
			<h1>Add Meal</h1>
			<i class="fas fa-times exit-modal" @click="exitModal()"></i>

			<div class="modal-form">

				<div class="modal-form-item">
					<label for="user">User</label>
					<select v-model="new_meal.user"
									:class="{'invalid-input': error_user}">
						<option v-for="user in all_users" :key="user.id" :value="user.id">{{user.email}}</option>
					</select>
					<div v-if="error_user" class="blank"></div>
					<p v-if="error_user" class="err-msg">{{error_user}}</p>
				</div>

				<div class="modal-form-item">
					<label for="date">Date</label>
					<VueCtkDateTimePicker v-model="new_meal.date"
																class="date-picker-input"
																:only-date="true"
																label=""
																format="YYYY-MM-DD"
																formatted="ll"
																:class="{'invalid-input': error_date}"
					></VueCtkDateTimePicker>
					<div v-if="error_date" class="blank"></div>
					<p v-if="error_date" class="err-msg">{{error_date}}</p>
				</div>

				<div class="modal-form-item">
					<label for="time">Time</label>
					<VueCtkDateTimePicker v-model="new_meal.time"
																class="time-picker-input"
																:only-time="true"
																label="Select Time"
																format="HH:mm:ss"
																formatted="hh:mm a"
																:minuteInterval="10"
																:class="{'invalid-input': error_time}"
					></VueCtkDateTimePicker>
					<div v-if="error_time" class="blank"></div>
					<p v-if="error_time" class="err-msg">{{error_time}}</p>
				</div>

				<div class="modal-form-item">
					<label for="description">Description</label>
					<input type="text" v-model="new_meal.description"
									:class="{'invalid-input': error_description}">
					<div v-if="error_description" class="blank"></div>
					<p v-if="error_description" class="err-msg">{{error_description}}</p>
				</div>

				<div class="modal-form-item">
					<label for="calories">Calories</label>
					<input type="number" v-model.number="new_meal.calories"
									:class="{'invalid-input': error_calories}">
					<div v-if="error_calories" class="blank"></div>
					<p v-if="error_calories" class="err-msg">{{error_calories}}</p>
				</div>

				<div class="error-message">
					{{ error_message }}
				</div>
				<div class="success-message">
					{{ success_message }}
				</div>

				<button @click="createMealClick()">Add Meal</button>
			</div>

		</div>

	</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
	name: "AddUserModal",
	data() {
		return {
			new_meal: {
				user: null,
				date: "",
				time: "",
				description: "",
				calories: null
			},
			success_message: "",
			error_message: "",
			error_user: "",
			error_date: "",
			error_time: "",
			error_description: "",
			error_calories: "",
		}
	},
	computed: {
		...mapGetters(['add_meal_modal', 'all_users'])
	},
	methods: {
		...mapActions(['toggleAddMealModal', 'createMeal']),
		cleanNewMeal: function() {
			this.new_meal = {
				user: null,
				date: "",
				time: "",
				description: "",
				calories: null
			}
		},
		cleanErrorMessages: function() {
			this.error_message = "";
			this.error_user = "";
			this.error_date = "";
			this.error_time = "";
			this.error_description = "";
			this.error_calories = "";
		},
		exitModal: function() {
			this.success_message = "";
			this.cleanErrorMessages();
			this.cleanNewMeal();
			this.toggleAddMealModal(false);
		},
		createMealClick: async function() {
			try {
				await this.createMeal(this.new_meal);
				this.success_message = "Meal added successfully";
				this.cleanErrorMessages();
			}
			catch (err) {
				if (err.response.data.user) { this.error_user = err.response.data.user[0]; }
				else { this.error_user = "" }
				if (err.response.data.date) { this.error_date = "invalid input." }
				else { this.error_date = ""}
				if (err.response.data.time) { this.error_time = "invalid input." }
				else { this.error_time = ""}
				if (err.response.data.description) { this.error_description = err.response.data.description[0]; }
				else { this.error_description = ""}
				if (err.response.data.calories) { this.error_calories = err.response.data.calories[0]; }
				else { this.error_calories = ""}
				if (err.response.data.non_field_errors) { this.error_message = err.response.data.non_field_errors[0] }
				else { this.error_message = "" }
				
				this.success_message = "";
			}
		},
	},
	watch: {
		'new_meal.calories': function() {
			if (this.new_meal.calories == "" || this.new_meal.calories < 0) {
				this.new_meal.calories = 0;
			}
		}
	}
}
</script>

<style scoped>

button {
	width: 100px;
	background: var(--main-blue);
	color: #fff;
	border: 1px solid #000;
	padding: 10px;
	margin-top: 20px;
	cursor: pointer;
	align-self: center;
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
	margin: 10px;
	color: red;
}

.success-message {
	margin: 10px;
	color: green;
}

</style>
