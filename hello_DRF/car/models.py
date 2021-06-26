from django.db import models

# Create your models here.


class Car(models.Model):
    no_plate = models.IntegerField(primary_key=True, blank=False)
    model = models.CharField(max_length=10)
    color = models.CharField(max_length=12)
    owner = models.ForeignKey(
        'auth.user', related_name='car', on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=30)
    DOB = models.DateField()
    job = models.CharField(max_length=18)


class Owner(models.Model):
    owner = models.ForeignKey(
        'auth.user', related_name='cars', on_delete=models.CASCADE)
    highlighted = models.TextField()
