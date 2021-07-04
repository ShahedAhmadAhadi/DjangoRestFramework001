from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import check_for_language
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmpSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Create your views here.


@api_view(['GET', 'POST'])
def create_records(request):
    print(request.__dict__)
    print(request._full_data)
    if request.method == "POST":
        print(request.data)
        serializer = EmpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)

    if request.method == "GET":
        return render(request, './router/index.html')
