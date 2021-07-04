from .views import create_records, template_view
from django.conf import settings
from django.urls import path

app_name = 'router'

urlpatterns = [
    path('router/', create_records),
    path('template/', template_view)
]
