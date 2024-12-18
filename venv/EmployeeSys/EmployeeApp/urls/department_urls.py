from django.urls import path
from EmployeeApp.views.department_views import (
    department_list,
    department_detail,
    department_update,
    department_delete
)


urlpatterns = [
    path('', department_list, name='department_list'),
    path('<int:pk>/', department_detail, name='department_detail'),
    path('<int:pk>/update/', department_update, name='department_update'),
    path('<int:pk>/delete/', department_delete, name='department_delete'),
]