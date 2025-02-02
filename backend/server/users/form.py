from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2')


class ProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name')
