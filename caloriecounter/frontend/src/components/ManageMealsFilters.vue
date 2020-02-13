<template>
	<div class="filters-main">
		<div class="datetime-filters">
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
			<VueCtkDateTimePicker v-model="time_from"
														class="time-picker-input"
														:only-time="true"
														label="Select start time"
														format="HH:mm:ss"
														formatted="hh:mm a"
														:minuteInterval="10"
			></VueCtkDateTimePicker> - 
			<VueCtkDateTimePicker v-model="time_to"
														class="time-picker-input"
														:only-time="true"
														label="Select end time"
														format="HH:mm:ss"
														formatted="hh:mm a"
														:minuteInterval="10"
			></VueCtkDateTimePicker>
		</div>

		<div>
			<label>User</label> <input type="text" v-model="user" @change="userChange()">
			<label>Search</label> <input type="text" v-model="search_val">
		</div>
	</div>
</template>

<script>
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
			user: ""
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
		userChange: function() {
			if (this.user) {
				this.$set(this.params, "user", this.user);
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
	}
}
</script>

<style scoped>

.filters-main {
	display: flex;
	flex-direction: column;
}

.datetime-filters {
	display: flex;
}

.date-picker-input {
	width: 250px;
}

.time-picker-input {
	width: 155px;
}

input {
	padding: 5px;
}

</style>
