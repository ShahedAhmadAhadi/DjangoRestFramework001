from re import search
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Car


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CarSerializer(serializers.Serializer):
    no_plate = serializers.IntegerField()
    model = serializers.CharField(max_length=10)
    color = serializers.CharField(max_length=12)

    def create(self, validated_data):
        return Car.create(validated_data)

    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance
