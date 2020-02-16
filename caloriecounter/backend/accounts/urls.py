from django.urls import path, re_path
from rest_framework.authtoken import views
from .views import UsersAPIView, UsersRudView, SelfUserRudView, ProfileRudView, Logout, Signup, activate

urlpatterns = [
    path('api/users', UsersAPIView.as_view(), name='users-listcreate'),
	path('api/users/<int:pk>', UsersRudView.as_view(), name='users-rud'),
	path('api/users/<int:pk>/profile', ProfileRudView.as_view(), name='profile-rud'),
	path('api/users/self', SelfUserRudView.as_view(), name='self-user-rud'),

	path('api/auth/login', views.obtain_auth_token, name='api-token-auth'),
    path('api/auth/signup', Signup.as_view()),
	path('api/auth/logout', Logout.as_view()),
	re_path(r'api/auth/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
			 activate, name='activate'),
]