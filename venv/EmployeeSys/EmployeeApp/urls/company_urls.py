from django.urls import path
from EmployeeApp.views.company_views import (
    company_list,
    company_detail,
    company_update,
    company_delete
)


urlpatterns = [
    path('', company_list, name='company_list'),
    path('<int:pk>/', company_detail, name='company_detail'),
    path('<int:pk>/update/', company_update, name='company_update'),
    path('<int:pk>/delete/', company_delete, name='company_delete'),
]