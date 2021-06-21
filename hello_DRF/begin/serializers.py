from django.contrib.auth import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModalSerializer):
    class Meta:
        model: User
        fields: ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkModelSerializer):
    class Meta: 
        model: Group
        fields: ['url', 'name']
