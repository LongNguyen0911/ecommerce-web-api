from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.utils import timezone


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.CharField(max_length=200)
    product_name = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    category = serializers.CharField(max_length=200)
    approval = serializers.BooleanField(default=False)
    #image = serializers.ImageField(null=True, blank=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.owner = validated_data.get('owner', instance.owner)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.approval = validated_data.get('approval', instance.approval)
        
        instance.save()
        return instance