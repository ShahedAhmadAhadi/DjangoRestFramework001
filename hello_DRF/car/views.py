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


@csrf_exempt
def car_details(request, pk):
    try:
        car = Car.objects.get(no_plate=pk)
    except Car.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == "GET":
        serializer = CarSerializer(car)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CarSerializer(car, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors ,status=400)

    elif request.method == "DELETE":
        car.delete()
        return JsonResponse(status=204)

@csrf_exempt
def person_list(request):
    if request.method == "GET":
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def person_details(request, pk):
    try:
        person = Person.objects.get(id=pk)
    except Person.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == "GET":
        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PersonSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors ,status=400)

    elif request.method == "DELETE":
        person.delete()
        return JsonResponse(status=204)
