<template>
	<div class="my-meals-wrapper">

		<div class="meals-list">
			<div class="main-settings-menu">

				<DiaryDaySelect v-model="current_date" v-if="!show_filters" />

				<div class="open-modal-icon filter" @click="toggleFilters()">
						<i class="fas fa-sliders-h" v-if="!show_filters"></i>
						<i class="far fa-calendar-check" v-if="show_filters"></i>
				</div>

			<div class="datetime-filters" v-if="show_filters">
				<div class="date-range" data-label="Date Range">
					<VueCtkDateTimePicker v-model="date_range"
																class="date-picker-input"
																format="YYYY-MM-DD"
																formatted="ll"
																:range="true"
																label="Select date range"
																@input="dateRangeChange()"
																@validate="fetchMyMeals(params)"
																@is-hidden="fetchMyMeals(params)"
					></VueCtkDateTimePicker>
				</div>
				<div class="time-range" data-label="Time Range">
					<VueCtkDateTimePicker v-model="time_from"
																class="time-picker-input"
																:only-time="true"
																label="From"
																format="HH:mm:ss"
																formatted="hh:mm a"
																:minuteInterval="10"
																@input="timeFromChange()"
																@validate="fetchMyMeals(params)"
																@is-hidden="fetchMyMeals(params)"
					></VueCtkDateTimePicker> <span>-</span>
					<VueCtkDateTimePicker v-model="time_to"
																class="time-picker-input"
																:only-time="true"
																label="To"
																format="HH:mm:ss"
																formatted="hh:mm a"
																:minuteInterval="10"
																@input="timeToChange()"
																@validate="fetchMyMeals(params)"
																@is-hidden="fetchMyMeals(params)"
					></VueCtkDateTimePicker>
				</div>
			</div>


				<div class="count-calories">
					<h1 :class="{'green': calories_balance && !show_filters, 
											'red': !calories_balance && !show_filters, 
											'gray': !expected_calories || show_filters}">
						{{ all_calories }}<span>Cals</span>
					</h1>
					<h4 v-if="expected_calories && !show_filters">
						/ {{ expected_calories }} Cals
					</h4>
				</div>

			</div>

			<div v-for="meal in my_meals" :key="meal.id">
				<DiaryMeal :meal="meal" @deleteMeal="deleteMeal"/>
			</div>

			<AddMeal :current_date="current_date" @addNewMeal="addNewMeal" v-if="!show_filters" />

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
			show_filters: false,
			params: {},
			date_range: {
				"start": null,
				"end": null,
				"shortcut": "month"
			},
			time_from: "",
			time_to: "",
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
		dateRangeChange: function() {
			if (this.date_range && this.date_range.start) {
				this.$set(this.params, "date_from", this.date_range.start);
			}
			else {
				this.$delete(this.params, "date_from");
				this.fetchMyMeals(this.params);
			}
			if (this.date_range && this.date_range.end) {
				this.$set(this.params, "date_to", this.date_range.end);
			}
			else {
				this.$delete(this.params, "date_to");
			}
		},
		timeFromChange: function() {
			if (this.time_from) {
				this.$set(this.params, "time_from", this.time_from);
			}
			else {
				this.$delete(this.params, "time_from");
				this.fetchMyMeals(this.params);
			}
		},
		timeToChange: function() {
			if (this.time_to) {
				this.$set(this.params, "time_to", this.time_to);
			}
			else {
				this.$delete(this.params, "time_to");
				this.fetchMyMeals(this.params);
			}
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
			this.show_filters = !this.show_filters;
			if (!this.show_filters) {
				this.params = {
				"date_from": this.current_date,
				"date_to": this.current_date
			}
			this.fetchMyMeals();
			}
			else {
				this.date_range = {
					"start": null,
					"end": null,
					"shortcut": "month"
				}
				this.time_from = ""
				this.time_to = ""
			}
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

.datetime-filters {
	display: flex;
	justify-content: center;
	padding: 5px 0;
}

.time-range {
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 0 2px;
}

.time-range span {
	padding: 0 2px;
}

.date-picker-input {
	width: 225px;
}

.time-picker-input {
	width: 120px;
}

@media (max-width: 600px) {
	.datetime-filters {
		flex-direction: column;
	}
	.time-range {
		margin: 0 25%;
	}
}

@media (max-width: 450px) {
	.time-range {
		margin: 0 10%;
	}
}

@media (max-width: 340px) {
	.date-range {
		margin-right: 20px;
	}
}

</style>
