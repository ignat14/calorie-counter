from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework.authtoken.models import Token

from .models import Meal
from accounts.models import User
from caloriecounter.utils import test_setup


class MyMealsAPITestCase(APITestCase):

	def setUp(self):
		test_setup()
	

	# My Meals Tests

	def test_get_my_meals(self):
		"""Test getting own meals"""
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-meals:my-meals-listcreate")
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)
		self.assertEqual(response.data[0].get('description'), 'Cake')
	
	def test_get_my_meals_unauthorized(self):
		"""Test getting own meals --- unauthorized"""
		data = {}
		url = api_reverse("api-meals:my-meals-listcreate")
		response = self.client.get(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_create_my_meal_successfull(self):
		"""Test creating own meal --- successfully"""
		data = {
			"description": "Burger",
			"date": "2020-02-09",
			"time": "16:00:00",
			"calories": 550
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-meals:my-meals-listcreate")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_my_meal_unauthorized(self):
		"""Test creating own meal --- unauthorized"""
		data = {
			"description": "Burger",
			"date": "2020-02-09",
			"time": "16:00:00",
			"calories": 550
		}
		url = api_reverse("api-meals:my-meals-listcreate")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_create_my_meal_invalid_date(self):
		"""Test creating own meal --- invalid date"""
		data = {
			"description": "Burger",
			"date": "01-01-2020",
			"time": "16:00:00",
			"calories": 550
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-meals:my-meals-listcreate")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertNotEqual(response.data.get('date'), None)

	def test_create_my_meal_invalid_calories(self):
		"""Test creating own meal --- invalid calories"""
		data = {
			"description": "Burger",
			"date": "2020-01-01",
			"time": "16:00:00",
			"calories": -50
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-meals:my-meals-listcreate")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertNotEqual(response.data.get('calories'), None)

	def test_retrieve_my_meal(self):
		"""Test getting one own meal"""
		data = {}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		meal = Meal.objects.get(user=user)
		url = api_reverse("api-meals:my-meals-rud", [meal.id])
		response = self.client.get(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data.get('description'), 'Cake')

	def test_update_my_meal(self):
		"""Test updating one own meal"""
		data = {
			"description": "BigBurger",
			"date": "2020-02-08",
			"time": "12:15:00",
			"calories": 520
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		meal = Meal.objects.get(user=user)
		url = api_reverse("api-meals:my-meals-rud", [meal.id])
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data.get('description'), 'BigBurger')

	def test_update_someone_elses_meal(self):
		"""Test updating someone elses meal"""
		data = {
			"description": "BigBurger",
			"date": "2020-02-08",
			"time": "12:15:00",
			"calories": 520
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		other_user = User.objects.get(email="manager@test.com")
		meal = Meal.objects.get(user=other_user)
		url = api_reverse("api-meals:my-meals-rud", [meal.id])
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_patch_my_meal(self):
		"""Test patching one own meal"""
		data = {
			"calories": 650
		}
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		meal = Meal.objects.get(user=user)
		url = api_reverse("api-meals:my-meals-rud", [meal.id])
		response = self.client.patch(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data.get('calories'), 650)

	def test_delete_my_meal(self):
		"""Test delete one own meal"""
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		meal = Meal.objects.get(user=user)
		url = api_reverse("api-meals:my-meals-rud", [meal.id])
		response = self.client.delete(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class AllMealsAPITestCase(APITestCase):

	def setUp(self):
		test_setup()
	
	def test_get_all_meals_list_unauthorized(self):
		"""Test to get all meals with list user and manager --- unauthorized"""
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-meals:all-meals-listcreate")
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		url = api_reverse("api-meals:all-meals-listcreate")
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_get_all_meals_list_successful(self):
		"""Test to get all meals list with admin --- successfully"""
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		url = api_reverse("api-meals:all-meals-listcreate")
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 3)

	def test_create_meal_unauthorized(self):
		"""Test to create meals with user and manager --- unauthorized"""
		user = User.objects.get(email="user@test.com")
		token3 = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token3}')
		url = api_reverse("api-meals:all-meals-listcreate")
		response = self.client.post(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
		manager = User.objects.get(email="manager@test.com")
		token2 = Token.objects.get(user=manager)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token2}')
		url = api_reverse("api-meals:all-meals-listcreate")
		response = self.client.post(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_create_meals_successful(self):
		"""Test to create a meal with admin --- successfully"""
		data = {
			"description": "Cerial",
			"date": "2020-12-05",
			"time": "08:00:00",
			"calories": 220,
			"user": 1
		}
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		url = api_reverse("api-meals:all-meals-listcreate")
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data.get('description'), 'Cerial')

	def test_get_meal_successful(self):
		"""Test get one specific meal"""
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		meal2 = Meal.objects.get(description="Pasta")
		url = api_reverse("api-meals:all-meals-rud", [meal2.id])
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data.get('description'), 'Pasta')

	def test_update_meal_successful(self):
		"""Test updating one specific meal"""
		data = {
			"description": "Rice",
			"date": "2020-12-05",
			"time": "08:00:00",
			"calories": 220,
			"user": 1
		}
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		meal2 = Meal.objects.get(description="Pasta")
		url = api_reverse("api-meals:all-meals-rud", [meal2.id])
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data.get('description'), 'Rice')

	def test_patch_meal_successful(self):
		"""Test patching one specific meal"""
		data = {
			"time": "23:40"
		}
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		meal2 = Meal.objects.get(description="Pasta")
		url = api_reverse("api-meals:all-meals-rud", [meal2.id])
		response = self.client.patch(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data.get('time'), '23:40:00')

	def test_delete_meal_successful(self):
		"""Test deleting one specific meal"""
		admin = User.objects.get(email="admin@test.com")
		token1 = Token.objects.get(user=admin)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token1}')
		meal2 = Meal.objects.get(description="Pasta")
		url = api_reverse("api-meals:all-meals-rud", [meal2.id])
		response = self.client.delete(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
