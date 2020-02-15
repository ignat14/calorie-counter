<template>
	<div>
		<div class="main-settings-menu">
			<h1>Manage Users</h1>
			<div class="open-modal-icon" @click="toggleAddUserModal(true)">
				<i class="fas fa-plus"></i>
				<!-- <i class="fas fa-user-plus"></i> -->
			</div>
		</div>
		<UsersList />
		<AddUserModal />
	</div>
</template>

<script>
import UsersList from '@/components/users/UsersList.vue';
import AddUserModal from '@/components/modals/AddUser.vue';
import { mapActions } from 'vuex';

export default {
	name: 'ManageUsers',
	components: {
		UsersList,
		AddUserModal
	},
	methods: {
		...mapActions(['toggleAddUserModal'])
	}
}
</script>

<style scoped>

</style>
