from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserUpdateSerializer, ProfileSerializer
from .models import User, Profile
from accounts.permissions import IsAdmin, IsAdminOrManager

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