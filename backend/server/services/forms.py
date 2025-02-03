from django.forms import ModelForm

from .models import Service, ServiceAttachment


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'descr', 'price', 'isActive', 'category')

class AttachmentForm(ModelForm):
    class Meta:
        model = ServiceAttachment
        fields = ('image',)