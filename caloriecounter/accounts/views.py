from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserUpdateSerializer, ProfileSerializer, SignupUserSerializer
from .models import User, Profile
from accounts.permissions import IsAdmin, IsAdminOrManager

from django.views.decorators.csrf import csrf_exempt

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from rest_framework import serializers


class UsersAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAdminOrManager]

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class UsersRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	queryset = User.objects.all()
	serializer_class = UserUpdateSerializer
	permission_classes = [IsAdminOrManager]


class SelfUserRudView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = UserUpdateSerializer

	def get_object(self):
		return self.request.user
		
	def get_queryset(self):
		return User.objects.get(user=self.request.user)


class ProfileRudView(generics.RetrieveUpdateAPIView):
	serializer_class = ProfileSerializer

	def get_object(self):
		return Profile.objects.get(user_id=self.kwargs.get('pk'))
	

class Logout(APIView):
    def post(self, request, format=None):
        # delete the token to force a logout
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



@csrf_exempt
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('http://0.0.0.0:8080/login')
    else:
        return HttpResponse('Activation link is invalid!')

class Signup(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = SignupUserSerializer
	permission_classes = [AllowAny]

	def get_serializer_context(self, *args, **kwargs):
		if 'password1' not in self.request.data:
			raise serializers.ValidationError("Password 1 is required")
		if 'password2' not in self.request.data:
			raise serializers.ValidationError("Password 2 is required")
		if self.request.data['password1'] != self.request.data['password2']:
			raise serializers.ValidationError({"non_field": "The passwords did not match"})
		return {
			"request": self.request,
			"password": self.request.data['password1']
			}
