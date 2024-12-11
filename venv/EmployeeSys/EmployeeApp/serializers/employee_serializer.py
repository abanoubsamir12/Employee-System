from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User



from django.contrib.auth.hashers import make_password
from EmployeeApp.models.employee import Employee
from EmployeeApp.models.company import Company
from django.db import transaction
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, Permission



class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), write_only=True, required=True)  # Role for the User
    company_id = serializers.PrimaryKeyRelatedField(source='company', queryset=Company.objects.all(), required=True)
    role_name = serializers.CharField(source='user.role.name', read_only=True)  # Display role in response

    class Meta:
        model = Employee
        fields = [
            'username',
            'password',
            'group',
            'role_name',
            'company_id',
            'status',
            'name',
            'mobile_number',
            'address',
            'designation',
        ]

    def validate_username(self, value):
        """Ensure the username is unique."""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        # Extract user-related data
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        group = validated_data.pop('group')

        # Create User instance
        user = User(username=username, password=make_password(password))
        user.save()
        user.groups.add(group)        
        # Assign group permissions to the user
        user.user_permissions.set(group.permissions.all())
        user.save()
        

        # Create Employee instance linked to the User
        employee = Employee.objects.create(user=user, **validated_data)
        return employee

    @transaction.atomic
    def update(self, instance, validated_data):
        # Update User data
        if 'username' in validated_data:
            instance.user.username = validated_data.pop('username')
            instance.user.save()

        if 'password' in validated_data:
            instance.user.password = make_password(validated_data.pop('password'))
            instance.user.save()

        if 'group' in validated_data:
            instance.user.role = validated_data.pop('group')
            instance.user.save()

        # Update Employee data
        return super().update(instance, validated_data)


