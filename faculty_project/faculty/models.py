from django.db import models

class FacultyMember(models.Model):
    emp_id = models.CharField(max_length=20, unique=True, verbose_name="ID")
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} {self.name} - {self.branch}"
