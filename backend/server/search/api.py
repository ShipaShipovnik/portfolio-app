from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer

from services.models import Service
from services.serializers import ServiceSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def search(request):
    data = request.data
    query = data['query']

    users = User.objects.filter(name__icontains=query)
    users_serializer = UserSerializer(users, many=True)

    services = Service.objects.filter(title__icontains=query)
    services_serializer = ServiceSerializer(services, many=True)

    print('query',query)
    return JsonResponse({
        'services': services_serializer.data,
        'users': users_serializer.data
    }, safe=False)

