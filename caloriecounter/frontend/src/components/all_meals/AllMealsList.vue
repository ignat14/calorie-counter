<template>
	<div>
		<v-wait for="my list is to load">
			<template slot="waiting">
				<div class="loading">
						<Loader />
				</div>
			</template>
		</v-wait>
		
		<div v-for="meal in all_meals" :key="meal.id">
			<ManagedMeal :meal="meal" @deleteMeal="deleteMeal"/>
		</div>


		</div>
</template>

<script>
import ManagedMeal from '@/components/all_meals/ManagedMeal.vue';
import Loader from '@/components/utils/Loader.vue';
import { mapActions, mapGetters } from 'vuex';


export default {
	name: "AllMealsList",
	components: {
		ManagedMeal,
		Loader
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
	created: async function() {
		this.$wait.start('my list is to load');
		await this.fetchAllMeals();
		this.$wait.end('my list is to load');
	}
}
</script>

<style scoped>

.loading {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
}

</style>
