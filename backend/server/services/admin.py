from django.contrib import admin

from .models import Service, Category, ServiceAttachment

admin.site.register(Service)
admin.site.register(ServiceAttachment)
admin.site.register(Category)
