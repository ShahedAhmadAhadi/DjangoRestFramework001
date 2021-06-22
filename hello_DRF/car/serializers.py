from re import search
from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.Serializer):
    no_plate = serializers.IntegerField()
    model = serializers.CharField(max_length=10)
    color = serializers.CharField(max_length=12)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance
