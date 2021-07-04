from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import check_for_language
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmpSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

@api_view(['GET', 'POST'])
def create_records(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        serializer = EmpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
    return render(request, './router/index.html')
