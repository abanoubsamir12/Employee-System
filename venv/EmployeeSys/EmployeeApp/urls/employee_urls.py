from django.urls import path
from EmployeeApp.views.employee_views import (
    employee_list,
    employee_create,
    employee_detail,
    employee_update,
    employee_delete,
)

urlpatterns = [
    path('', employee_list, name='employee_list'),  # List all employees (no "employees/")
    path('create/', employee_create, name='employee_create'),  # Create a new employee
    path('<int:id>/', employee_detail, name='employee_detail'),  # Retrieve a single employee
    path('<int:id>/update/', employee_update, name='employee_update'),  # Update an employee
    path('<int:id>/delete/', employee_delete, name='employee_delete'),  # Delete an employee
]
