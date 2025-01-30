from django.contrib import admin

from .models import Service, Category, ServicePhoto

admin.site.register(Service)
admin.site.register(ServicePhoto)
admin.site.register(Category)
