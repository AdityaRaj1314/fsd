from django.db import models

class Alumni(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    passing_year = models.IntegerField()
    company = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.passing_year}"
