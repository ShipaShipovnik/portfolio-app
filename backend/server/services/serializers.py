from rest_framework import serializers

from users.models import User
from users.serializers import UserSerializer

from .models import Service, Category

from rest_framework import serializers
from .models import Service

from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Service
        fields = ['id', 'title', 'descr', 'price', 'isActive', 'category', 'created_by', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
