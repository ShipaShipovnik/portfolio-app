from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .forms import ServiceForm
from .models import Service, Category
from .serializers import ServiceSerializer, CategorySerializer


@api_view(['GET'])
def service_list(request):
    services = Service.objects.all()

    serializer = ServiceSerializer(services, many=True)

    return JsonResponse({'data': serializer.data})


@api_view(['POST'])
def add_service(request):
    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            service = serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def categories_list(request):
    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    return JsonResponse({'data': serializer.data})
