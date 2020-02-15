<template>
	<div class="filters-main">

			<div class="mm-filter" data-label="User">
				<select v-model="user_id" @change="userChange()">
					<option v-for="user in users" :key="user.id" :value="user.id">{{user.email}}</option>
					<option value="">All</option>
				</select>
			</div>

			<div class="mm-filter" data-label="Date Range">
				<VueCtkDateTimePicker v-model="date_range"
															class="date-picker-input"
															format="YYYY-MM-DD"
															formatted="ll"
															:range="true"
															label="Select date range"
															@input="dateRangeChange()"
															@validate="filterMeals(params)"
															@is-hidden="filterMeals(params)"
				></VueCtkDateTimePicker>
			</div>
			<div class="mm-filter" data-label="Time Range">
				<VueCtkDateTimePicker v-model="time_from"
															class="time-picker-input"
															:only-time="true"
															label="From"
															format="HH:mm:ss"
															formatted="hh:mm a"
															:minuteInterval="10"
															@input="timeFromChange()"
															@validate="filterMeals(params)"
															@is-hidden="filterMeals(params)"
				></VueCtkDateTimePicker> - 
				<VueCtkDateTimePicker v-model="time_to"
															class="time-picker-input"
															:only-time="true"
															label="To"
															format="HH:mm:ss"
															formatted="hh:mm a"
															:minuteInterval="10"
															@input="timeToChange()"
															@validate="filterMeals(params)"
															@is-hidden="filterMeals(params)"
				></VueCtkDateTimePicker>
			</div>

		<div class="mm-filter" data-label="Description">
			<input type="text" v-model="search_val">
		</div>
		

	</div>
</template>

<script>
import UsersAPI from '@/services/api/users.js';
import { mapActions } from 'vuex';

export default {
	name: "ManageMealsFilters",
	data() {
		return {
			params: {},
			date_range: {
				"start": null,
				"end": null,
				"shortcut": "month"
			},
			time_from: "",
			time_to: "",
			search_val: "",
			user_id: null,
			users: []
		}
	},
	methods: {
		...mapActions(['filterMeals']),
		dateRangeChange: function() {
			if (this.date_range && this.date_range.start) {
				this.$set(this.params, "date_from", this.date_range.start);
			}
			else {
				this.$delete(this.params, "date_from");
				this.filterMeals(this.params);
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
				this.filterMeals(this.params);
			}
		},
		timeToChange: function() {
			if (this.time_to) {
				this.$set(this.params, "time_to", this.time_to);
			}
			else {
				this.$delete(this.params, "time_to");
				this.filterMeals(this.params);
			}
		},
		userChange: function() {
			if (this.user_id) {
				this.$set(this.params, "user", this.user_id);
			}
			else {
				this.$delete(this.params, "user");
			}
			this.filterMeals(this.params);
		}
	},
	watch: {
		'search_val': function(val) {
			if (this.timeout) clearTimeout(this.timeout); 
				this.timeout = setTimeout(() => {
					if (val.length > 0) {
						this.$set(this.params, "description", val);
					}
					else {
						this.$delete(this.params, "description");
					}
					this.filterMeals(this.params);
				}, 200);
		}
	},
	created: async function() {
		let response = await UsersAPI.getAllUsers();
		this.users = response.data;
	}
}
</script>

<style scoped>

.filters-main {
	display: flex;
	justify-content: center;
	margin-top: 35px;
	margin-bottom: 10px;
}

.mm-filter {
	margin: 0 5px;
}

.mm-filter {
	position: relative;
	display: flex;
	justify-content: center;
	align-items: center;
}

.mm-filter::after {
	content: attr(data-label);
	position: absolute;
	top: -27px;
	left: 50%;
	transform: translateX(-50%);
	border-bottom: 1px solid #000;
	font-weight: bold;
}

.mm-filter input {
	padding: 10px;
}

.mm-filter select {
	text-align: center;
	padding: 10px;
	background: #fff;
	border: 1px solid #999;
	width: 200px;
	margin: 2px;
}

.datetime-filters {
	display: flex;
}

.date-picker-input {
	width: 230px;
}

.time-picker-input {
	width: 120px;
	margin: 0 5px;
}

input {
	padding: 5px;
}

@media (max-width: 1040px) {
	.mm-filter select {
		width: 150px;
	}
	.mm-filter input {
		width: 120px;
	}
}

</style>
