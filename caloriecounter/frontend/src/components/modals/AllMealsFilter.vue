<template>
	<div v-if="all_meals_filter_modal" class="modal-dark-backround">

		<div class="main-modal">
			<h1>Filter Meals</h1>
			<i class="fas fa-times exit-modal" @click="toggleAllMealsFilterModal(false)"></i>

			<!-- <div class="modal-form">
				<div class="modal-form-item">
					<label for="email">Email</label>
					<input type="email">
				</div>
				<div class="modal-form-item">
					<label for="email">Permission</label>
					<select v-model="all_users">
						<option>USER</option>
						<option>MANAGER</option>
						<option>ADMIN</option>
					</select>
				</div>
				<button>Add User</button>
			</div> -->

		</div>

	</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
	name: "AddUserModal",
	computed: {
		...mapGetters(['all_meals_filter_modal', 'all_users'])
	},
	methods: {
		...mapActions(['toggleAllMealsFilterModal'])
	}
}
</script>

<style scoped>

</style>