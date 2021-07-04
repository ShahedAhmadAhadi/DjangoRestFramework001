from django.db.models import fields
from rest_framework import serializers
from .models import Employee


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'gender', 'email', 'phone']
