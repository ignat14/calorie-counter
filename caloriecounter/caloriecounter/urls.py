from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken import views

urlpatterns = [
    path('', include('accounts.urls')),
    path('', include('meals.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]



##### DOCUMENTATION ######
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="CalorieCounter API",
      default_version='v1',
      description="Test Application for counting calories",
      contact=openapi.Contact(email="ignat14@gmail.com")
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]