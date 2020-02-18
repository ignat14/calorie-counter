<template>
	<div class="add-meal">
		<form @submit="addMeal">

			<div class="meal-box">
					<span class="input-wrapper">
						<VueCtkDateTimePicker v-model="new_meal.time"
																	:only-time="true"
																	format="HH:mm"
																	formatted="HH:mm"
																	:minuteInterval="10">
							<input v-model="new_meal.time" class="meal-input time-input" type="text" 
										placeholder="Add time" readonly :class="{'is-invalid': time_errors}">
						</VueCtkDateTimePicker>
						<div v-if="time_errors" class="error-msg">This value is invalid</div>
					</span>
					<span class="input-wrapper">
						<input type="text" 
										class="meal-input"
										v-model="new_meal.description"
										placeholder="Add description"
										:class="{'is-invalid': description_errors}">
						<div v-if="description_errors" class="error-msg">This value is invalid</div>
					</span>

				<span class="input-wrapper">
					<input type="number" 
									class="meal-input" 
									v-model.number="new_meal.calories" 
									placeholder="Add Calories"
									:class="{'is-invalid': calories_errors}">
					<div v-if="calories_errors" class="error-msg">This value is invalid</div>
				</span>

				<button type="submit">
					<i class="fas fa-check add-icon"></i>
				</button>
				
			</div>

		</form>
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
				date: this.current_date,
			},
			isInvalid: true,
			time_errors: "",
			description_errors: "",
			calories_errors: ""
		};
	},
	methods: {
		addMeal: async function(e) {
			e.preventDefault();

			try {
				this.new_meal.date = this.current_date;
				let response = await MyMealsAPI.createMyMeal(this.new_meal);
				this.$emit('addNewMeal', response.data);
				this.clearNewMeal();
				this.clearErrors();
			}
			catch (err) {
				this.time_errors = err.response.data.time;
				this.description_errors = err.response.data.description;
				this.calories_errors = err.response.data.calories;
			}
		},
		clearNewMeal: function() {
			this.new_meal = {
				time: "",
				description: "",
				calories: null,
				date: this.current_date
			};
		},
		clearErrors: function() {
			this.time_errors = "";
			this.description_errors = "";
			this.calories_errors = "";
		}
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

.add-meal {
	margin-top: 50px;
	margin-bottom: 150px;
}

.add-icon {
	cursor: pointer;
	font-size: 1.4rem;
	padding: 10px;
}

.add-icon:hover {
	transform: scale(1.2)
}

.input-wrapper {
	position: relative;
}

.is-invalid {
	border-bottom: 2px solid red;
}

.error-msg {
	position: absolute;
	top: 90%;
	left: 5%;
	color: red;
	font-size: 0.8rem;
}

button[type=submit] {
	background: none;
	border: none;
	outline: none;
}

</style>
