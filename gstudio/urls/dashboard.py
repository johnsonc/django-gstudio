"""Url for Gstudio User Dashboard"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('gstudio.views.userdashboard',
                       url(r'^$', 'userdashboard',
                           name='gstudio_userdashboard'),

                       )
