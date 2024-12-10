from django.http import JsonResponse
from django.core.management import call_command
from django.contrib.auth.models import Group, Permission


def setup_roles_and_permissions():
    # Create roles
    admin_group, _ = Group.objects.get_or_create(name='Admin')
    manager_group, _ = Group.objects.get_or_create(name='Manager')
    employee_group, _ = Group.objects.get_or_create(name='Employee')

    try:
        # Assign permissions
        view_users_permission = Permission.objects.get(codename='can_view_users')
        add_user_permission = Permission.objects.get(codename='can_add_user')
        edit_user_permission = Permission.objects.get(codename='can_edit_user')
        delete_user_permission = Permission.objects.get(codename='can_delete_user')

        # Add permissions to admin
        admin_group.permissions.add(view_users_permission)
        admin_group.permissions.add(add_user_permission)
        admin_group.permissions.add(edit_user_permission)
        admin_group.permissions.add(delete_user_permission)

        # Add permissions to manager
        manager_group.permissions.add(view_users_permission)
        manager_group.permissions.add(edit_user_permission)

        # Add permissions to employee
        employee_group.permissions.add(view_users_permission)

        print("Roles and permissions have been set up successfully!")
    except Permission.DoesNotExist as e:
        print(f"Error: Permission does not exist: {e}")


def run_setup_roles(request):
    try:
        setup_roles_and_permissions()
        return JsonResponse({"message": "Roles setup successfully!"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
