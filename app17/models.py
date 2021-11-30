from django.db import models

class Employee(models.Model):
    idno= models.IntegerField(unique=True)
    name= models.CharField(max_length=100)
    salary= models.FloatField()