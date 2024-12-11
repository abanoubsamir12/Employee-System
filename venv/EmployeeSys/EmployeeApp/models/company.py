    from django.db import models

    class Company(models.Model):
        name = models.CharField(max_length=255, unique=True)
        num_departments = models.PositiveIntegerField(default=0, editable=False)
        num_employees = models.PositiveIntegerField(default=0, editable=False)

        def __str__(self):
            return self.name
