from django.conf.urls import url 
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^processGold$', views.processGold),
    url(r'^reset$', views.reset),
]