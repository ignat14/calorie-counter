<template>
	<div class="user-main">
		<div class="user-title">
			<span>{{user.email}}</span>
		</div>
		<div class="user-details">
			<input type="text" v-model="user.email">
			<select v-model="user.permission">
				<option>USER</option>
				<option>MANAGER</option>
				<option>ADMIN</option>
			</select>
			<button class="save" @click="saveUser()">Save</button>
			<button class="delete" @click="deleteUser()">Delete</button>

		</div>
	</div>
</template>

<script>
import UsersAPI from '@/services/api/users.js';

export default {
	name: "User",
	props: {
		user: Object
	},
	methods: {
		saveUser: function() {
			console.log("Saving user", this.user);
			UsersAPI.updateUser(this.user.id, this.user)
		},
		deleteUser: function() {
		UsersAPI.deleteUser(this.user.id);
		this.$emit('deleteUser', this.user.id);
			
		}
	}
}
</script>

<style scoped>

.user-main {
	display: grid;
  justify-content: center;
	margin: 0 200px;
}

.user-details {
	margin-bottom: 50px;
}

.user-main span {
	flex: 5;
}

.user-main input {
	flex: 1;
	padding: 10px;
	width: 200px;
	margin: 2px;
}

.user-main select {
	text-align: center;
	padding: 10px;
	background: #fff;
	border: 1px solid #999;
	width: 200px;
	margin: 2px;
}

.user-main button {
	width: 100px;
	padding: 10px;
	border: 1px solid #999;
	color: #fff;
	margin: 2px;
	cursor: pointer;
}

.save {
	background: rgb(59, 206, 83);
}

.delete {
	background: rgb(245, 94, 94);
}

@media (max-width: 420px) {
	.user-main {
		margin: 0 100px;
	}
}

</style>
