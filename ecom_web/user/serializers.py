from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.utils import timezone


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    is_staff = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=True)
    date_joined = serializers.DateTimeField(default=timezone.now)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        
        instance.save()
        return instance