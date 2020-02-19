import axios from 'axios';
import settings from '@/settings';

export default {
	async getLoggedUser() {
		let response = await axios.get(`http://${settings.backend_domain}:${settings.backend_port}/api/users/self`);
		return response;
	},
	async login(data) {
		let response = await axios.post(`http://${settings.backend_domain}:${settings.backend_port}/api/auth/login/`, data);
		localStorage.cc_token = response.data.token;
		return response;
	},
	async signUp(data) {
		let response = await axios.post(`http://${settings.backend_domain}:${settings.backend_port}/api/auth/signup/`, data);
		return response;
	},
	async resetPassword(data) {
		let response = await axios.post(`http://${settings.backend_domain}:${settings.backend_port}/api/auth/password_reset/`, data);
		return response;
	},
	async resetPasswordConfirm(data) {
		let response = await axios.post(`http://${settings.backend_domain}:${settings.backend_port}/api/auth/password_reset/confirm/`, data);
		return response;
	},
	logOut: async () => await axios.post(`http://${settings.backend_domain}:${settings.backend_port}/api/auth/logout/`, {})
}