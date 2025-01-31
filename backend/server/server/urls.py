from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('users.urls')),
    path('search/', include('search.urls')),
    path('api/services/', include('services.urls')),
    path('admin/', admin.site.urls),
]
