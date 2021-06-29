from django.shortcuts import render
from rest_framework import serializers
from .serailizers import ExampleSerializer, RequestSerializer
from rest_framework.response import Response
from .models import ExampleModel, RequestLog
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.


def example(request):
    try:
        file = open('text.txt', 'w')
        file.write(request)
    except:
        pass

    if request.method == 'GET':
        example = ExampleModel.objects.all()
        serializer = ExampleSerializer(example, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExampleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def log(request):
    pass
