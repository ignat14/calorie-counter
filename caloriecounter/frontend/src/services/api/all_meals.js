import axios from 'axios';

export default {
	async getAllMeals(params=null) {
		let response = await axios.get('http://localhost:8000/api/all_meals', {params});
		return response;
	},
	async updateMeal(id, data) {
		let response = await axios.put(`http://localhost:8000/api/all_meals/${id}`, data);
		return response;
	},
	async deleteMeal(id) {
		let response = await axios.delete(`http://localhost:8000/api/all_meals/${id}`);
		return response;
	}
}