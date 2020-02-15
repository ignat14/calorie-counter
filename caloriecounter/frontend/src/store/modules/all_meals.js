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
	}
}

const mutations = {
	fetchAllMeals: (state, all_meals) => state.all_meals = all_meals
}


export default {
	state,
	getters,
	actions,
	mutations
}