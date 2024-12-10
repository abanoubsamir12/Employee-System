from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    password = models.CharField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Add related_name to resolve conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Custom reverse relation name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Custom reverse relation name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    class Meta:
        permissions = [
            ("can_view_users", "Can view users"),
            ("can_add_user", "Can add user"),
            ("can_edit_user", "Can edit user"),
            ("can_delete_user", "Can delete user"),
        ]

    def __str__(self):
        return self.username
