from .views import create_records
from django.conf import settings
from django.urls import path

app_name = 'router'

urlpatterns = [
    path('router/', create_records)
]
