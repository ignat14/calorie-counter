from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import MyMealsSerializer, AllMealsSerializer
from .models import Meal
from accounts.permissions import IsAdmin, IsAdminOrManager
from .utils import filter_meals

import datetime


class MyMealsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	"""API view for creating and listing own meals"""
	serializer_class = MyMealsSerializer

	def get_queryset(self):
		qs = Meal.objects.filter(user=self.request.user)
		params = self.request.GET
		qs = filter_meals(params, qs).order_by('time')
		return qs

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class MyMealsRudView(generics.RetrieveUpdateDestroyAPIView):
	"""API view for retrieving, updating and deleing own meals"""
	lookup_field = 'pk'
	serializer_class = MyMealsSerializer

	def get_queryset(self):
		qs = Meal.objects.filter(user=self.request.user)
		return qs


class AllMealsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	"""
	API view for creating and listing all meals.
	Only available for admin users.
	"""
	serializer_class = AllMealsSerializer
	permission_classes = [IsAdmin]

	def get_queryset(self):
		qs = Meal.objects.all()
		params = self.request.GET
		qs = filter_meals(params, qs).order_by('time').order_by('date')
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class AllMealsRudView(generics.RetrieveUpdateDestroyAPIView):
	"""
	API view for retrieving, updating and deleting meals.
	Only available for admin users
	"""
	lookup_field = 'pk'
	queryset = Meal.objects.all()
	serializer_class = AllMealsSerializer
	permission_classes = [IsAdmin]
