from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework.parsers import JSONParser
from EmployeeApp.models.employee import Employee
from django.contrib.auth.decorators import permission_required
from ..serializers import EmployeeSerializer
import json
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


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
    operation_description="create student and add to database",
    responses={200: 'student created'}
)

@api_view(['POST'])
@permission_required('EmployeeApp.can_add_user', raise_exception=True)
def employee_create(request):
    data = JSONParser().parse(request)
    serializer = EmployeeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)




@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a student with specific id",
    responses={200: 'retrieve the student'}
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
@permission_required('EmployeeApp.can_edit_user', raise_exception=True)
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
    operation_description="delete a student",
    responses={200: 'student deleted'}
)

@api_view(['DELETE'])
@permission_required('EmployeeApp.can_delete_user', raise_exception=True)
def employee_delete(request,id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)
    employee.delete()
    return JsonResponse({"message": "Employee deleted successfully"}, status=204)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You have accessed a protected API!"})