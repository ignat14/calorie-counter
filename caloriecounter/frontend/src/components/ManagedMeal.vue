<template>
	<div class="managed-meal-main">
		<input class="mm-input user" type="text" name="user" v-model="meal.user">
		<div class="mm-input date-picker-div">
			<VueCtkDateTimePicker v-model="meal.date"
														class="date-picker-input"
														:only-date="true"
														format="YYYY-MM-DD"
														formatted="ll"
			></VueCtkDateTimePicker>
		</div>
		<div class="mm-input date-picker-div">
			<VueCtkDateTimePicker v-model="meal.time"
														class="time-picker-input"
														:only-time="true"
														format="HH:mm:ss"
														formatted="hh:mm a"
														:minuteInterval="10"
			></VueCtkDateTimePicker>
		</div>
		<input class="mm-input desc" type="text" name="description" v-model="meal.description">
		<input class="mm-input cals" type="number" name="calories" v-model="meal.calories">
		<button class="mm-input save" @click="updateMeal()">Save</button>
		<button class="mm-input delete" @click="deleteMeal()">Delete</button>
	</div>
</template>

<script>
import AllMealsAPI from '@/services/api/all_meals.js';

export default {
	name: "ManagedMeal",
	props: {
		meal: Object
	},
	methods: {
		updateMeal: function() {
			AllMealsAPI.updateMeal(this.meal.id, this.meal);
		},
		deleteMeal: async function() {
			await AllMealsAPI.deleteMeal(this.meal.id);
			this.$emit("deleteMeal", this.meal.id);
		}
	}
}
</script>

<style scoped>

.managed-meal-main {
	display: flex;
	justify-content: center;
	margin: 0 100px;
}

.mm-input {
	margin: 2px;
	margin-bottom: 15px;
	padding: 0 5px;
	text-align: center;
}

.desc {
	width: 250px;
}

.cals {
	width: 100px;
}

.date-picker-div {
	width: 150px;
}

.managed-meal-main button {
	width: 60px;
	border: 1px solid #999;
	color: #fff;
	cursor: pointer;
}

.save {
	background: rgb(59, 206, 83);
}

.delete {
	background: rgb(245, 94, 94);
}

</style>
