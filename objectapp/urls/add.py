"""Urls for Objectapp forms"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('objectapp.views.add',
                       url(r'^gbobject/$', 'addgbobject',
                           name='objectapp_add_gbobject'),
                       url(r'^process/$', 'addprocess',
                           name='objectapp_add_gbobject'),
                       url(r'^system/$', 'addsystem',
                           name='objectapp_add_system'),

                       )

