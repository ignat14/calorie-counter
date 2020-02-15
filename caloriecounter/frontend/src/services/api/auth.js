import axios from 'axios';

export default {
	async signUp(data) {
		let response = await axios.post('http://localhost:8000/api/auth/signup', data);
		return response;
	},
	getLoggedUser: async () => await axios.get('http://localhost:8000/api/users/self'),
	logOut: async () => await axios.post('http://localhost:8000/api/logout/', {})
}