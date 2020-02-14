<template>
	<div class="meal-box">
		
		<span>
			<VueCtkDateTimePicker v-model="meal.time"
														:only-time="true"
														format="HH:mm:ss"
														formatted="hh:mm a"
														:minuteInterval="10"
														@validate="patchMeal({'time': meal.time})"
														@is-hidden="patchMeal({'time': meal.time})"
			>
				<input class="meal-input time-input" type="text" readonly>
			</VueCtkDateTimePicker>
		</span>
		<input type="text" 
						class="meal-input" 
						v-model="meal.description" 
						@change="patchMeal({'description': meal.description})"
		>
		<input type="number" 
						class="meal-input" 
						v-model.number="meal.calories" 
						@change="patchMeal({'calories': meal.calories})">
		<i class="fas fa-times delete-icon" @click="deleteMeal"></i>
	</div>
</template>

<script>
import MyMealAPI from '@/services/api/my_meals.js';

export default {
	name: 'Meal',
	props: {
		meal: Object,
	},
	data() {
		return {
			display: true
		};
	},
	methods: {
		patchMeal: async function(data) {
			let response = await MyMealAPI.patchMyMeal(data, this.meal.id);
			return response.data;
		},
		deleteMeal: async function() {
			await MyMealAPI.deleteMyMeal(this.meal.id);
			this.$emit('deleteMeal', this.meal.id);
		}
	},
	watch: {
		'meal.calories': function() {
			if (this.meal.calories == "" || this.meal.calories < 0) {
				this.meal.calories = 0;
			}
		}
	}
}
</script>

<style>

.meal-box {
	display: flex;
	justify-content: center;
	align-items: center;
}

.meal-input {
	width: 150px;
	margin: 10px;
	margin-top: 30px;
	padding: 10px;
	text-align: center;
	outline: none;
	border: none;
	border-bottom: 1px solid gray;
	font-size: 18px;
}

.time-input {
	cursor: pointer;
}

.delete-icon {
	cursor: pointer;
}

.delete-icon:hover {
	transform: scale(1.5);
}

</style>
