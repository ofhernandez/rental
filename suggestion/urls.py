__author__ = 'audire'

from django.conf.urls import url

urlpatterns = [
    url(r'list/$', 'suggestion.views.list', name='suggestions_list'),
    url(r'view/(?P<id>\d+)$', 'suggestion.views.view', name='view_suggestion'),
    url(r'delete/(?P<id>\d+)$', 'suggestion.views.delete', name='delete_suggestion'),
]