from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .form import RegisterForm


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
    else:
        message = 'error'
        print(f"Form errors: {form.errors}")  # Логируем ошибки формы

    return JsonResponse({'message': message})


@api_view(['POST'])
@permission_classes([AllowAny])  # Разрешаем доступ без аутентификации
def logout(request):
    if request.method == 'POST':
        # Инвалидация токена (если нужно)
        # Например, удаление токена из базы данных
        return Response({"message": "Logged out successfully"})
