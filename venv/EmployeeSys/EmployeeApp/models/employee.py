from django.db import models
from django.utils.timezone import now
from datetime import date
from .company import Company
from .department import Department
from .user import User
from django.core.validators import RegexValidator
class WorkflowMixin:
    """Mixin to handle simple status transitions."""
    def can_transition(self, new_status):
        """Define valid transitions."""
        transitions = {
            'pending': ['hired', 'terminated'],
            'hired': ['terminated', 'active'],
            'terminated': [],
            'active': ['terminated']
        }
        return new_status in transitions.get(self.status, [])


class Employee(WorkflowMixin, User):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('hired', 'Hired'),
        ('active', 'Active'),
        ('terminated', 'Terminated'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True, related_name='employees')
    name = models.CharField(max_length=255, blank=False, null=False)  
    mobile_number = models.CharField(max_length=15, blank=False, null=False,validators=[RegexValidator(regex=r'^\+?\d{10,15}$', message="Enter a valid mobile number.")],)
    address = models.TextField(blank=True, null=True)
    designation = models.CharField(max_length=255)
    hired_on = models.DateField(blank=True, null=True)
    days_employed = models.PositiveIntegerField(blank=True, null=True, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    
    def save(self, *args, **kwargs):
        if self.status == 'hired' and not self.hired_on:
            self.hired_on = date.today()
        if self.status == 'hired':
            self.days_employed = (now().date() - self.hired_on).days if self.hired_on else None
        elif self.status != 'hired':
            self.days_employed = None

        super().save(*args, **kwargs)

    def transition_status(self, new_status):
        if self.can_transition(new_status):
            self.status = new_status
            self.save()
        else:
            raise ValueError(f"Invalid status transition from {self.status} to {new_status}")

    def __str__(self):
        return self.name
