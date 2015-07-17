from django.conf.urls import patterns, url
from artly import views
from artly import populateartly

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.map, name='map'),
    url(r'^populate/$', populateartly.populate, name='populate'),
    url(r'^toggle_favourite/$', views.toggle_favourite, name='toggle_favourite'),
    )
