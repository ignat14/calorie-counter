from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework.authtoken.models import Token

from .models import Meal
from accounts.models import User


class BlogPostAPITestCase(APITestCase):

	def setUp(self):
		user = User(email="test@test.com")
		user.set_password("123")
		user.save()
		meal = Meal.objects.create(
			user=user,
			description="Bananas",
			date="2020-01-01",
			time="12:00:00",
			calories=120
		)
		token = Token.objects.create(key="12345", user=user)
	
	def test_single_user(self):
		user_count = User.objects.count()
		self.assertEqual(user_count, 1)

	def test_single_meal(self):
		meal_count = Meal.objects.count()
		self.assertEqual(meal_count, 1)

	def test_get_meals(self):
		# test the get list
		data = {}
		user = User.objects.first()
		token = Token.objects.get(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
		url = api_reverse("api-meals:my-meals-listcreate")
		response = self.client.get(url, data, format='json')
		print("---", response.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)