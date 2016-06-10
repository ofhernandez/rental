__author__ = 'audire'

from django.conf.urls import url

urlpatterns = [
    url(r'list/$', 'request.views.list', name='request_list'),
    url(r'view/(?P<id>\d+)$', 'request.views.view', name='view_request'),
    url(r'change_state/(?P<id>\d+)$', 'request.views.change_state', name='change_state_request'),
    url(r'delete/(?P<id>\d+)$', 'request.views.delete', name='delete_request'),
]