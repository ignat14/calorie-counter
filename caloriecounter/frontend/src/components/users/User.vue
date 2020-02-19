<template>
	<div class="user-main">

		<div class="user-title">
			<span>{{user.email}}</span> 
			<span v-if="!user.is_active" class="not-active"> (Not Active)</span>
		</div>


			<div class="user-details">

			<span>
				<input type="text" v-model="user.email"
								:class="{'invalid-input': error_email}">
								<!-- <p v-if="error_email" class="err-msg">{{error_email}}</p> -->
			</span>


			<span>
				<select v-model="user.permission" :class="{'invalid-input': error_permission}">
					<option>USER</option>
					<option>MANAGER</option>
					<option>ADMIN</option>
				</select>
				<!-- <p v-if="error_permission" class="err-msg">{{error_permission}}</p> -->
			</span>

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

				<div class="error-message">
					{{ error_message }}
				</div>
				<div class="success-message">
					{{ success_message }}
				</div>

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
			show_save_dialog: false,
			success_message: "",
			error_message: "",
			error_email: "",
			error_permission: ""
		}
	},
	methods: {
		saveUser: async function() {
			try {
				await UsersAPI.updateUser(this.user.id, this.user);
				this.show_save_dialog = false;
				this.success_message = "Saved Sucessfully";
				this.error_message = "";
				this.error_email = "";
				this.error_permission = "";
				this.clearSuccessMessages();
			}
			catch(err) {
				if (err.response.data.email) { this.error_email = err.response.data.email[0]; }
				else { this.error_email = ""}
				if (err.response.data.permission) { this.error_permission = err.response.data.permission[0]; }
				else { this.error_permission = ""}

				if (err.response.data.non_field_errors) { this.error_message = err.response.data.non_field_errors[0] }
				else { this.error_message = "" }
				if (this.error_email) {this.error_message = this.error_email}
				if (this.error_permission) {this.error_message = this.error_permission}

				this.success_message = ""
				this.show_save_dialog = false;
			}
		},
		deleteUser: function() {
		UsersAPI.deleteUser(this.user.id);
		this.$emit('deleteUser', this.user.id);
		},
		clearSuccessMessages: function() {
			setTimeout(() => {
					this.success_message = "";
				}, 2000);
		},
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

.not-active {
	color: gray;
	font-size: 1.1rem;
}

@media (max-width: 420px) {
	.user-main {
		margin: 0 100px;
	}
}

.invalid-input {
	border: 1px solid red;
}

.err-msg {
	color: red;
	margin: 0;
	padding: 0;
	font-size: 0.8rem;
}

.error-message {
	margin: 10px;
	color: red;
}

.success-message {
	margin: 10px;
	color: green;
}

</style>
