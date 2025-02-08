from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from .forms import ServiceForm, AttachmentForm
from .models import Service, Category
from .serializers import ServiceSerializer, CategorySerializer


@api_view(["GET"])
def service_list(request):
    services = Service.objects.all()

    serializer = ServiceSerializer(services, many=True)

    return JsonResponse({"data": serializer.data})


@api_view(["GET"])
def service_list_profile(request, id):
    user = User.objects.get(pk=id)
    services = Service.objects.filter(created_by=id)

    services_serializer = ServiceSerializer(services, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse(
        {"services": services_serializer.data, "user": user_serializer.data}, safe=False
    )


@api_view(["POST"])
def add_service(request):
    # Обработка основной формы услуги
    service_form = ServiceForm(request.POST)
    attachment = None

    # Обработка вложения, если есть файл
    if request.FILES:
        attachment_form = AttachmentForm(request.POST, request.FILES)
        if attachment_form.is_valid():
            attachment = attachment_form.save(commit=False)
            attachment.created_by = request.user
            attachment.save()
        else:
            return JsonResponse({'error': attachment_form.errors}, status=400)

    if service_form.is_valid():
        service = service_form.save(commit=False)
        service.created_by = request.user
        service.save()

        if attachment:
            service.photos.add(attachment)

        serializer = ServiceSerializer(service)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': service_form.errors}, status=400)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_service(request, pk):
    try:
        service = get_object_or_404(Service, pk=pk, created_by=request.user)
        service.delete()
        return Response({'message': 'Услуга успешно удалена'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def edit_service(request, pk):
    service = get_object_or_404(Service, pk=pk, created_by=request.user)
    service_form = ServiceForm(request.POST, instance=service)
    attachment = None

    # Обработка вложения, если есть файл
    if request.FILES:
        attachment_form = AttachmentForm(request.POST, request.FILES)
        if attachment_form.is_valid():
            attachment = attachment_form.save(commit=False)
            attachment.created_by = request.user
            attachment.save()
        else:
            return JsonResponse({'error': attachment_form.errors}, status=400)

    if service_form.is_valid():
        service = service_form.save(commit=False)
        service.save()

        if attachment:
            service.photos.set([attachment])

        serializer = ServiceSerializer(service)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': service_form.errors}, status=400)


@api_view(["GET"])
@permission_classes([AllowAny])
def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    service_data = ServiceSerializer(service).data
    user_data = {
        'id': service.created_by.id,
        'username': service.created_by.name
    }
    return JsonResponse({
        'service': service_data,
        'user': user_data
    })


@api_view(["GET"])
@permission_classes([AllowAny])
def categories_list(request):
    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    return JsonResponse({"data": serializer.data})
