<template>
	<div>
		<div v-for="meal in all_meals" :key="meal.id">
			<ManagedMeal :meal="meal" @deleteMeal="deleteMeal"/>
		</div>
	</div>
</template>

<script>
import AllMealsAPI from '@/services/api/all_meals.js';
import ManagedMeal from '@/components/ManagedMeal.vue';
import { mapActions, mapGetters } from 'vuex';


export default {
	name: "AllMealsList",
	components: {
		ManagedMeal
	},
	computed: {
		...mapGetters(['all_meals']),
	},
	methods: {
		...mapActions([]),
		fetchAllMeals: async function() {
			let response = await AllMealsAPI.getAllMeals();
			this.all_meals = response.data;
		},
		deleteMeal(meal_id) {
			for (let i = 0; i < this.all_meals.length; i++) {
				if (this.all_meals[i].id === meal_id) {
					this.all_meals.splice(i, 1);
					break
				}
			}
		}
	},
	created: function() {
		this.fetchAllMeals();
	}
}
</script>

<style>

</style>
