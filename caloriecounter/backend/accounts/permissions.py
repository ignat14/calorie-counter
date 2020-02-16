from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
	message = 'This action is only allowed for ADMIN users'

	def has_permission(self, request, view):
		if request.user.is_anonymous:
			return False
		else:
			return request.user.permission == 'ADMIN'


class IsAdminOrManager(permissions.BasePermission):
	message = 'This action is only allowed for ADMIN and MANAGER users'

	def has_permission(self, request, view):
		if request.user.is_anonymous:
			return False
		else:
			return request.user.permission == 'MANAGER' or request.user.permission == 'ADMIN'
