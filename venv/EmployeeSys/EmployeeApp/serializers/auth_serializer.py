from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from EmployeeApp.models.employee import Employee
from EmployeeApp.models.company import Company
from django.db import transaction
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, Permission
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        # Check if the user exists in your custom User model
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "Invalid username or password"})

        # Verify the password using check_password
        if not check_password(password, user.password):
            raise serializers.ValidationError({"detail": "Invalid username or password"})

        # Check if the user is active
        if not user.is_active:
            raise serializers.ValidationError({"detail": "User account is inactive"})

        # Ensure compatibility with the parent class
        self.user = user
        data = super().validate(attrs)

        # Add custom information (e.g., role or groups)
        data['role'] = user.groups.first().name if user.groups.exists() else "No group assigned"
        return data
