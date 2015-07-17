from django.conf.urls import patterns, url
from artly import views
from artly import populate_artly
from artly import toggle_favourites

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.map, name='map'),
    url(r'^populate/$', populate_artly.populate, name='populate'),
    url(r'^toggle_favourites/$', toggle_favourites.toggle_favourites, name='toggle_favourites'),
    )
