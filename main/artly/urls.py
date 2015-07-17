from django.conf.urls import patterns, url
from artly import views
from artly import populate_artly

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.map, name='map'),
    url(r'^populate/$', populate_artly.populate, name='populate'),
    url(r'^toggle_favourite/$', views.toggle_favourite, name='toggle_favourite'),
    )
