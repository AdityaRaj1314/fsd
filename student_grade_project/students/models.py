from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return self.name
