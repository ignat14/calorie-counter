from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import MyMealsSerializer, AllMealsSerializer
from .models import Meal
from accounts.permissions import IsAdmin, IsAdminOrManager
from .utils import filter_datetime

import datetime


class MyMealsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = MyMealsSerializer

	def get_queryset(self):
		qs = Meal.objects.filter(user=self.request.user)
		params = self.request.GET
		qs = filter_datetime(params, qs)
		return qs

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class MyMealsRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = MyMealsSerializer

	def get_queryset(self):
		return Meal.objects.filter(user=self.request.user)





class AllMealsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = AllMealsSerializer
	permission_classes = [IsAdmin]

	def get_queryset(self):
		qs = Meal.objects.all()
		params = self.request.GET
		qs = filter_datetime(params, qs)
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class AllMealsRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	queryset = Meal.objects.all()
	serializer_class = AllMealsSerializer
	permission_classes = [IsAdmin]
