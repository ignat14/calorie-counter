import AllMealsAPI from '@/services/api/all_meals.js';


const state = {
	all_meals: []
};

const getters = {
	all_meals: state => state.all_meals
}

const actions = {
	async fetchAllMeals({ commit }) {
		let response = await AllMealsAPI.getAllMeals();
		commit('fetchAllMeals', response.data);
	},
	async filterMeals({ commit }, params) {
		let response = await AllMealsAPI.getAllMeals(params);
		commit('fetchAllMeals', response.data);
	},
	async createMeal({ commit }, meal) {
		let response = await AllMealsAPI.createMeal(meal);
		console.log(response.data);
		
		commit('createMeal', response.data);
	}
}

const mutations = {
	fetchAllMeals: (state, all_meals) => state.all_meals = all_meals,
	createMeal: (state, new_meal) => state.all_meals.push(new_meal)
}


export default {
	state,
	getters,
	actions,
	mutations
}