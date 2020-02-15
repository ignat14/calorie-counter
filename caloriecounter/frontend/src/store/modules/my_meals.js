import MyMealsAPI from '@/services/api/my_meals.js';


const state = {
	my_meals: []
};

const getters = {
	my_meals: state => state.my_meals
}

const actions = {
	async fetchMyMeals({ commit }, params) {
		let response = await MyMealsAPI.getMyMeals(params);
		commit('fetchMyMeals', response.data);
	},
	async filterMeals({ commit }, params) {
		let response = await MyMealsAPI.getMyMeals(params);
		commit('fetchMyMeals', response.data);
	}
}

const mutations = {
	fetchMyMeals: (state, my_meals) => state.my_meals = my_meals
}


export default {
	state,
	getters,
	actions,
	mutations
}