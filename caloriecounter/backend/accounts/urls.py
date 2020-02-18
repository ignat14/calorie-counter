from django.urls import path, re_path, include
from rest_framework.authtoken import views
from .views import UsersAPIView, UsersRudView, SelfUserRudView, ProfileRudView, Logout, Signup, activate, PasswordChange

app_name = 'accounts'
urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users-list'),
	path('users/<int:pk>', UsersRudView.as_view(), name='users-rud'),
	path('users/<int:pk>/profile', ProfileRudView.as_view(), name='profile-rud'),
	path('users/self', SelfUserRudView.as_view(), name='self-user-rud'),
	path('users/self/password_change', PasswordChange.as_view(), name='self-user-change-password'),

	path('auth/login/', views.obtain_auth_token, name='api-token-auth'),
    path('auth/signup/', Signup.as_view()),
	path('auth/logout/', Logout.as_view()),
	path('auth/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
	re_path(r'auth/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
			 activate, name='activate'),
]