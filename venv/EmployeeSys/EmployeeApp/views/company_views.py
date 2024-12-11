from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from EmployeeApp.models.company import Company
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


@swagger_auto_schema(
    method='get',
    operation_description="Retrieve all companies",
    responses={200: 'A list of employees'}
)
@api_view(['GET'])
def company_list(request):
    companies = Company.objects.all()
    data = [{"id": company.id, "name": company.name} for company in companies]
    return JsonResponse(data, safe=False)
    
    
    
@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a company and take primary key as an input",
    responses={200: 'A company with specific id'}
)
@api_view(['GET'])
def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    data = {"id" : company.id , "name" : company.name}
    return JsonResponse(data,safe = False)


@swagger_auto_schema(
    method='patch',
    operation_description="Update a company (partial update)",
    responses={200: 'Company updated successfully', 400: 'Bad Request'}
)

@api_view(['PATCH'])
def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    try:
        data = JSONParser().parse(request)  # Parse incoming JSON payload
        if 'name' in data:
            company.name = data['name']
        company.save()
        updated_data = {"id": company.id, "name": company.name}
        return JsonResponse(updated_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@swagger_auto_schema(
    method='delete',
    operation_description="Delete a company",
    responses={204: 'Company deleted successfully'}
)
@api_view(['DELETE'])
def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    return HttpResponse(status=204)
