import axios from 'axios';

export default {
	async getAllUsers() {
		let response = await axios.get('http://localhost:8000/api/users');
		return response;
	},
	async updateUser(id, user) {
		let data = {
			"email": user.email,
			"permission": user.permission
		}
		let response = await axios.put(`http://localhost:8000/api/users/${id}`, data);
		return response;
	},
	async deleteUser(id) {
		let response = await axios.delete(`http://localhost:8000/api/users/${id}`);
		return response;
	},
	
	async getProfile(id) {
		let response = await axios.get(`http://localhost:8000/api/users/${id}/profile`);
		return response;
	},
	async patchProfile(id, expected_calories_per_day) {
		await axios.patch(`http://localhost:8000/api/users/${id}/profile`, {expected_calories_per_day});
	}
}