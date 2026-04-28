from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} - {self.grade}"
