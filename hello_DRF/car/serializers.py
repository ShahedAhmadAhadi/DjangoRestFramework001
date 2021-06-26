from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Car, Person


class CarSerializer(serializers.Serializer):
    no_plate = serializers.IntegerField(read_only=True)
    model = serializers.CharField(max_length=10)
    color = serializers.CharField(max_length=12)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.no_plate = validated_data.get('no_plate', instance.no_plate)
        instance.model = validated_data.get('model', instance.model)
        instance.color = validated_data.get('color', instance.color)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'DOB', 'job']


class UserSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Car.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'car']
