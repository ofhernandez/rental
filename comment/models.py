from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)
    image = models.FileField(upload_to='complaints', null=True)
