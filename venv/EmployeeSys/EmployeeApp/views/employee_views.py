from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework.parsers import JSONParser
from EmployeeApp.models.employee import Employee
from django.contrib.auth.decorators import permission_required
from EmployeeApp.serializers.employee_serializer import EmployeeSerializer
import json
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view,permission_classes
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve all students",
    responses={200: 'A list of students'}
)

@api_view(['GET'])
@permission_required('EmployeeApp.can_view_users', raise_exception=True)
@require_http_methods(["GET"])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)




@swagger_auto_schema(
    method='post',
    request_body=EmployeeSerializer,  # Use the EmployeeSerializer for the request body schema
    responses={
        201: openapi.Response('Employee created successfully', EmployeeSerializer),
        400: openapi.Response('Validation error'),
    },
    operation_description="Create a new employee",
)

@api_view(['POST'])
@permission_classes([AllowAny])
def employee_create(request):
    data = JSONParser().parse(request)
    serializer = EmployeeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)




@swagger_auto_schema(
    method='get',
    operation_description="Retrieve an employee with specific id",
    responses={200: 'retrieve the employee'}
)

@api_view(['GET'])
def employee_detail(request,id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)
    serializer = EmployeeSerializer(employee)
    return JsonResponse(serializer.data)
    
    
@swagger_auto_schema(
    method='patch',
    operation_description="update employee data",
    responses={200: 'updated employee'}
)

@api_view(['PATCH'])
@permission_required('EmployeeApp.can_edit_employee', raise_exception=True)
def employee_update(request,id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)
    data = JSONParser().parse(request)
    serializer = EmployeeSerializer(employee, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)




@swagger_auto_schema(
    method='delete',
    operation_description="delete an employee",
    responses={200: 'employee deleted'}
)

@api_view(['DELETE'])
@permission_required('EmployeeApp.can_delete_employee', raise_exception=True)
def employee_delete(request,id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)
    employee.delete()
    return JsonResponse({"message": "Employee deleted successfully"}, status=204)

