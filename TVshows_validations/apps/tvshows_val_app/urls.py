from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.new),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<Shows_id>\d+)$', views.shows),
    url(r'^destroy/(?P<Shows_id>\d+)$', views.destroy),
    url(r'^shows/(?P<Shows_id>\d+)/edit$', views.shows_edit),
    url(r'^shows/(?P<Shows_id>\d+)/updating$', views.updating)
       
]