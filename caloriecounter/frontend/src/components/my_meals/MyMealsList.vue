<template>
	<div class="my-meals-wrapper">

		<div class="meals-list">
			<div class="main-settings-menu">
				<DiaryDaySelect v-model="current_date"/>
				<div class="open-modal-icon filter" @click="toggleFilters()">
						<i class="fas fa-sliders-h"></i>
				</div>

				<div class="count-calories">
					<h1 :class="{'green': calories_balance, 
											'red': !calories_balance, 
											'gray': !expected_calories}">
						{{ all_calories }}<span>Cals</span>
					</h1>
					<h4 v-if="expected_calories">
						/ {{ expected_calories }} Cals
					</h4>
				</div>
			</div>

			<div v-for="meal in my_meals" :key="meal.id">
				<DiaryMeal :meal="meal" @deleteMeal="deleteMeal"/>
			</div>
			<AddMeal :current_date="current_date" @addNewMeal="addNewMeal"/>
		</div>

	</div>
</template>

<script>
import MyMealsAPI from '@/services/api/my_meals.js';
import DiaryMeal from '@/components/my_meals/DiaryMeal.vue';
import DiaryDaySelect from '@/components/my_meals/DiaryDaySelect.vue';
import AddMeal from '@/components/my_meals/AddMeal.vue';
import { mapGetters } from "vuex";

export default {
	name: 'MyMealsList',
	components: {
		DiaryDaySelect,
		DiaryMeal,
		AddMeal
	},
	data() {
		return {
			my_meals: [],
			current_date: null,
			params: {}
		};
	},
	computed: {
		...mapGetters(["logged_user"]),
		all_calories: function() {
			let count_cals = 0;
			this.my_meals.forEach(meal => {
				count_cals += meal.calories;
			});
			return count_cals
		},
		expected_calories: function() {
			return this.logged_user.profile.expected_calories_per_day;
		},
		calories_balance: function() {
			return this.expected_calories / this.all_calories  > 1;
		}
	},
	methods: {
		fetchMyMeals: async function() {
			let response = await MyMealsAPI.getMyMeals(this.params);
			this.my_meals = response.data;
		},
		addNewMeal: function(new_meal) {
			this.my_meals.push(new_meal);
		},
		deleteMeal: function(meal_id) {
			for (let i = 0; i < this.my_meals.length; i++) {
				if (this.my_meals[i].id === meal_id) {
					this.my_meals.splice(i, 1);
					break
				}
			}
		},
		toggleFilters: function() {
			console.log("Toggle Filters");
			
		}
	},
	watch: {
		current_date: function() {
			this.params = {
				"date_from": this.current_date,
				"date_to": this.current_date
			}
			this.fetchMyMeals();
		}
	},
	created() {
		let today = new Date();
		this.current_date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
	}
}
</script>

<style scoped>
.my-meals-wrapper {
	display: flex;
	justify-content: space-around;
}

.meals-list {
	position: relative;
}

.count-calories {
	font-family: 'Dancing Script', cursive;
}

.count-calories h1 {
	margin: 0;
	font-size: 3em;
	display: inline;
}
.count-calories h1 span{
	margin: 0;
	font-size: 2rem;
}

.count-calories h4 {
	margin: 0;
	font-size: 1rem;
	display: inline;
	/* transform: translateX(3em); */
}

.green {
	color: green;
}

.red {
	color: red;
}

.gray {
	color: #888;
}

</style>
