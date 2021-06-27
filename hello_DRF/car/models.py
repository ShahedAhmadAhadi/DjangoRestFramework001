from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.


class Car(models.Model):
    no_plate = models.IntegerField(primary_key=True, blank=False)
    model = models.CharField(max_length=10)
    color = models.CharField(max_length=12)
    owner = models.ForeignKey(
        'auth.user', related_name='car', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.model)
        linenos = 'table' if True else False
        options = {'title': self.color} if self.color else {}
        formatter = HtmlFormatter(style='friendly', linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight('<html></html>', lexer, formatter)
        super(Car, self).save(*args, **kwargs)


class Person(models.Model):
    name = models.CharField(max_length=30)
    DOB = models.DateField()
    job = models.CharField(max_length=18)


class Owner(models.Model):
    owner = models.ForeignKey(
        'auth.user', related_name='cars', on_delete=models.CASCADE)
    highlighted = models.TextField()
