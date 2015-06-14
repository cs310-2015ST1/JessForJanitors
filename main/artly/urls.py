from django.conf.urls import patterns, url
from artly import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^click_installation/$', views.click_installation, name='click_installation'),
    )
