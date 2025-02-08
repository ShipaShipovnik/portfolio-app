from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import User
from users.serializers import UserSerializer

from .form import RegisterForm, ProfileForm


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register(request):
    data = request.data
    print(f"Received data: {data}")  # Логируем полученные данные
    message = 'success'

    form = RegisterForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        print("Form is valid. Saving user.")  # Логируем успешную валидацию
        form.save()
        return JsonResponse({'message': 'success'})
    else:
        print(f"Form errors: {form.errors}")  # Логируем ошибки формы
        # Преобразуем ошибки формы в список
        errors = {field: errors[0] for field, errors in form.errors.items()}
        return JsonResponse({'message': 'error', 'errors': errors}, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def logout(request):
    if request.method == 'POST':
        # Инвалидация токена (если нужно)
        # Например, удаление токена из базы данных
        return Response({"message": "Logged out successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    user = request.user
    email = request.data.get('email')

    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return Response({'message': 'Имейл уже существует'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        print(request.data)
        print(request.FILES)

        form = ProfileForm(request.data,request.FILES ,instance=user)

        if form.is_valid():
            form.save()
        return Response({'message': 'Информация обновлена'}, status=status.HTTP_200_OK)