<template>
	<div>
		<h1>Manage Users</h1>
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
