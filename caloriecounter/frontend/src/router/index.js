import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import store from '@/store/index.js';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  hash: false,
  routes
})

router.beforeEach(async (to, from, next) => {

  if (to.path == '/login') {
    next();
  }
  
  await store.dispatch('fetchUser');

  const logged_user = store.getters.logged_user;
  
  if (logged_user.email) {
    next();
  }
  else if (from.path != '/login') {
    next("/login");
  }
  
  
  
	// if (to.matched.some(record => record.meta.requires_auth)) {
	// 	await store.dispatch('fetchCustomerGroup');
	// 	await store.dispatch('fetchUser');
	// 	await store.dispatch('fetchVersionNumber');

	// 	const logged_user = store.getters.logged_user;
	// 	const root_cg_permissions = store.getters.current_CG.root_customer_group_permissions;

	// 	if (
	// 		(logged_user.customer_permission == 'ADMIN' ||
	// 			logged_user.customer_permission == 'OPERATOR') &&
	// 		(root_cg_permissions.indexOf('Show Incident Manager dashboard only') >= 0 ||
	// 			root_cg_permissions.indexOf('Show Alert Cascade + Incident Manager dashboard') >= 0)
	// 	) {
	// 		next();
	// 	} else {
	// 		store.dispatch('logout');
	// 	}
	// } else {
	// 	store.dispatch('changeIncidentTemplate', location.host.split('.')[0]);
	// 	next();
	// }
});

export default router

