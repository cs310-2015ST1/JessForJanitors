from django.conf.urls import patterns, url
from .views import AuthComplete, LoginError
from artly import views
from artly import populate_artly

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.map, name='map'),
    url(r'^populate/$', populate_artly.populate, name='populate'),
    url(r'^click_installation/$', views.click_installation, name='click_installation'),
    url(r'^complete/(?P[^/]+)/$', AuthComplete.as_view()),
    url(r'^login-error/$', LoginError.as_view()),
    url(r'', include('social_auth.urls')),
    )
