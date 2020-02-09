from django.urls import path
from .views import MyMealsAPIView, MyMealsRudView, AllMealsAPIView, AllMealsRudView

urlpatterns = [
    path('api/my_meals', MyMealsAPIView.as_view(), name='my-meals-listcreate'),
	path('api/my_meals/<int:pk>', MyMealsRudView.as_view(), name='my-meals-rud'),

	path('api/all_meals', AllMealsAPIView.as_view(), name='all-meals-listcreate'),
	path('api/all_meals/<int:pk>', AllMealsRudView.as_view(), name='all-meals-rud')
]