from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    semester = models.IntegerField()
    fee_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.usn})"
