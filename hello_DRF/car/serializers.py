from re import search
from rest_framework import fields, serializers
from .models import Car, Person


class CarSerializer(serializers.Serializer):
    no_plate = serializers.IntegerField(read_only=True)
    model = serializers.CharField(max_length=10)
    color = serializers.CharField(max_length=12)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.no_plate = validated_data.get('no_plate', instance.no_plate)
        instance.model = validated_data.get('model', instance.model)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'DOB', 'job']

