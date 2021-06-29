from django.core.checks.messages import Error
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from .serailizers import ExampleSerializer, RequestSerializer
from rest_framework.response import Response
from .models import ExampleModel, RequestLog
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.

# @csrf_exempt
@api_view(['GET', 'POST'])
def example(request):
    try:
        print(request)
        # with open('text.txt', 'w') as file:
        #     for i in req:
        #         file.write(i)
    finally:
        # file.close()
        pass

    if request.method == 'GET':
        example = ExampleModel.objects.all()
        serializer = ExampleSerializer(example, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExampleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def log(request):
    pass
