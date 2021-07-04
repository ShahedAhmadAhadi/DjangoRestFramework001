from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import check_for_language
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmpSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

@api_view(['GET', 'POST'])
def create_records(request):
    print(request.headers)
    if request.method == "POST":
        print(request.data)
        serializer = EmpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(request.data)

    if request.method == "GET":
        return render(request, './router/index.html')
