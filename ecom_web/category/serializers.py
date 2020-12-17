from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.utils import timezone


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_id = serializers.IntegerField()
    category_name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Categorie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.category_id = validated_data.get('cat_id', instance.category_id)
        instance.category_name = validated_data.get('cat_name', instance.category_name)
        instance.description = validated_data.get('description', instance.description)
        
        instance.save()
        return instance