<template>
	<div class="manage-meals">
		<div class="main-settings-menu">
			<h1>Manage Meals
				<span class="main-buttons">
					<i class="fas fa-sliders-h" @click="show_filters = !show_filters"></i>
					<i class="far fa-plus-square" @click="show_add_new =true"></i>
				</span>
			</h1>

			<ManageMealsFilters v-if="show_filters"/>
		</div>

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
	data() {
		return {
			show_filters: true,
			show_add_new: false
		}
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

.manage-meals {
	position: relative;
}

.main-buttons {
	position: absolute;
	top: 0;
	right: 0;
	transform: translateX(-100%);
	padding: 0 10px;
}

h1 i {
	padding: 5px;
	cursor: pointer;
}

h1 i:hover {
	color: var(--main-blue);
}

</style>
