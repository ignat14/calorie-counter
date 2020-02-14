<template>
	<div>
		<div class="main-settings-menu">
			<h1>Manage Users
				<i class="far fa-plus-square"></i>
			</h1>
		</div>
		<UsersList />
	</div>
</template>

<script>
import UsersList from '@/components/UsersList.vue';

export default {
	name: 'ManageUsers',
	components: {
		UsersList
	}
}
</script>

<style>

</style>
