from adminsortable.models import SortableMixin
from ckeditor.fields import RichTextField
from slugify import slugify

from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField('Nombre', max_length=128, blank=False)
    email_or_phone = models.CharField('Celular o e-mail', max_length=128, blank=False)
    message = models.TextField('Mensaje')
    created_at = models.DateTimeField('Fecha', auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField('Nombre', max_length=128, blank=False, unique=True)
    description = models.TextField('Descripción', default='', blank=True)
    image = models.ImageField('Imagen', upload_to='services/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', args=[self.id])
