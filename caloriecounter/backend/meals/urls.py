from django.urls import path
from .views import MyMealsAPIView, MyMealsRudView, AllMealsAPIView, AllMealsRudView

app_name = 'meals'
urlpatterns = [
    path('my_meals/', MyMealsAPIView.as_view(), name='my-meals-listcreate'),
	path('my_meals/<int:pk>', MyMealsRudView.as_view(), name='my-meals-rud'),

	path('', AllMealsAPIView.as_view(), name='all-meals-listcreate'),
	path('<int:pk>', AllMealsRudView.as_view(), name='all-meals-rud')
]