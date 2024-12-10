from django.urls import path
from EmployeeApp.views.setup_roles import (
    run_setup_roles
)

urlpatterns = [
    path('', run_setup_roles, name='run_setup_roles'),  
]
