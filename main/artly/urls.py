from django.conf.urls import patterns, url
from artly import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^add_site/$', 'add_site'),
    url(r'^remove_site/$', 'remove_site'),
    )
