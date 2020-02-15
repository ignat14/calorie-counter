<template>
	<div class="manage-meals">
		<div class="main-settings-menu">
			<h1>Manage Meals
				<div class="open-modal-icon filter" @click="toggleFilters()">
						<i class="fas fa-sliders-h"></i>
				</div>
				<div class="open-modal-icon" @click="toggleAddMealModal(true)">
					<i class="fas fa-plus"></i>
				</div>
			</h1>

			<mq-layout mq="laptop+">
				<ManageMealsFilters v-if="show_filters"/>
			</mq-layout>
		</div>

		<AllMealsList />

		<AllMealsFilterModal />
		<AddMealModal />
	</div>
</template>

<script>
import ManageMealsFilters from '@/components/all_meals/ManageMealsFilters.vue';
import AllMealsList from '@/components/all_meals/AllMealsList.vue';
import AllMealsFilterModal from '@/components/modals/AllMealsFilter.vue';
import AddMealModal from '@/components/modals/AddMeal.vue';
import { mapActions } from 'vuex';

export default {
	name: "ManageMeals",
	components: {
		ManageMealsFilters,
		AllMealsList,
		AllMealsFilterModal,
		AddMealModal
	},
	data() {
		return {
			show_filters: false,
			show_add_new: false
		}
	},
	methods: {
		...mapActions(['fetchAllMeals', 'toggleAllMealsFilterModal', 'toggleAddMealModal']),
		toggleFilters: function() {
			if (this.$mq === 'laptop' || this.$mq === 'desktop') {
				this.show_filters = !this.show_filters;
			}
			else {
				this.toggleAllMealsFilterModal(true);
			}
		}
	},
	created: function() {
		this.fetchAllMeals();
	}
}
</script>

<style scoped>

.filter {
	transform: translateX(-320%);
}

@media (max-width: 640px) {
	.filter {
		transform: translateX(-270%);
	}
}

</style>
