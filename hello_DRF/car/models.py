from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.


class Car(models.Model):
    no_plate = models.IntegerField(primary_key=True, blank=False)
    model = models.CharField(max_length=10)
    color = models.CharField(max_length=12)



class Person(models.Model):
    name = models.CharField(max_length=30)
    DOB = models.DateField()
    job = models.CharField(max_length=18)


class Owner(models.Model):
    owner = models.ForeignKey('auth.user', related_name='cars', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Snippet, self).save(*args, **kwargs)
