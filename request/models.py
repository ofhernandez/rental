from __future__ import unicode_literals

from django.db import models


class Request(models.Model):
    content = models.TextField()
    contact_info = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)
