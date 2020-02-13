<template>
	<div>
		<h1>Manage Meals</h1>
		<ManageMealsFilters />
		<hr />
		<AllMealsList />
	</div>
</template>

<script>
import ManageMealsFilters from '@/components/ManageMealsFilters.vue';
import AllMealsList from '@/components/AllMealsList.vue';
import { mapActions } from 'vuex';

export default {
	name: "ManageMeals",
	components: {
		ManageMealsFilters,
		AllMealsList
	},
	methods: {
		...mapActions(['fetchAllMeals'])
	},
	created: function() {
		this.fetchAllMeals();
	}
}
</script>

<style scoped>

hr {
	width: 80%;
	margin: auto;
	margin-top: 20px;
	margin-bottom: 20px;
}

</style>
