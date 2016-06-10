# coding=UTF-8

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from suggestion.models import Suggestion

# Create your views here.

@login_required(login_url='/')
def list(request):
    suggestions = Suggestion.objects.filter(deleted=False).order_by('-date')
    data = {'suggestions': suggestions}
    return render_to_response('suggestions/list.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def view(request, id):
    suggestion = get_object_or_404(Suggestion, id=id, deleted=False)
    suggestion.state = True
    suggestion.save()
    data = {'suggestion': suggestion}
    return render_to_response('suggestions/view.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def delete(request, id):
    suggestion = get_object_or_404(Suggestion, id=id, deleted=False)
    suggestion.deleted = True
    suggestion.deleted_at = datetime.datetime.now()
    suggestion.save()
    messages.success(request, 'La sugerencia se eliminó satisfactoriamente.')
    return HttpResponseRedirect(reverse('suggestions_list'))