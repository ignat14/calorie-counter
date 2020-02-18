<template>
	<div v-if="all_meals_filter_modal" class="modal-dark-backround">

		<div class="main-modal">
			<h1>Filter Meals</h1>
			<i class="fas fa-times exit-modal" @click="toggleAllMealsFilterModal(false)"></i>

			<div class="modal-form">

				<div class="modal-form-item">
					<label for="user">User</label>
					<select v-model="user_id">
						<option v-for="user in all_users" :key="user.id" :value="user.id">{{user.email}}</option>
						<option value="">All</option>
					</select>
				</div>

				<div class="modal-form-item">
					<label for="date-range">Date Range</label>
					<VueCtkDateTimePicker v-model="date_range"
															class="date-picker-input"
															label=""
															:no-label="true"
															format="YYYY-MM-DD"
															formatted="ll"
															:range="true"
				></VueCtkDateTimePicker>
				</div>

				<div class="modal-form-item">
					<label for="date-range">Time From</label>
					<VueCtkDateTimePicker v-model="time_from"
																class="time-picker-input"
																:only-time="true"
																label=""
																:no-label="true"
																format="HH:mm"
																formatted="HH:mm"
																:minuteInterval="10"
					></VueCtkDateTimePicker>
				</div>

				<div class="modal-form-item">
					<label for="date-range">Time To</label>
					<VueCtkDateTimePicker v-model="time_to"
															class="time-picker-input"
															:only-time="true"
															label=""
															:no-label="true"
															format="HH:mm"
															formatted="HH:mm"
															:minuteInterval="10"
				></VueCtkDateTimePicker>
				</div>

				<div class="modal-form-item">
					<label for="date-range">Description</label>
					<input type="text" v-model="description">
				</div>

				<button @click="filterMealsClicked()">Filter Meals</button>

			</div>

		</div>

	</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
	name: "AddUserModal",
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
			description: "",
			user_id: null
		}
	},
	computed: {
		...mapGetters(['all_meals_filter_modal', 'all_users'])
	},
	methods: {
		...mapActions(['toggleAllMealsFilterModal', 'filterMeals']),
		setParams: function(obj, name) {
			if (obj) { this.$set(this.params, name, obj)}
			else { this.$delete(this.params, name) }
		},
		filterMealsClicked: async function() {
			this.setParams(this.user_id, "user")
			this.setParams(this.time_from, "time_from")
			this.setParams(this.time_to, "time_to")
			this.setParams(this.description, "description")

			if (this.date_range && this.date_range.start) {
				this.$set(this.params, "date_from", this.date_range.start);
			} else { this.$delete(this.params, "date_from"); }

			if (this.date_range && this.date_range.end) {
				this.$set(this.params, "date_to", this.date_range.end);
			} else { this.$delete(this.params, "date_to"); }
			
			await this.filterMeals(this.params);
			this.toggleAllMealsFilterModal(false);
		}
	}
}
</script>

<style scoped>

</style>