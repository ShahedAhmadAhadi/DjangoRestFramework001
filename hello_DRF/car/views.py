from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from .models import Person, Car
from .serializers import PersonSerializer, CarSerializer

# Create your views here.


@csrf_exempt
def car_list(request):
    if request.method == "GET":
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

