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


