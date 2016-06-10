from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Service(models.Model):
    spanish_name = models.CharField(max_length=255, unique=True)
    english_name = models.CharField(max_length=255, unique=True)
    french_name = models.CharField(max_length=255, unique=True)
    german_name = models.CharField(max_length=255, unique=True)
    portuguese_name = models.CharField(max_length=255, unique=True)
    spanish_description = models.TextField(null=True)
    english_description = models.TextField(null=True)
    french_description = models.TextField(null=True)
    german_description = models.TextField(null=True)
    portuguese_description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.CharField(max_length=255)


class Image(models.Model):
    name = models.FileField(upload_to='gallery')
    date = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    service = models.ForeignKey(Service)