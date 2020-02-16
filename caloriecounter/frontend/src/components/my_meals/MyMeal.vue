<template>
	<div class="meal-box">
		
		<span class="input-wrapper">
			<VueCtkDateTimePicker v-model="meal.time"
														:only-time="true"
														format="HH:mm:ss"
														formatted="hh:mm a"
														:minuteInterval="10"
														@validate="patchTime()"
														@is-hidden="patchTime()"
			>
				<input class="meal-input time-input" type="text" readonly
								:class="{'is-invalid': error_time, 'is-valid': success_time}">
			</VueCtkDateTimePicker>

			<div v-if="success_time" class="success-msg">{{success_time}}</div>
			<div v-if="error_time" class="error-msg">Value is invalid</div>
		</span>

		<span class="input-wrapper">
			<input type="text" 
							class="meal-input" 
							v-model="meal.description"
							@change="patchDescription()"
							:class="{'is-invalid': error_description, 'is-valid': success_description}">
			<div v-if="success_description" class="success-msg">{{success_description}}</div>
			<div v-if="error_description" class="error-msg">Value is invalid</div>
		</span>

		<span class="input-wrapper">
			<input type="number" 
							class="meal-input" 
							v-model.number="meal.calories" 
							@change="patchCalories()"
							:class="{'is-invalid': error_calories, 'is-valid': success_calories}">
			<div v-if="success_calories" class="success-msg">{{success_calories}}</div>
			<div v-if="error_calories" class="error-msg">Value is invalid</div>
		</span>

		<div class="delete-meal-wrapper">
			<i class="fas fa-times delete-icon" @click="show_delete_dialog = !show_delete_dialog"></i>
			<ConfirmDialog
						v-if="show_delete_dialog"
						text="Are you sure you want to delete this meal?"
						@yes="deleteMeal"
						@no="show_delete_dialog = false" 
			/>
		</div>
	</div>
</template>

<script>
import ConfirmDialog from '@/components/utils/ConfirmDialog.vue';
import MyMealAPI from '@/services/api/my_meals.js';

export default {
	name: 'Meal',
	components: {
		ConfirmDialog
	},
	props: {
		meal: Object,
	},
	data() {
		return {
			display: true,
			show_delete_dialog: false,
			success_description: "",
			success_calories: "",
			success_time: "",
			error_description: "",
			error_calories: "",
			error_time: ""
		};
	},
	methods: {
		patchTime: async function() {
			let data = {'time': this.meal.time}
			try {
				await MyMealAPI.patchMyMeal(data, this.meal.id);
				this.success_time = "Updated";
				this.error_time = "";
				this.clearTimeMessages();
			}
			catch (err)
			{
				this.error_time = err.response.data.time;
				this.success_time = "";
				this.clearTimeMessages();
			}
		},
		patchDescription: async function() {
			let data = {'description': this.meal.description};
			try {
				await MyMealAPI.patchMyMeal(data, this.meal.id);
				this.success_description = "Updated";
				this.error_description = "";
				this.clearDescMessages();
			}
			catch (err) {
				this.error_description = err.response.data.description;
				this.success_description = "";
				this.clearDescMessages();
			}
		},
		patchCalories: async function() {
			let data = {'calories': this.meal.calories}
			try {
				await MyMealAPI.patchMyMeal(data, this.meal.id);
				this.success_calories = "Updated";
				this.error_calories = "";
				this.clearCalsMessages();
			}
			catch (err) {
				this.error_calories = err.response.data.calories;
				this.success_calories = "";
				this.clearCalsMessages();
			}
		},
		patchMeal: async function(data) {
			let response = await MyMealAPI.patchMyMeal(data, this.meal.id);
			return response.data;
		},
		deleteMeal: async function() {
			await MyMealAPI.deleteMyMeal(this.meal.id);
			this.$emit('deleteMeal', this.meal.id);
		},
		clearTimeMessages: function() {
			setTimeout(() => {
					this.success_time = "";
					this.error_time = "";
				}, 2000);
		},
		clearDescMessages: function() {
			setTimeout(() => {
					this.success_description = "";
					this.error_description = "";
				}, 2000);
		},
		clearCalsMessages: function() {
			setTimeout(() => {
					this.success_calories = "";
					this.error_calories = "";
				}, 2000);
		}
	},
	watch: {
		'meal.calories': function() {
			if (this.meal.calories == "" || this.meal.calories < 0) {
				this.meal.calories = 0;
			}
		}
	}
}
</script>

<style>

.meal-box {
	display: flex;
	justify-content: center;
	align-items: center;
}

.meal-input {
	width: 150px;
	margin: 10px;
	margin-top: 10px;
	padding: 10px;
	text-align: center;
	outline: none;
	border: none;
	border-bottom: 1px solid gray;
	font-size: 1.3em;
}

.time-input {
	cursor: pointer;
}

.delete-meal-wrapper {
	position: relative;
}

.delete-icon {
	cursor: pointer;
	font-size: 1.4rem;
	padding: 10px;
}

.delete-icon:hover {
	transform: scale(1.2);
}

@media (max-width: 640px) {
	.meal-box {
		flex-direction: column;
	}
}


.input-wrapper {
	position: relative;
}

.is-invalid {
	border-bottom: 1px solid red;
}

.is-valid {
	border-bottom: 1px solid green;
}

.error-msg {
	position: absolute;
	top: 90%;
	left: 5%;
	color: red;
	font-size: 0.8rem;
}

.success-msg {
	position: absolute;
	top: 90%;
	left: 5%;
	color: green;
	font-size: 0.8rem;
}

</style>
