<template>
	<div class="add-meal">
		<div class="meal-box">
			<div>
				<VueCtkDateTimePicker v-model="new_meal.time"
															:only-time="true"
															format="HH:mm:ss"
															formatted="hh:mm a"
															:minuteInterval="10"
				>
					<input v-model="new_meal.time" class="meal-input time-input" type="text" placeholder="Add time" readonly>
				</VueCtkDateTimePicker>
			</div>
			<input type="text" 
							class="meal-input" 
							v-model="new_meal.description"
							placeholder="Add description">
			<input type="number" 
							class="meal-input" 
							v-model.number="new_meal.calories" 
							placeholder="Add Calories">

			<i class="fas fa-check add-icon" @click="addMeal"></i>
		</div>
	</div>
</template>

<script>
import MyMealsAPI from '@/services/api/my_meals.js';

export default {
	name: 'AddMeal',
	props: {
		current_date: String
	},
	data() {
		return {
			new_meal: {
				time: "",
				description: "",
				calories: null,
				date: this.current_date
			}
		};
	},
	methods: {
		addMeal: async function() {
			let response = await MyMealsAPI.createMyMeal(this.new_meal);
			this.$emit('addNewMeal', response.data);
			this.clearNewMeal();
		},
		clearNewMeal: function() {
			this.new_meal = {
				time: "",
				description: "",
				calories: null,
				date: this.current_date
			};
		}
	},
	watch: {
		calories: function() {
			if (this.calories == "" || this.calories < 0) {
				this.calories = 0;
			}
		}
	}
}
</script>

<style scoped>

.add-meal {
	margin-top: 50px;
	margin-bottom: 150px;
}

.add-icon {
	cursor: pointer;
}

.add-icon:hover {
	transform: scale(1.5)
}

</style>
