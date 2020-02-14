import axios from 'axios';

export default {
	async getMyMeals(params=null) {
		console.log(params);
		
		let response = await axios.get('http://localhost:8000/api/my_meals', {params});
		return response;
	},

	async createMyMeal(data) {
		let response = await axios.post('http://localhost:8000/api/my_meals', data);
		return response;
	},

	async patchMyMeal(data, id) {
		let response = await axios.patch(`http://localhost:8000/api/my_meals/${id}`, data);
		return response;
	},

	async deleteMyMeal(id) {
		await axios.delete(`http://localhost:8000/api/my_meals/${id}`);
	},
}