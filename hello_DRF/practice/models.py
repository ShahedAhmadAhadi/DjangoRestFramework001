from django.db import models
from django.contrib.auth.models import User

# Create your models here.

LANGUAGES_AVAILABLE = ['English', 'Espanish', 'Arabic', 'French', 'Persian']

class ExampleModel(models.Model):
    name = models.CharField(max_length=20)
    language = models.CharField(choices=LANGUAGES_AVAILABLE, max_length=50)


class RequestLog(models.Model):
    request_by = models.ForeignKey(User, on_delete=models.CASCADE)
    request_for = models.ForeignKey(ExampleModel, on_delete=models.CASCADE)
    request_log = models.TextField()

