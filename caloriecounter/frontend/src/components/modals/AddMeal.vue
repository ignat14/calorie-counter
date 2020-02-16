<template>
	<div v-if="add_meal_modal" class="modal-dark-backround">

		<div class="main-modal">
			<h1>Add Meal</h1>
			<i class="fas fa-times exit-modal" @click="toggleAddMealModal(false)"></i>

			<div class="modal-form">

				<div class="modal-form-item">
					<label for="user">User</label>
					<select v-model="new_meal.user">
						<option v-for="user in all_users" :key="user.id" :value="user.id">{{user.email}}</option>
					</select>
				</div>

				<div class="modal-form-item">
					<label for="date">Date</label>
					<VueCtkDateTimePicker v-model="new_meal.date"
																class="date-picker-input"
																:only-date="true"
																label="Select Date"
																format="YYYY-MM-DD"
																formatted="ll"
					></VueCtkDateTimePicker>
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
					></VueCtkDateTimePicker>
				</div>

				<div class="modal-form-item">
					<label for="description">Description</label>
					<input type="text" v-model="new_meal.description">
				</div>

				<div class="modal-form-item">
					<label for="calories">Calories</label>
					<input type="number" v-model="new_meal.calories">
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
			}
		}
	},
	computed: {
		...mapGetters(['add_meal_modal', 'all_users'])
	},
	methods: {
		...mapActions(['toggleAddMealModal', 'createMeal']),
		createMealClick: async function() {
			this.createMeal(this.new_meal);
			this.toggleAddMealModal(false);
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

</style>
