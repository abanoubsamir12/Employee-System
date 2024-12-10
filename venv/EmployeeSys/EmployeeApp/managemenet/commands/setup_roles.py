from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
class Command(BaseCommand):
    help = 'Create user roles and assign permissions'
    print(help)
    def handle(self, *args, **kwargs):
        # Create roles
        admin_group, created = Group.objects.get_or_create(name='Admin')
        manager_group, created = Group.objects.get_or_create(name='Manager')
        employee_group, created = Group.objects.get_or_create(name='Employee')
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
        manager_group.permissions.add(edit_users_permission)
        # Add permissions to emp
        employee_group.permissions.add(view_users_permission)
        print("11111111111111111")  
        self.stdout.write(self.style.SUCCESS('Roles and permissions have been set up successfully!'))