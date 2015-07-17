from django.conf.urls import patterns, url
import views
import populateartly

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.map, name='map'),
    url(r'^populate/$', populateartly.populate, name='populate'),
    url(r'^click_installation/$', views.click_installation, name='click_installation'),
    url(r'^click_save/$', views.click_save, name='click_save'),
    )
