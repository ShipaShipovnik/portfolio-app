from .models import Service, Category

from rest_framework import serializers
from .models import Service,ServiceAttachment

class ServiceAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAttachment
        fields = ('id', 'get_image',)


class ServiceSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    photos = ServiceAttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'descr', 'price', 'isActive', 'category','photos', 'created_by', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
