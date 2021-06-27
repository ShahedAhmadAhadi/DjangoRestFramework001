from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from .models import Person, Car
from rest_framework import permissions
from .serializers import CarSerializer, PersonSerializer, UserSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response

# Create your views here.


class CarList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



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
        return JsonResponse(serializer.errors, status=400)

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
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        person.delete()
        return JsonResponse(status=204)


class UserList(generics.ListAPIView):
    user = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    user = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'car': reverse('car-list', request=request, format=format)
    })


class CarHighlight(generics.GenericAPIView):
    queryset= Car.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        car = self.get_object()
        return Response(car.highlighted)
