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


			

			<span class="btn-wrapper">
				<button class="save" @click="show_save_dialog = !show_save_dialog">Save</button>
				<ConfirmDialog
					v-if="show_save_dialog"
					text="Are you sure you want to save this user?"
					@yes="saveUser()"
					@no="show_save_dialog = false" 
				/>
			</span>

			<span class="btn-wrapper">
				<button class="delete" @click="show_delete_dialog = !show_delete_dialog">Delete</button>
				<ConfirmDialog
					v-if="show_delete_dialog"
					text="Are you sure you want to delete this user?"
					@yes="deleteUser()"
					@no="show_delete_dialog = false" 
				/>
			</span>

		</div>
	</div>
</template>

<script>
import UsersAPI from '@/services/api/users.js';
import ConfirmDialog from '@/components/utils/ConfirmDialog.vue';

export default {
	name: "User",
	components: {
		ConfirmDialog
	},
	props: {
		user: Object
	},
	data() {
		return {
			show_delete_dialog: false,
			show_save_dialog: false
		}
	},
	methods: {
		saveUser: function() {
			UsersAPI.updateUser(this.user.id, this.user);
			this.show_save_dialog = false;
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
	position: relative;
	background: rgb(245, 94, 94);
}

.btn-wrapper {
	position: relative;
}

@media (max-width: 420px) {
	.user-main {
		margin: 0 100px;
	}
}

</style>
