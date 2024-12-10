from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models import Company, Department, Employee

@receiver(post_save, sender=Department)
@receiver(post_delete, sender=Department)
def update_num_departments(sender, instance, **kwargs):
    company = instance.company
    company.num_departments = company.departments.count()
    company.save()

@receiver(post_save, sender=Employee)
@receiver(post_delete, sender=Employee)
def update_num_employees(sender, instance, **kwargs):
    company = instance.company
    company.num_employees = company.employees.count()
    company.save()
