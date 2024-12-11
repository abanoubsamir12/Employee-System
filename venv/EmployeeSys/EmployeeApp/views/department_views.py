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
    data = [{"id" : department.id , "name" : department.name} for department in departments]
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

@swagger_auto_schema(
    method='patch',
    operation_description="Update a department (partial update)",
    responses={200: 'Department updated successfully', 400: 'Bad Request'}
)
@api_view(['PATCH'])
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    try:
        data = JSONParser().parse(request)  # Parse incoming JSON payload
        if 'name' in data:
            department.name = data['name']
        department.save()
        updated_data = {"id": department.id, "name": department.name}
        return JsonResponse(updated_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@swagger_auto_schema(
    method='delete',
    operation_description="Delete a department",
    responses={204: 'Department deleted successfully'}
)
@api_view(['DELETE'])
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return HttpResponse(status=204)