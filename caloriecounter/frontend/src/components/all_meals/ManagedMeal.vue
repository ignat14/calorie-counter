<template>
	<div class="managed-meal-main">
		<select v-model="meal.user" @change="userChange()" class="mm-input user">
			<option v-for="user in all_users" :key="user.id" :value="user.id">{{user.email}}</option>
		</select>
		<div class="date-time">
			<div class="mm-input date-picker-div">
				<VueCtkDateTimePicker v-model="meal.date"
															class="date-picker-input"
															:only-date="true"
															label="Select Date"
															format="YYYY-MM-DD"
															formatted="ll"
				></VueCtkDateTimePicker>
			</div>
			<div class="mm-input date-picker-div time">
				<VueCtkDateTimePicker v-model="meal.time"
															class="time-picker-input"
															:only-time="true"
															label="Select Time"
															format="HH:mm:ss"
															formatted="hh:mm a"
															:minuteInterval="10"
				></VueCtkDateTimePicker>
			</div>
		</div>
		<input class="mm-input desc" type="text" name="description" v-model="meal.description">
		<input class="mm-input cals" type="number" name="calories" v-model="meal.calories">
		<div class="save-delete">

			<span class="btn-wrapper">
				<button class="save" @click="show_save_dialog = !show_save_dialog">Save</button>
				<ConfirmDialog
						v-if="show_save_dialog"
						text="Are you sure you want to save this meal?"
						@yes="updateMeal()"
						@no="show_save_dialog = false" 
					/>
			</span>

			<span class="btn-wrapper">
				<button class="delete" @click="show_delete_dialog = !show_delete_dialog">Delete</button>
				<ConfirmDialog
					v-if="show_delete_dialog"
					text="Are you sure you want to delete this meal?"
					@yes="deleteMeal()"
					@no="show_delete_dialog = false" 
				/>
			</span>

		</div>
	</div>
</template>

<script>
import AllMealsAPI from '@/services/api/all_meals.js';
import ConfirmDialog from '@/components/utils/ConfirmDialog.vue';
import { mapGetters } from 'vuex';

export default {
	name: "ManagedMeal",
	components: {
		ConfirmDialog
	},
	props: {
		meal: Object
	},
	data() {
		return {
			show_save_dialog: false,
			show_delete_dialog: false
		}
	},
	computed: {
		...mapGetters(['all_users'])
	},
	methods: {
		updateMeal: function() {
			AllMealsAPI.updateMeal(this.meal.id, this.meal);
			this.show_save_dialog = false
		},
		deleteMeal: async function() {
			await AllMealsAPI.deleteMeal(this.meal.id);
			this.$emit("deleteMeal", this.meal.id);
		}
	}
}
</script>

<style scoped>

.managed-meal-main {
	display: grid;
	grid-template-columns: 2fr 2fr 1fr 1fr 2fr;
	grid-template-areas: "user date-time desc cals save-del";
	justify-content: center;
	margin: 30px 500px;
}

.mm-input {
	margin: 2px;
	/* padding: 10px 5px; */
	text-align: center;
}

.user {
	grid-area: user;
	padding: 5px 2px;
	background: #fff;
}

.date-time {
	grid-area: date-time;
	display: flex;
}

.desc {
	grid-area: desc;
	width: 250px;
}

.cals {
	grid-area: cals;
	width: 100px;
}

.save-delete {
	grid-area: save-del;
	display: flex;
	align-items: center;
}

.date-picker-div {
	width: 150px;
}

.btn-wrapper {
	position: relative;
}

.save {
	background: rgb(59, 206, 83);
	width: 70px;
	padding: 12px;
	margin: 0 2px;
	border: 1px solid #999;
	color: #fff;
	cursor: pointer;
}

.delete {
	background: rgb(245, 94, 94);
	padding: 12px;
	margin: 0 2px;
	width: 70px;
	border: 1px solid #999;
	color: #fff;
	cursor: pointer;
}

@media (max-width: 1240px) {
	.managed-meal-main {
		grid-template-columns: 1fr 1fr 3fr;
		grid-template-areas: 
					"user date-time date-time"
					"desc cals save-del";
		margin: 30px 400px;
	}
	.desc {
		padding: 10px 0;
	}
}

@media (max-width: 780px) {
	.managed-meal-main {
		grid-template-columns: 1fr 1fr;
		grid-template-areas: 
					"user user"
					"date-time date-time"
					"desc desc"
					"cals save-del";
		margin: 30px 300px;
	}
	.cals {
		padding: 10px;
	}
}

@media (max-width: 615px) {
	.managed-meal-main {
		margin: 30px 200px;
	}
}

@media (max-width: 400px) {
	.managed-meal-main {
		margin: 30px 100px;
	}
}

</style>
