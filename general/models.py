from __future__ import unicode_literals
from django.contrib.auth.models import User
from suggestion.models import Suggestion
from comment.models import Comment
from request.models import Request
import datetime

from django.db import models

# Create your models here.

class Tools(User):

    def get_suggestions(self):
        return Suggestion.objects.filter(state=False).order_by('-date')

    def get_comments(self):
        comments = Comment.objects.filter(deleted=False).order_by('-date')
        return comments

    def get_requests(self):
        requests = Request.objects.filter(deleted=False, state=False).order_by('-date')
        return requests


class ContactInfo(models.Model):
    phone = models.CharField(max_length=255)
    direccion = models.TextField()
    cel = models.CharField(max_length=255)
    email = models.EmailField()
    fax = models.CharField(max_length=255)
