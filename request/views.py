# coding=UTF-8

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from request.models import Request


@login_required(login_url='/')
def list(request):
    requests = Request.objects.filter(deleted=False).order_by('-date')
    data = {'requests': requests}
    return render_to_response('request/list.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def view(request, id):
    req = get_object_or_404(Request, id=id, deleted=False)
    req.save()
    data = {'request': req}
    return render_to_response('request/view.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def delete(request, id):
    req = get_object_or_404(Request, id=id, deleted=False)
    req.deleted = True
    req.deleted_at = datetime.datetime.now()
    req.save()
    messages.success(request, 'La solicitud se eliminó satisfactoriamente.')
    return HttpResponseRedirect(reverse('request_list'))


@login_required(login_url='/')
def change_state(request, id):
    req = get_object_or_404(Request, id=id, deleted=False)
    if req.state:
        req.state = False
        messages.success(request, 'La solicitud se marcó como no atendida satisfactoriamente.')
    else:
        req.state = True
        messages.success(request, 'La solicitud se atendió satisfactoriamente.')
    req.save()
    return HttpResponseRedirect(reverse('request_list'))
