from django.urls import path, include, re_path
from . import documentation

urlpatterns = [
    path('api/', include('accounts.urls', namespace='api-users')),
    path('api/meals/', include('meals.urls', namespace='api-meals')),
    path('api/docs/', include(documentation))
]
