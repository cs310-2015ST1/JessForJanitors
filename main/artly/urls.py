from django.conf.urls import patterns, url
from artly import views
from artly import populate_artly

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.map, name='map'),
    url(r'^populate/$', populate_artly.populate, name='populate'),
    url(r'^click_installation/$', views.click_installation, name='click_installation'),
    url(r'^click_save/$', views.click_save, name='click_save'),
    url(r'^logintest/$', views.home, name='home'),
    )
