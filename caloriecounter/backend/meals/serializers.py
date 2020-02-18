from rest_framework import serializers
from .models import Meal


class MyMealsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Meal
		fields = '__all__'
		read_only_fields = ['id', 'user']

class AllMealsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Meal
		fields = '__all__'
		read_only_fields = ['id']
