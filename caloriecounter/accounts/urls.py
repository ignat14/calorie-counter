from django.urls import path
from .views import UsersAPIView, UsersRudView, SelfUserRudView, ProfileRudView, Logout

urlpatterns = [
    path('api/users', UsersAPIView.as_view(), name='users-listcreate'),
	path('api/users/<int:pk>', UsersRudView.as_view(), name='users-rud'),
	path('api/users/<int:pk>/profile', ProfileRudView.as_view(), name='profile-rud'),
	path('api/users/self', SelfUserRudView.as_view(), name='self-user-rud'),

	path('api/logout/', Logout.as_view()),
]