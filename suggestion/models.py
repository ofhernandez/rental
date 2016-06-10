from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Suggestion(models.Model):
    content = models.TextField()
    answer = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    state = models.BooleanField(default=False)
    image = models.FileField(upload_to='complaints', null=True)
    contact_info = models.TextField(null=True)