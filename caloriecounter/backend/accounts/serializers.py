from django.contrib.auth.password_validation import validate_password, get_password_validators
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import serializers
from caloriecounter import settings as cc_settings
from .tokens import account_activation_token
from .models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profile
		fields = ['user_id', 'expected_calories_per_day']
	
	def validate_expected_calories_per_day(self, value):
		if value < 0:
			raise serializers.ValidationError("Negative calories are not allowed")
		return value

class UserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer(required=False)

	class Meta:
		model = User
		fields = ['id', 'email', 'permission', 'profile', 'password', 'is_active']
		read_only_fields = ['id', 'is_active']
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
		extra_kwargs = {
            'permission': {'required': False}
        }

	def validate_permission(self, new_permission):
		self_user = self.context.get('request').user
		own_permission = self_user.permission
		old_permission = self.instance.permission
		if self_user == self.instance and old_permission != new_permission:
			raise serializers.ValidationError(f"Can't change own permission")
		if own_permission != 'ADMIN' and old_permission != 'ADMIN' and new_permission == 'ADMIN':
			raise serializers.ValidationError(f"{own_permission}S don't have permission to upgrade to ADMIN")
		if own_permission != 'ADMIN' and old_permission == 'ADMIN' and new_permission != 'ADMIN':
			raise serializers.ValidationError(f"{own_permission}S don't have permission to downgrade from ADMIN")
		return new_permission

class PasswordChangeSerializer(serializers.Serializer):
	old_password = serializers.CharField(required=True)
	new_password1 = serializers.CharField(required=True)
	new_password2 = serializers.CharField(required=True)

	class Meta:
		fields = ['old_password', 'new_password1', 'new_password2']


class SignupUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['email', 'permission']
		extra_kwargs = {
            'permission': {'required': False}
        }


	def validate_permission(self, new_permission):
		if self.context.get('request').user.is_anonymous:
			raise serializers.ValidationError(f"Not authorized users can't select permission")
		own_permission = self.context.get('request').user.permission
		if own_permission != 'ADMIN' and new_permission == 'ADMIN':
			raise serializers.ValidationError(f"{own_permission}S don't have permission to create ADMIN users")
		return new_permission

	def validate(self, data):
		if not self.context.get('password1'):
			raise serializers.ValidationError({"password1": "Password is required."})
		if not self.context.get('password2'):
			raise serializers.ValidationError({"password2": "Password Confirmation is required."})
		if self.context.get('password1') != self.context.get('password2'):
			raise serializers.ValidationError({"password2": "The password did not match."})
		try:
			validate_password(
				self.context.get('password1'),
				password_validators=get_password_validators(settings.AUTH_PASSWORD_VALIDATORS),
				user=None
			)
		except ValidationError as e:
			raise serializers.ValidationError({
				'password1': e.messages
			})
		return data
		


	def create(self, validated_data):
		permission = 'USER'
		if 'permission' in validated_data:
			permission = validated_data['permission']
		user = User(
			email=validated_data['email'],
			permission=permission,
			is_active=False
		)

		user.set_password(self.context.get('password2'))
		user.save()

		mail_subject = "Please Activate your account"
		message = render_to_string('activate_email.html', {
			'user': user,
			'domain': f"{cc_settings.SITE_DOMAIN}:{cc_settings.SITE_PORT}",
			'uid':urlsafe_base64_encode(force_bytes(user.pk)),
			'token':account_activation_token.make_token(user),
		})
		to_email = validated_data['email']

		email = EmailMessage(mail_subject, message, to=[to_email])
		email.send()

		return user
