import re
from django.core.checks.messages import Error
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from .serailizers import ExampleSerializer, RequestSerializer
from rest_framework.response import Response
from .models import ExampleModel, RequestLog
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

# Create your views here.

# @csrf_exempt


def fileWriting(name, encoding, data, path=""):
    try:
        with open(f'{path}{name}.txt', 'w', encoding=encoding) as file:
            file.write(f"data : {data.data}\n")
            file.write(f"user : {data.user}\n")
            file.write(f"query_parmas : {data.query_params}\n")
            file.write(f"parsers : {data.parsers}\n")
            file.write(f"accepted_renderer : {data.accepted_renderer}\n")
            file.write(f"accepted_media_type : {data.accepted_media_type}\n")
            file.write(f"auth : {data.auth}\n")
            file.write(f"authenticators : {data.authenticators}\n")
            file.write(f"method : {data.method}\n")
            file.write(f"content_type : {data.content_type}\n")
            file.write(f"stream : {data.stream}\n")
            file.write(f"META : {data.META}\n")
    finally:
        file.close()
        print(data)
        return data


def file_writing_for_api_view(name, encoding, data, path=""):
    try:
        with open(f'{path}{name}.txt', 'w', encoding=encoding) as file:
            file.write(f"renderer_classes : {data.renderer_classes}\n")
            file.write(f"parser_classes : {data.parser_classes}\n")
            file.write(f"authentication_classes : {data.authentication_classes}\n")
            file.write(f"throttle_classes : {data.throttle_classes}\n")
            file.write(f"permission_classes : {data.permission_classes}\n")
            file.write(f"content_negotiation_class : {data.content_negotiation_class}\n")
    finally:
        file.close()
        print(data)
        return data


# @api_view(['GET', 'POST'])
# def example(request):

#     if request.method == 'GET':
#         request = fileWriting('GETRequestFile', 'utf-8', request)
#         example = ExampleModel.objects.all()
#         serializer = ExampleSerializer(example, many=True)
#         return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

#     if request.method == 'POST':
#         req = fileWriting('POSTRequestFile', 'utf-8', request)
#         # data = JSONParser().parse(request)
#         serializer = ExampleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response('req')

class Example(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

    def post(self, request, format=None):
        pass


def log(request):
    pass
