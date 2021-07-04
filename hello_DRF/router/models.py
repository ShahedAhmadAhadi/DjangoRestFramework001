from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=7)
    email = models.EmailField()
    phone = models.IntegerField()
