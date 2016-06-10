# coding=UTF-8

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from gallery.models import Service
from gallery.models import Image


@login_required(login_url='/')
def list(request):
    galleries = Service.objects.filter(deleted=False)
    data = {'galleries': galleries, 'length': galleries.count()}
    return render_to_response('galleries/list.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def new(request):
    length = Service.objects.filter(deleted=False).count()
    if length >= 6:
        messages.error(request, 'Límite de 6 servicios excedido.')
        return HttpResponseRedirect(reverse('galleries_list'))
    data = {}
    if request.method == 'POST':
        spanish_name = request.POST['spanish_name']
        english_name = request.POST['english_name']
        french_name = request.POST['french_name']
        german_name = request.POST['german_name']
        portuguese_name = request.POST['portuguese_name']
        spanish_description = request.POST['spanish_description']
        english_description = request.POST['english_description']
        french_description = request.POST['french_description']
        portuguese_description = request.POST['portuguese_description']
        german_description = request.POST['german_description']
        icon = request.POST['icon']
        if spanish_name == '' or english_name == '' or french_name == '' or german_name == '' or portuguese_name == '' or \
            spanish_description == '' or english_description == '' or french_description == '' or german_description == '' or portuguese_description == '':
            messages.error(request, 'Todos los campos son obligatorios.')
        else:
            validate_spanish = Service.objects.filter(spanish_name=spanish_name)
            validate_english = Service.objects.filter(english_name=english_name)
            validate_french = Service.objects.filter(french_name=french_name)
            validate_german = Service.objects.filter(german_name=german_name)
            validate_portuguese = Service.objects.filter(portuguese_name=portuguese_name)
            if not validate_english and not validate_french and not validate_german and not validate_portuguese and not validate_spanish:
                if icon == 'none':
                    icon = 'sun-o'
                gallery = Service(spanish_name=spanish_name,
                                  english_name=english_name,
                                  french_name=french_name,
                                  german_name=german_name,
                                  portuguese_name=portuguese_name,
                                  spanish_description=spanish_description,
                                  english_description=english_description,
                                  french_description=french_description,
                                  portuguese_description=portuguese_description,
                                  german_description=german_description,
                                  icon=icon
                                  )
                gallery.save()
                messages.success(request, 'Servicio creado satisfactoriamente.')
                return HttpResponseRedirect(reverse('galleries_list'))
            else:
                messages.error(request, 'Ya existe un servicio con alguno delos nombres solicitados.')
                data['spanish_name'] = spanish_name
                data['english_name'] = english_name
                data['french_name'] = french_name
                data['german_name'] = german_name
                data['portuguese_name'] = portuguese_name
                data['spanish_description'] = spanish_description
                data['english_description'] = english_description
                data['french_description'] = french_description
                data['german_description'] = german_description
                data['portuguese_description'] = portuguese_description
    return render_to_response('galleries/new.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def edit(request, id):
    service = get_object_or_404(Service, id=id)
    data = {}
    data['spanish_name'] = service.spanish_name
    data['english_name'] = service.english_name
    data['french_name'] = service.french_name
    data['german_name'] = service.german_name
    data['portuguese_name'] = service.portuguese_name
    data['spanish_description'] = service.spanish_description
    data['english_description'] = service.english_description
    data['french_description'] = service.french_description
    data['german_description'] = service.german_description
    data['portuguese_description'] = service.portuguese_description
    data['icon'] = service.icon
    if request.method == 'POST':
        spanish_name = request.POST['spanish_name']
        english_name = request.POST['english_name']
        french_name = request.POST['french_name']
        german_name = request.POST['german_name']
        portuguese_name = request.POST['portuguese_name']
        spanish_description = request.POST['spanish_description']
        english_description = request.POST['english_description']
        french_description = request.POST['french_description']
        portuguese_description = request.POST['portuguese_description']
        german_description = request.POST['german_description']
        icon = request.POST['icon']
        if spanish_name == '' or english_name == '' or french_name == '' or german_name == '' or portuguese_name == '' or \
            spanish_description == '' or english_description == '' or french_description == '' or german_description == '' or portuguese_description == '':
            messages.error(request, 'Todos los campos son obligatorios.')
        else:
            validate_spanish = Service.objects.filter(spanish_name=spanish_name)
            validate_english = Service.objects.filter(english_name=english_name)
            validate_french = Service.objects.filter(french_name=french_name)
            validate_german = Service.objects.filter(german_name=german_name)
            validate_portuguese = Service.objects.filter(portuguese_name=portuguese_name)
            has_error = False
            if validate_spanish and str(validate_spanish[0].id) != str(id):
                messages.error(request, 'Ya existe un servicio con el nombre en español especificado.')
                has_error = True
            if validate_english and str(validate_english[0].id) != str(id):
                messages.error(request, 'Ya existe un servicio con el nombre en inglés especificado.')
                has_error = True
            if validate_german and str(validate_german[0].id) != str(id):
                messages.error(request, 'Ya existe un servicio con el nombre en alemán especificado.')
                has_error = True
            if validate_french and str(validate_french[0].id) != str(id):
                messages.error(request, 'Ya existe un servicio con el nombre en francés especificado.')
                has_error = True
            if validate_portuguese and str(validate_portuguese[0].id) != str(id):
                messages.error(request, 'Ya existe un servicio con el nombre en portugués especificado.')
                has_error = True
            if not has_error:
                if icon == 'none':
                    icon = 'sun-o'
                service.spanish_name = spanish_name
                service.spanish_description = spanish_description
                service.english_name = english_name
                service.english_description = english_description
                service.french_name = french_name
                service.french_description = french_description
                service.portuguese_name = portuguese_name
                service.portuguese_description = portuguese_description
                service.german_name = german_name
                service.german_description = german_description
                service.icon = icon
                service.save()
                messages.success(request, 'Servicio editado satisfactoriamente.')
                return HttpResponseRedirect(reverse('galleries_list'))
            else:
                data['spanish_name'] = spanish_name
                data['english_name'] = english_name
                data['french_name'] = french_name
                data['german_name'] = german_name
                data['portuguese_name'] = portuguese_name
                data['spanish_description'] = spanish_description
                data['english_description'] = english_description
                data['french_description'] = french_description
                data['german_description'] = german_description
                data['portuguese_description'] = portuguese_description
                data['icon'] = icon
    return render_to_response('galleries/edit.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def view(request, id):
    gallery = get_object_or_404(Service, id=id, deleted=False)
    images = Image.objects.filter(service=gallery, deleted=False)
    data = {'gallery': gallery, 'images': images}
    return render_to_response('galleries/view.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def delete(request, id):
    service = get_object_or_404(Service, id=id)
    service.deleted = True
    service.deleted_at = datetime.datetime.now()
    service.save()
    messages.success(request, 'Servicio eliminado satisfactoriamente.')
    return HttpResponseRedirect(reverse('galleries_list'))


@login_required(login_url='/')
def add_images(request, id):
    gallery = get_object_or_404(Service, id=id, deleted=False)
    data = {'gallery': gallery}
    if request.method == 'POST':
        images = request.FILES
        new = Image(name=images['file'], service=gallery)
        new.save()
        messages.success(request, 'Im&aacute;genes subidas satisfactoriamente.')
    return render_to_response('galleries/add_images.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def delete_image(request, service, id):
    serviceO = get_object_or_404(Service, id=service)
    image = get_object_or_404(Image, pk=id, service=serviceO)
    image.deleted = True
    image.deleted_at = datetime.datetime.now()
    image.save()
    messages.success(request, 'Imagen eliminada satisfactoriamente.')
    return HttpResponseRedirect('admin/galleries/view/'+ str(service))
