from rest_framework import serializers

from users.models import User
from users.serializers import UserSerializer

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Service
        fields = ['id', 'title', 'descr', 'price','category','created_by', 'created_at_formatted',]


