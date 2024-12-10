from django.db import models
from .company import Company

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    num_employees = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return f"{self.name} ({self.company.name})"
