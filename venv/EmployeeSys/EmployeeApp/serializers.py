from rest_framework import serializers
from .models import Employee
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()  # Field name matches model field
    role = serializers.CharField() 
    extra_kwargs = {'password': {'write_only': True}} 
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_status(self, value):
        """Custom validation for status transitions."""
        if self.instance and not self.instance.can_transition(value):
            raise serializers.ValidationError(f"Invalid status transition from {self.instance.status} to {value}")
        return value



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        
        token['role'] = user.role
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        return data
