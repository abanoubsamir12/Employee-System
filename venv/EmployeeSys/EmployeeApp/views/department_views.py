from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from EmployeeApp.models.department import Department
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve all departments",
    responses={200: 'A list of departments'}
)

@api_view(['GET'])
def department_list(request):
    departments = Department.objects.all()
    data = [{"id" : department.id , "name" : departmen.name} for department in departments]
    return JsonResponse(data,safe=False)


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a department by taking primary key as an input",
    responses={200: 'a department with specific id'}
)

@api_view(['GET'])
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    data = {"id" : department.id , "name" : department.name}
    return JsonResponse(data,safe = False)