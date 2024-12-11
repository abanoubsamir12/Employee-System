from django.contrib import admin

from .EmployeeApp.models import Role, Permission

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('permissions',)  # Add a user-friendly widget for ManyToManyField