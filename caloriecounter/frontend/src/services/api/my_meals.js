import axios from 'axios';
import settings from '@/settings';

export default {
	async getMyMeals(params=null) {
		let response = await axios.get(`http://${settings.backend_domain}:${settings.backend_port}/api/my_meals`, {params});
		return response;
	},

	async createMyMeal(data) {
		let response = await axios.post(`http://${settings.backend_domain}:${settings.backend_port}/api/my_meals`, data);
		return response;
	},

	async patchMyMeal(data, id) {
		let response = await axios.patch(`http://${settings.backend_domain}:${settings.backend_port}/api/my_meals/${id}`, data);
		return response;
	},

	async deleteMyMeal(id) {
		await axios.delete(`http://${settings.backend_domain}:${settings.backend_port}/api/my_meals/${id}`);
	},
}