import random
from django.shortcuts import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from comment.models import Comment

from gallery.models import Service
from gallery.models import Image
from request.models import Request

# Create your views here.
from general.models import ContactInfo
from suggestion.models import Suggestion

LANGUAGES = ['es', 'en', 'pt', 'de', 'fr']


def index2(request):
    return index(request, 'en')


def index(request, lang):
    data = {'lang': lang}
    if lang not in LANGUAGES:
        return render_to_response('client/404.html', {'data': data}, RequestContext(request))
    contact_info = ContactInfo.objects.all()
    if contact_info:
        data['contact_info'] = contact_info[0]
    comments = Comment.objects.filter(deleted=False).order_by('-date')
    data['comments'] = comments
    order = ''
    if lang == 'es':
        order = 'spanish_name'
    elif lang == 'en':
        order = 'english_name'
    elif lang == 'de':
        order = 'german_name'
    elif lang == 'pt':
        order = 'portuguese_name'
    elif lang == 'fr':
        order = 'french_name'
    services_list = Service.objects.filter(deleted=False).order_by(order)
    data['services'] = services_list
    if request.method == 'POST':
        if 'btn_comment' in request.POST:
            content = request.POST['text_comment']
            comment = Comment(content=content)
            comment.save()
            return HttpResponseRedirect('/services/' + lang)
        elif 'btn_suggestion' in request.POST:
            content = request.POST['text_suggestion']
            suggestion = Suggestion(content=content)
            suggestion.save()
            return HttpResponseRedirect('/services/' + lang)
        elif 'btn_request' in request.POST:
            content = request.POST['request']
            contact_info = request.POST['contact_info']
            req = Request(content=content, contact_info=contact_info)
            req.save()
            return HttpResponseRedirect('/services/' + lang)
    return render_to_response('client/main/index.html', {'data': data}, RequestContext(request))


def services(request, lang):
    contact_info = ContactInfo.objects.all()
    comments = Comment.objects.filter(deleted=False).order_by('-date')
    data = {'lang': lang, 'comments': comments}
    if contact_info:
        data['contact_info'] = contact_info[0]
    if lang not in LANGUAGES:
        return render_to_response('client/404.html', {'data': data}, RequestContext(request))
    order = ''
    if lang == 'es':
        order = 'spanish_name'
    elif lang == 'en':
        order = 'english_name'
    elif lang == 'de':
        order = 'german_name'
    elif lang == 'pt':
        order = 'portuguese_name'
    elif lang == 'fr':
        order = 'french_name'
    if 'service' in request.GET:
        id = request.GET['service']
        error = False
        for x in range(0, len(str(id))):
            if not str(id)[x].isdigit():
                error = True
                break
        if not error:
            services_list = Service.objects.filter(deleted=False, id=int(id)).order_by(order)
            if not services_list:
                return render_to_response('client/404.html', {'data': data}, RequestContext(request))
            images = Image.objects.filter(deleted=False, service=services_list[0])
            if images:
                position = random.randrange(0, images.count())
                data['image'] = images[position]
            data['selected'] = True
            data['service'] = id
        else:
            return render_to_response('client/404.html', {'data': data}, RequestContext(request))
    else:
        services_list = Service.objects.filter(deleted=False).order_by(order)
        images = Image.objects.filter(deleted=False)
        if images:
                position = random.randrange(0, images.count())
                data['image'] = images[position]
    data['services'] = services_list
    data['images'] = images
    if request.method == 'POST':
        if 'btn_comment' in request.POST:
            content = request.POST['text_comment']
            comment = Comment(content=content)
            comment.save()
            return HttpResponseRedirect('/services/' + lang)
        elif 'btn_suggestion' in request.POST:
            content = request.POST['text_suggestion']
            suggestion = Suggestion(content=content)
            suggestion.save()
            return HttpResponseRedirect('/services/' + lang)
        elif 'btn_request' in request.POST:
            content = request.POST['request']
            contact_info = request.POST['contact_info']
            req = Request(content=content, contact_info=contact_info)
            req.save()
            return HttpResponseRedirect('/services/' + lang)
    return render_to_response('client/services/index.html', {'data': data}, RequestContext(request))


def services2(request):
    return services(request, 'en')
