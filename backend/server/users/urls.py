from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('register/', api.register, name='register'),
    path('me/', api.me, name='me'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('logout/', api.logout,name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]