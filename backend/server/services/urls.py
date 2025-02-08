from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('', api.service_list, name='service_list'),
    path('profile/<uuid:id>', api.service_list_profile, name='service_list_profile'),
    path('add-service', api.add_service, name='add_service'),
    path('edit-service/<uuid:pk>/', api.edit_service, name='edit_service'),
    path('delete-service/<uuid:pk>/', api.delete_service, name='delete_service'),
    path('<uuid:pk>/', api.service_detail, name='service_detail'),
    path('categories', api.categories_list, name='categories_list')
]
