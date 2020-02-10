import axios from 'axios';

export default {
	getLoggedUser: async () => await axios.get('http://localhost:8000/api/users/self'),
	logOut: async () => await axios.post('http://localhost:8000/api/logout/', {})
}