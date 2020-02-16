<template>
	<div>
		<div v-for="meal in all_meals" :key="meal.id">
			<ManagedMeal :meal="meal" @deleteMeal="deleteMeal"/>
		</div>
	</div>
</template>

<script>
import ManagedMeal from '@/components/all_meals/ManagedMeal.vue';
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
		...mapActions(['fetchAllMeals']),
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
