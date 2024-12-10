from EmployeeApp.views.security_views import CustomTokenObtainPairView
from django.urls import path
urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
