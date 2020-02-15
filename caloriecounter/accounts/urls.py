from django.urls import path
from .views import UsersAPIView, UsersRudView, SelfUserRudView, ProfileRudView, Logout

urlpatterns = [
    path('api/users', UsersAPIView.as_view(), name='users-listcreate'),
	path('api/users/<int:pk>', UsersRudView.as_view(), name='users-rud'),
	path('api/users/<int:pk>/profile', ProfileRudView.as_view(), name='profile-rud'),
	path('api/users/self', SelfUserRudView.as_view(), name='self-user-rud'),

	path('api/logout/', Logout.as_view()),
]



# from django.conf.urls import url, include
# from allauth.account.views import ConfirmEmailView
# from . import views

# urlpatterns += [
#     # Override urls
#     url(r'^registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
#     url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
#     url(r'^registration/complete/$', views.complete_view, name='account_confirm_complete'),
#     url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.null_view, name='password_reset_confirm'),
#     # Default urls
#     url(r'', include('rest_auth.urls')),
#     url(r'^registration/', include('rest_auth.registration.urls'))
# ]