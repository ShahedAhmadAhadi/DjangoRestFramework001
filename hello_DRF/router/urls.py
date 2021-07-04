from django.urls import path

app_name = 'router'

urlpatterns = [
    # path('', initial, name="initial"),
    # path('add/', add_student, name="add"),
]
from django.conf import settings
from .views import create_records

urlpatterns = [
    path('router/', create_records)
]
