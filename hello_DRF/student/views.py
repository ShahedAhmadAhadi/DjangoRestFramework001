from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


@api_view
def student_list(request):
    pass
