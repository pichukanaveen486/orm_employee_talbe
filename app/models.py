from django.db import models

# Create your models here.
class Employee(models.Model):
    EID=models.IntegerField()
    name=models.CharField(max_length=100)
    SAL=models.IntegerField()
    JOB=models.CharField(max_length=100)
    DOB=models.DateField()


    def __str__(self):
        return self.name