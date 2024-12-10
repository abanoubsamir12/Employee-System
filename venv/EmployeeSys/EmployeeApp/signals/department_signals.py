from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models import Company, Department, Employee

@receiver(post_save, sender=Employee)
@receiver(post_delete, sender=Employee)
def update_department_employee_count(sender, instance, **kwargs):
    department = instance.department
    department.num_employees = department.employees.count()
    department.save()
