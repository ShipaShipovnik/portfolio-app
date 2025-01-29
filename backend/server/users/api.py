from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

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
