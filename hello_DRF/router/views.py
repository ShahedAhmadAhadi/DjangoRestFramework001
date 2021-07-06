from django.db.models.query import QuerySet
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
from rest_framework import viewsets

# Create your views here.


# @api_view(['GET', 'POST'])
class CreateRecords(viewsets.ModelViewSet):
    parser_classes = [JSONParser]
    serializer_class = EmpSerializer
    queryset = Employee.objects.all()


def template_view(request):
    if request.method == "GET":
        return render(request, './router/index.html')
