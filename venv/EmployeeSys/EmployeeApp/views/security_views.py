from rest_framework_simplejwt.views import TokenObtainPairView
from EmployeeApp.serializers.auth_serializer import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
