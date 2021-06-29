from django.contrib import admin
from .models import ExampleModel, RequestLog

# Register your models here.
admin.site.register(ExampleModel)
admin.site.register(RequestLog)
