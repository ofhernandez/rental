# coding=UTF-8

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from comment.models import Comment

# Create your views here.

@login_required(login_url='/')
def list(request):
    comments = Comment.objects.filter(deleted=False).order_by('-date')
    data = {'comments': comments}
    return render_to_response('comments/list.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def view(request, id):
    comment = get_object_or_404(Comment, id=id, deleted=False)
    data = {'comment': comment}
    return render_to_response('comments/view.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def delete(request, id):
    comment = get_object_or_404(Comment, id=id, deleted=False)
    comment.deleted = True
    comment.deleted_at = datetime.datetime.now()
    comment.save()
    messages.success(request, 'El comentario se eliminó satisfactoriamente.')
    return HttpResponseRedirect(reverse('comments_list'))