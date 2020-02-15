import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '@/store/index.js';

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
    meta: {
      requires_auth: false,
    },
  },
  {
    path: '/signup',
    name: 'Signup',
    component: () => import('../views/Signup.vue'),
    meta: {
      requires_auth: false,
    },
  },
  {
    path: '/',
    name: 'Diary',
    component: () => import('../views/Diary.vue'),
    meta: {
      requires_auth: true,
    },
  },
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('../views/Settings.vue'),
    meta: {
      requires_auth: true,
    },
  },
  {
    path: '/manage_users',
    name: 'ManageUsers',
    component: () => import('../views/ManageUsers.vue'),
    meta: {
      requires_auth: true,
    },
  },
  {
    path: '/manage_meals',
    name: 'ManageMeals',
    component: () => import('../views/ManageMeals.vue'),
    meta: {
      requires_auth: true,
    },
  }
]

const router = new VueRouter({
  mode: 'history',
  hash: false,
  routes
})


router.beforeEach(async (to, from, next) => {
	if (to.matched.some(record => record.meta.requires_auth)) {
		await store.dispatch('fetchUser');
		const logged_user = store.getters.logged_user;

		if (logged_user.id) {
			next();
		} else {
      store.dispatch('logout');
      next("/login");
		}
  } 
  else if (to.matched.some(record => !record.meta.requires_auth)){
		next();
  }
  else {
    next("/login");
  }
});

export default router

