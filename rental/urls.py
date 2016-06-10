"""rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/$', 'general.views.login_system', name='login'),
    url(r'^admin/close$', 'general.views.close', name='close'),
    url(r'^admin/dashboard/', 'general.views.dashboard', name='dashboard'),
    url(r'^admin/change_pass/', 'general.views.change_pass', name='change_pass'),
    url(r'^admin/contact_info/', 'general.views.contact_info', name='contact_info'),
    url(r'^admin/suggestions/', include('suggestion.urls')),
    url(r'^admin/request/', include('request.urls')),
    url(r'^admin/comments/', include('comment.urls')),
    url(r'^admin/galleries/', include('gallery.urls')),
    url(r'^$', 'client.views.index2', name='client2'),
    url(r'^services/$', 'client.views.services2', name='services2'),
    url(r'^services/(?P<lang>\D+)/$', 'client.views.services', name='services'),
    url(r'^(?P<lang>\D+)/$', 'client.views.index', name='client'),



]
