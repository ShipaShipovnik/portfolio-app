import uuid
from email.policy import default
from tabnanny import verbose

from django.db import models
from django.utils.timesince import timesince
from rest_framework.fields import CharField

from users.models import User


# Категория =======================================================
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"


# Услуги =======================================================
class ServiceAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='service_photos')
    created_by = models.ForeignKey(User, related_name='service_photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        else:
            return ''


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=300,default='')
    price = models.FloatField(null=False, blank=False)
    descr = models.TextField(blank=False, null=False)
    isActive = models.BooleanField(default=True)
    # workTime = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='services')

    photos = models.ManyToManyField('ServiceAttachment', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='services', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.title}'

    def created_at_formatted(self):
        return timesince(self.created_at)
