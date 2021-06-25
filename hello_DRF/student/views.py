from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student


# Create your views here.


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == "GET":
        student = Student.objects.all()
        serializer = StudentSerializer(student, manay=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
