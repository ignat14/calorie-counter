import Vue from 'vue';
import Vuex from 'vuex';
import authAPI from '@/services/api/auth.js';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    logged_user: {}
  },
  getters: {
    logged_user: (state) => state.logged_user
  },
  actions: {
    async fetchUser( {commit} ) {
      const response = await authAPI.getLoggedUser();
      commit('fetchUser', response.data)
    },
    logout( {commit} ) {
      console.log("STORE");
      
      authAPI.logOut();
      localStorage.removeItem("drf_token");
      commit('clearUser');
    }
  },
  mutations: {
    fetchUser: (state, logged_user) => state.logged_user = logged_user,
    clearUser: (state) => state.logged_user = {},
  },
  modules: {
  }
})
