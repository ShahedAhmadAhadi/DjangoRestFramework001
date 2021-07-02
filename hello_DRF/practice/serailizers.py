from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import ExampleModel, RequestLog



class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ['id', 'name', 'language']


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLog
        fields = ['id', 'request_by', 'request_for', 'request_log']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
