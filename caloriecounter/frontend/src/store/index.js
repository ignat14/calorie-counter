import Vue from 'vue';
import Vuex from 'vuex';
import authAPI from '@/services/api/auth.js';

import my_meals from './modules/my_meals.js';
import all_meals from './modules/all_meals.js';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    my_meals,
    all_meals
  },
  state: {
    logged_user: {},
    left_menu_show: false,
    right_menu_show: false,
    add_user_modal: false,
    add_meal_modal: false,
    all_meals_filter_modal: false
  },
  getters: {
    logged_user: (state) => state.logged_user,
    left_menu_show: (state) => state.left_menu_show,
    right_menu_show: (state) => state.right_menu_show,
    add_user_modal: (state) => state.add_user_modal,
    add_meal_modal: (state) => state.add_meal_modal,
    all_meals_filter_modal: (state) => state.all_meals_filter_modal
  },
  actions: {
    async fetchUser({commit}) {
      const response = await authAPI.getLoggedUser();
      commit('fetchUser', response.data)
    },
    toggleLeftMenu({commit}, value ) {
			commit('toggleLeftMenu', value)
    },
    toggleRightMenu({commit}, value ) {
			commit('toggleRightMenu', value)
    },
    toggleAddUserModal({commit}, value) {
      commit('toggleAddUserModal', value)
    },
    toggleAddMealModal({commit}, value) {
      commit('toggleAddMealModal', value)
    },
    toggleAllMealsFilterModal({commit}, value) {
      commit('toggleAllMealsFilterModal', value)
    },
    logout({commit}) {
      authAPI.logOut();
      localStorage.removeItem("drf_token");
      commit('clearUser');
    }
  },
  mutations: {
    fetchUser: (state, logged_user) => state.logged_user = logged_user,
    clearUser: (state) => state.logged_user = {},
    toggleLeftMenu: (state, value) => state.left_menu_show = value,
    toggleRightMenu: (state, value) => state.right_menu_show = value,
    toggleAddUserModal: (state, value) => state.add_user_modal = value,
    toggleAddMealModal: (state, value) => state.add_meal_modal = value,
    toggleAllMealsFilterModal: (state, value) => state.all_meals_filter_modal = value
  }
})
