__author__ = 'audire'

from django.conf.urls import url

urlpatterns = [
    url(r'list/$', 'comment.views.list', name='comments_list'),
    url(r'view/(?P<id>\d+)$', 'comment.views.view', name='view_comment'),
    url(r'delete/(?P<id>\d+)$', 'comment.views.delete', name='delete_comment'),
]