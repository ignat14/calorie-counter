import axios from 'axios';
import settings from '@/settings';

export default {
	async getAllMeals(params=null) {
		let response = await axios.get(`http://${settings.backend_domain}:${settings.backend_port}/api/all_meals`, {params});
		return response;
	},
	async createMeal(data) {
		let response = await axios.post(`http://${settings.backend_domain}:${settings.backend_port}/api/all_meals`, data);
		return response;
	},
	async updateMeal(id, data) {
		let response = await axios.put(`http://${settings.backend_domain}:${settings.backend_port}/api/all_meals/${id}`, data);
		return response;
	},
	async deleteMeal(id) {
		let response = await axios.delete(`http://${settings.backend_domain}:${settings.backend_port}/api/all_meals/${id}`);
		return response;
	}
}