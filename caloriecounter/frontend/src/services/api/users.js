import axios from 'axios';
import settings from '@/settings';

export default {
	async getAllUsers() {
		let response = await axios.get(`http://${settings.backend_domain}:${settings.backend_port}/api/users`);
		return response;
	},
	async updateUser(id, user) {
		let data = {
			"email": user.email,
			"permission": user.permission
		}
		let response = await axios.put(`http://${settings.backend_domain}:${settings.backend_port}/api/users/${id}`, data);
		return response;
	},
	async deleteUser(id) {
		let response = await axios.delete(`http://${settings.backend_domain}:${settings.backend_port}/api/users/${id}`);
		return response;
	},
	
	async getProfile(id) {
		let response = await axios.get(`http://${settings.backend_domain}:${settings.backend_port}/api/users/${id}/profile`);
		return response;
	},
	async patchProfile(id, expected_calories_per_day) {
		await axios.patch(`http://${settings.backend_domain}:${settings.backend_port}/api/users/${id}/profile`, {expected_calories_per_day});
	},
	async changePassword(data) {
		await axios.put(`http://${settings.backend_domain}:${settings.backend_port}/api/users/self/password_change`, data);
	}
}