from django.db.models import fields
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'father_name', 'age']


class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'father_name']
