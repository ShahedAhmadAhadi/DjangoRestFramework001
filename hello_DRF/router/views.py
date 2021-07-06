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
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def create_records(request):
    if request.method == "GET":
        return Response({'result': 'only-post'}, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = EmpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'a':'a'}, status=status.HTTP_201_CREATED)


def template_view(request):
    if request.method == "GET":
        return render(request, './router/index.html')
