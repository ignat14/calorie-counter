import UsersAPI from '@/services/api/users.js';
import AuthAPI from '@/services/api/auth.js';

const state = {
	all_users: []
};

const getters = {
	all_users: state => state.all_users
}

const actions = {
	async fetchAllUsers({ commit }) {
		let response = await UsersAPI.getAllUsers();
		commit('fetchAllUsers', response.data);
	},
	async createUser({ commit }, new_user) {
		let response = await AuthAPI.signUp(new_user);

		commit('createUser', response.data);
	}
}

const mutations = {
	fetchAllUsers: (state, all_users) => state.all_users = all_users,
	createUser: (state, new_user) => state.all_users.push(new_user)
}


export default {
	state,
	getters,
	actions,
	mutations
}