from accounts.models import User
from meals.models import Meal
from rest_framework.authtoken.models import Token

def test_setup():
	user1 = User(email="admin@test.com", permission="ADMIN")
	user1.set_password("123")
	user1.save()
	user2 = User(email="manager@test.com", permission="MANAGER")
	user2.set_password("123")
	user2.save()
	user3 = User(email="user@test.com", permission="USER")
	user3.set_password("123")
	user3.save()
	meal1 = Meal.objects.create(
		user=user1,
		description="Banana",
		date="2020-01-01",
		time="12:00:00",
		calories=120
	)
	meal2 = Meal.objects.create(
		user=user2,
		description="Pasta",
		date="2020-03-05",
		time="18:20:00",
		calories=400
	)
	meal3 = Meal.objects.create(
		user=user3,
		description="Cake",
		date="2020-10-10",
		time="22:50:00",
		calories=380
	)
	token1 = Token.objects.create(key="12345", user=user1)
	token2 = Token.objects.create(key="56789", user=user2)
	token3 = Token.objects.create(key="010101", user=user3)