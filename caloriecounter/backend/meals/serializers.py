from rest_framework import serializers
from .models import Meal


class MyMealsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Meal
		fields = '__all__'
		read_only_fields = ['id', 'user']

	def validate_calories(self, value):
		if value < 0:
			raise serializers.ValidationError("Negative calories are not allowed")
		return value

class AllMealsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Meal
		fields = '__all__'
		read_only_fields = ['id']

	def validate_calories(self, value):
		if value < 0:
			raise serializers.ValidationError("Negative calories are not allowed")
		return value