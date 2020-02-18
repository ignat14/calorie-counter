from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.password_validation import validate_password, get_password_validators
from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework import generics, mixins, status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserUpdateSerializer, ProfileSerializer, SignupUserSerializer, PasswordChangeSerializer
from .models import User, Profile
from accounts.permissions import IsAdminOrManager
from caloriecounter import settings as cc_settings

from django.views.decorators.csrf import csrf_exempt

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from rest_framework import serializers


class UsersAPIView(generics.ListAPIView):
	"""
	API view that lists all the users.
	Only available for admins and managers.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAdminOrManager]


class UsersRudView(generics.RetrieveUpdateDestroyAPIView):
	"""
	API view for retrieving, updateing and deleting Users.
	Only available for admins and managers.
	"""
	lookup_field = 'pk'
	queryset = User.objects.all()
	serializer_class = UserUpdateSerializer
	permission_classes = [IsAdminOrManager]


class SelfUserRudView(generics.RetrieveUpdateDestroyAPIView):
	"""
	API view for retrieving, updating and deleting own user information.
	Right now can only change email.
	Own Permission is not allowed to be changed.
	"""
	serializer_class = UserUpdateSerializer

	def get_object(self):
		return self.request.user
		
	def get_queryset(self):
		return User.objects.get(user=self.request.user)


class ProfileRudView(generics.RetrieveUpdateAPIView):
	"""API view for retrieving, updating and deleting profile information."""
	serializer_class = ProfileSerializer

	def get_object(self):
		return Profile.objects.get(user_id=self.kwargs.get('pk'))
	

class Logout(APIView):
	"""Deleting the token to force a logout."""
	def post(self, request, format=None):
		request.user.auth_token.delete()
		return Response(status=status.HTTP_200_OK)


class Signup(generics.CreateAPIView):
	"""
	API view that overrides the create method for users.
	After creating a new user, verification email is sent.
	"""
	queryset = User.objects.all()
	serializer_class = SignupUserSerializer
	permission_classes = [AllowAny]

	def get_serializer_context(self, *args, **kwargs):
		return {
			"request": self.request,
			"password1": self.request.data.get('password1'),
			"password2": self.request.data.get('password2')
			}


class PasswordChange(generics.UpdateAPIView):
	"""
	API view that overrides the update method so
	users can change their own passwords
	"""
	serializer_class = PasswordChangeSerializer

	def get_object(self):
		return self.request.user
		
	def get_queryset(self):
		return User.objects.get(user=self.request.user)

	def update(self, request):
		old_password = request.data['old_password']
		new_password1 = request.data['new_password1']
		new_password2 = request.data['new_password2']

		if not request.user.check_password(old_password):
			raise serializers.ValidationError({"old_password": ["The old password is incorect."]})
		if new_password1 != new_password2:
			raise serializers.ValidationError({"new_password2": ["The passwords did not match."]})
		try:
			validate_password(
				new_password1,
				user=request.user,
				password_validators=get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
			)
		except ValidationError as e:
			raise exceptions.ValidationError({
				'new_password1': e.messages
			})

		request.user.set_password(request.data['new_password1'])
		request.user.save()
		return Response({"message": "Password save successfully"}, status=status.HTTP_200_OK)


@csrf_exempt
def activate(request, uidb64, token):
	"""
	API view that expects a valid token
	(one that is received by email after signup)
	so the user can be activated
	"""
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		return redirect(f'http://{cc_settings.FRONTEND_DOMAIN}:{cc_settings.FRONTEND_PORT}/login')
	else:
		return HttpResponse('Activation link is invalid!')