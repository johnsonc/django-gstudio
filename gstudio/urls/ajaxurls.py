"""Urls for the Gstudio sitemap"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('gstudio.views.ajaxviews',
                       url(r'^$', 'AjaxAttribute',

                           name='ajax_views'),
                       )
