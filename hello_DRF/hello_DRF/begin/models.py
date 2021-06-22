from django.db import models

# Create your models here.


class Car(models.Model):
    no_plate = models.IntegerField(primary_key=True, max_length=6, blank=False)
    model = models.CharField(max_length=10)
    color = models.CharField(max_length=12)

