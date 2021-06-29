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

def fileWriting(name, encoding, data, path = ""):
    try:
        with open(f'{path}{name}.txt', 'w', encoding=encoding) as file:
            file.write(f"data : {data.data}")
            file.write(f"user : {data.user}")
            file.write(f"query_parmas : {data.query_params}")
            file.write(f"parsers : {data.parsers}")
            file.write(f"accepted_renderer : {data.accepted_renderer}")
            file.write(f"accepted_media_type : {data.accepted_media_type}")
            file.write(f"auth : {data.auth}")
            file.write(f"authenticators : {data.authenticators}")
            file.write(f"method : {data.method}")
            file.write(f"content_type : {data.content_type}")
            file.write(f"stream : {data.stream}")
            file.write(f"META : {data.META}")
    finally:
        file.close()


@api_view(['GET', 'POST'])
def example(request):

    if request.method == 'GET':
        fileWriting('GETRequestFile', 'utf-8', request)
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
