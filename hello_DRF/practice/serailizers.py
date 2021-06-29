from django.db.models import fields
from rest_framework import serializers
from .models import ExampleModel


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ['id', 'name', 'language']