from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import RequestContext
from suggestion.models import Suggestion
from comment.models import Comment
from general.models import ContactInfo, Tools
from request.models import Request


@login_required(login_url='/')
def dashboard(request):
    suggestions = Suggestion.objects.filter(state=False).count()
    comments = Comment.objects.filter(deleted=False).count()
    requests = Request.objects.filter(deleted=False, state=False).count()
    data = {'suggestions': suggestions, 'comments': comments, 'requests': requests}
    return render_to_response('dashboard.html', {'data': data}, RequestContext(request))


@login_required(login_url='/login')
def change_pass(request):
    if request.method == 'POST':
        password = request.POST['password']
        passwordN = request.POST['passwordN']
        passwordR = request.POST['passwordR']
        if request.user.check_password(password):
            if passwordN != passwordR:
                messages.error(request, 'Las contrase&ntilde;as no coinciden.')
            else:
                passwordNS = make_password(passwordN)
                request.user.password = passwordNS
                request.user.save()
                result = authenticate(username=request.user.username, password=passwordN)
                login(request, result)
                messages.success(request, 'Contrase&ntilde;a cambiada satisfactoriamente.')
                return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'Su contrase&ntilde;a es incorrecta.')
    return render_to_response('change_pass.html', RequestContext(request))


@login_required(login_url='/')
def contact_info(request):
    contact = ContactInfo.objects.all()
    data = {}
    if contact:
        data['contact'] = contact[0]
    if request.method == 'POST':
        phone = request.POST['phone']
        cel = request.POST['cel']
        email = request.POST['email']
        direction = request.POST['direction']
        fax = request.POST['fax']
        contact = ContactInfo.objects.all()
        if contact:
            contact[0].phone = phone
            contact[0].cel = cel
            contact[0].email = email
            contact[0].direccion = direction
            contact[0].fax = fax
            contact[0].save()
        else:
            contact = ContactInfo(phone=phone, cel=cel, fax=fax, direccion=direction, email=email)
            contact.save()
        messages.success(request, 'Informaci&oacute;n de contacto editada satisfactoriamente.')
        return HttpResponseRedirect(reverse('contact_info'))
    return render_to_response('contact_info.html', {'data': data}, RequestContext(request))


def login_system(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard'))
    usuario = User.objects.filter(username='adminroot')
    if not usuario:
        Tools.objects.create_superuser(username='adminroot', email='adminroot@gmail.com', password='adminroot')
    usuario = User.objects.filter(username='gerson')
    if not usuario:
        Tools.objects.create_superuser(username='gerson', email='gerson@gmail.com', password='123')

    has_error = False
    data = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        result = authenticate(username=username, password=password)
        if result is None or not result.is_staff:
            has_error = True
        else:
            login(request, result)
            return HttpResponseRedirect(reverse('dashboard'))
        if has_error:
            data['username'] = username
            data['has_error'] = has_error
    return render_to_response('login.html', {'data': data}, RequestContext(request))


@login_required(login_url='/')
def close(request):
    logout(request)
    request.session.clear()
    return HttpResponseRedirect(reverse('login'))
