import axios from 'axios';
import router from '@/router/index.js';

axios.interceptors.request.use((config) => {
	if (localStorage.getItem("drf_token")) {
		config.headers['Authorization'] = 'Token ' + localStorage.getItem("drf_token");
	}
		return config;
	}, 
	(error) => {
		
		return Promise.reject(error)
	}
);

axios.interceptors.response.use((response) => {
	return response;
}, 
(error) => {
	if (error.response.status === 401 || error.response.status === 403) {
		router.push('/login');
			
	}
	return Promise.reject(error);
});