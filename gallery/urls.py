__author__ = 'audire'

from django.conf.urls import url

urlpatterns = [
    url(r'list/$', 'gallery.views.list', name='galleries_list'),
    url(r'new/$', 'gallery.views.new', name='new_gallery'),
    url(r'delete/(?P<id>\d+)$', 'gallery.views.delete', name='delete_gallery'),
    url(r'view/(?P<id>\d+)$', 'gallery.views.view', name='view_gallery'),
    url(r'add_images/(?P<id>\d+)$', 'gallery.views.add_images', name='add_images_gallery'),
    url(r'edit/(?P<id>\d+)$', 'gallery.views.edit', name='edit_gallery'),
    url(r'delete_image/(?P<service>\d+)/(?P<id>\d+)$', 'gallery.views.delete_image', name='delete_image'),
]