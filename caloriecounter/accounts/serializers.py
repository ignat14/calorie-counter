from rest_framework import serializers
from .models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profile
		fields = ['expected_calories_per_day']


class UserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer(required=False)

	class Meta:
		model = User
		fields = ['id', 'email', 'permission', 'profile', 'password']
		read_only_fields = ['id']
		extra_kwargs = {
            'password': {'write_only': True}
        }

	def create(self, validated_data):
		user = super().create(validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user


class UserUpdateSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer(required=False)

	class Meta:
		model = User
		fields = ['id', 'email', 'permission', 'profile']
		read_only_fields = ['id']
