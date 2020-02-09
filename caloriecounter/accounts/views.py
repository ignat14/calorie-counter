from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import UserSerializer, UserUpdateSerializer
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

