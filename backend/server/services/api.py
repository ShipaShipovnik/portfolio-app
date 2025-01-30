from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Service
from .serializers import ServiceSerializer


@api_view(['GET'])
def service_list(request):
    services = Service.objects.all()

    serializer = ServiceSerializer(services, many=True)

    return JsonResponse({'data': serializer.data})


@api_view(['POST'])
def service_create(request):
    form = ServiceForm(request.data)

    if form.is_valid():
        service = form.save(commit=False)
        service.created_by = request.user
        service.save()
