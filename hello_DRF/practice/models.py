from django.db import models
from django.db.models.query_utils import select_related_descend

# Create your models here.

LANGUAGES_AVAILABLE = ['English', 'Espanish', 'Arabic', 'French', 'Persian']

class ExampleModel(models.Model):
    name = models.CharField(max_length=20)
    language = models.CharField(choices=LANGUAGES_AVAILABLE, max_length=50)
