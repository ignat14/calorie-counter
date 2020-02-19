from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework.authtoken.models import Token

from .models import User
from meals.models import Meal
from caloriecounter.utils import test_setup


class UsersAPITestCase(APITestCase):

	def setUp(self):
		test_setup()

	def test_get_users_list_successful(self):
		"""Test to get users list with admin or manager --- successfully"""
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		url = api_reverse("api-users:users-list")
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		url = api_reverse("api-users:users-list")
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_users_list_not_allowed(self):
		"""Test to get users list with user --- not allowed"""
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:users-list")
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_get_user_successful(self):
		"""Test to get user with admin or manager --- successfully"""
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		url = api_reverse("api-users:users-rud", [admin.id])
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		url = api_reverse("api-users:users-rud", [admin.id])
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_user_not_allowed(self):
		"""Test to get user with user --- not allowed"""
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:users-rud", [user.id])
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_update_user_successful(self):
		"""Test MANAGER user updating normal USER"""
		data = {
			"email": "test@test.com",
			"permission": "MANAGER"
		}
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		user = User.objects.get(email="user@test.com")
		url = api_reverse("api-users:users-rud", [user.id])
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_user_for_manager_not_allowed_to_upgrade_to_admin(self):
		"""Test MANAGER USER trying to upgrade someone to ADMIN"""
		data = {
			"email": "test@test.com",
			"permission": "ADMIN"
		}
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		user = User.objects.get(email="user@test.com")
		url = api_reverse("api-users:users-rud", [user.id])
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_update_user_for_manager_not_allowed_to_downgrade_from_admin(self):
		"""Test MANAGER USER trying to downgrade ADMIN"""
		data = {
			"email": "test@test.com",
			"permission": "MANAGER"
		}
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		admin = User.objects.get(email="admin@test.com")
		url = api_reverse("api-users:users-rud", [admin.id])
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_update_user_change_own_permission(self):
		"""Test changeing own permission --- not allowed"""
		data = {
			"email": "manager@test.com",
			"permission": "ADMIN"
		}
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		url = api_reverse("api-users:users-rud", [manager.id])
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_patch_user_successful(self):
		"""Test ADMIN user patching normal USER"""
		data = {
			"permission": "MANAGER"
		}
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		user = User.objects.get(email="user@test.com")
		url = api_reverse("api-users:users-rud", [user.id])
		response = self.client.patch(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_user_successful(self):
		"""Test ADMIN user deleting normal USER"""
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		user = User.objects.get(email="user@test.com")
		url = api_reverse("api-users:users-rud", [user.id])
		response = self.client.delete(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_delete_user_not_allowed(self):
		"""Test normal USER trying to delete"""
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:users-rud", [user.id])
		response = self.client.delete(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_get_own_user_successful(self):
		"""Test get self user --- successfully"""
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:self-user-rud")
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_own_user_successful(self):
		"""Test update own user"""
		data = {
			"email": "test@test.com"
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:self-user-rud")
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_own_user_unsuccessful(self):
		"""Test USER trying to change own permission"""
		data = {
			"email": "test@test.com",
			"permission": "MANAGER"
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:self-user-rud")
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_patch_own_user_successful(self):
		"""Test patch own user"""
		data = {
			"email": "test@test.com"
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:self-user-rud")
		response = self.client.patch(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_patch_own_user_unsuccessful(self):
		"""Test USER trying to change own permission"""
		data = {
			"permission": "MANAGER"
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:self-user-rud")
		response = self.client.patch(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_get_own_profile_unsuccessful(self):
		"""Test getting own profile"""
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:profile-ru")
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_own_profile_successful(self):
		"""Test updating own profile --- successfully"""
		data = {
			"expected_calories_per_day": 500
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:profile-ru")
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data.get('expected_calories_per_day'), 500)

	def test_update_own_profile_invalid(self):
		"""Test updating own profile --- invalid data"""
		data = {
			"expected_calories_per_day": -500
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:profile-ru")
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_patch_own_profile_successful(self):
		"""Test patching own profile --- successfully"""
		data = {
			"expected_calories_per_day": 500
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:profile-ru")
		response = self.client.patch(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data.get('expected_calories_per_day'), 500)

	def test_change_own_password_successful(self):
		"""Test changeing own password"""
		data = {
			"old_password": "123",
			"new_password1": "testcc123",
			"new_password2": "testcc123"
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:self-user-change-password")
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_change_own_password_invalid_old_password(self):
		"""Test changeing own password --- invalid old password"""
		data = {
			"old_password": "000",
			"new_password1": "testcc123",
			"new_password2": "testcc123"
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-users:self-user-change-password")
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class AuthAPITestCase(APITestCase):

	def setUp(self):
		test_setup()

	def test_login_wrong_credentials(self):
		"""Test loging in with wrong credentials"""
		data = {
			"username": "admin@test.com",
			"password": "000"
		}
		url = api_reverse("api-users:login")
		response = self.client.post(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_login_successful(self):
		"""Test loging in with right credentials"""
		data = {
			"username": "admin@test.com",
			"password": "123"
		}
		url = api_reverse("api-users:login")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_signup_anonymous_successful(self):
		"""New user signup --- successful"""
		data = {
			"email": "test@test.com",
			"password1": "testcc123",
			"password2": "testcc123"
		}
		url = api_reverse("api-users:signup")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_signup_anonymous_forbiden_to_select_permission(self):
		"""New user signup with permission selection --- not allowed"""
		data = {
			"email": "test@test.com",
			"password1": "testcc123",
			"password2": "testcc123",
			"permission": "ADMIN"
		}
		url = api_reverse("api-users:signup")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_create_user_successful(self):
		"""Create new user --- successful for admins and managers"""
		data = {
			"email": "test@test.com",
			"password1": "testcc123",
			"password2": "testcc123",
			"permission": "USER"
		}
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		url = api_reverse("api-users:signup")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		data["email"] = "other_test@test.com"
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_manager_successful(self):
		"""Create new user --- successful for admins and managers"""
		data = {
			"email": "test@test.com",
			"password1": "testcc123",
			"password2": "testcc123",
			"permission": "MANAGER"
		}
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		url = api_reverse("api-users:signup")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		data["email"] = "other_test@test.com"
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		url = api_reverse("api-users:signup")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_user_for_managers_not_allowed_to_create_admins(self):
		"""Create new user --- not allowed for manager to create admins"""
		data = {
			"email": "test@test.com",
			"password1": "testcc123",
			"password2": "testcc123",
			"permission": "ADMIN"
		}
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		url = api_reverse("api-users:signup")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_password_reset_unexisting_email(self):
		"""Test password reset with unexisting email --- unsuccessful"""
		data = {
			"email": "test@test.com"
		}
		url = api_reverse("api-users:password_reset:reset-password-request")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_password_reset_successful(self):
		"""Test password reset --- successful"""
		data = {
			"email": "admin@test.com"
		}
		url = api_reverse("api-users:password_reset:reset-password-request")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_logout(self):
		"""Test logout"""
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		url = api_reverse("api-users:logout")
		response = self.client.post(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)