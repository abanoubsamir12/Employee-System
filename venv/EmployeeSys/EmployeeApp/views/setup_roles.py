from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from EmployeeApp.models import Employee  # Replace with your model


def setup_roles_and_permissions():
    
    # Create Groups (Roles)
    admin_group, _ = Group.objects.get_or_create(name='admin')
    manager_group, _ = Group.objects.get_or_create(name='manager')
    employee_group, _ = Group.objects.get_or_create(name='employee')

    # Create Permissions
    content_type = ContentType.objects.get_for_model(Employee)

    edit_permission, _ = Permission.objects.get_or_create(
        codename='can_edit_employee',
        name='Can Edit Employee',
        content_type=content_type,
    )
    delete_permission, _ = Permission.objects.get_or_create(
        codename='can_delete_employee',
        name='Can Delete Employee',
        content_type=content_type,
    )

    # Assign Permissions to Groups
    admin_group.permissions.add(edit_permission, delete_permission)
    manager_group.permissions.add(edit_permission)



@swagger_auto_schema(
    method='post',
    operation_description="create permission",
    responses={200: 'A list of permissions and groups'}
)
@api_view(['POST'])

@permission_classes([AllowAny])
def run_setup_roles(request):
    try:
        setup_roles_and_permissions()
        return JsonResponse({"message": "Roles setup successfully!"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
