"""Urls for Gstudio forms"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('gstudio.views.add',
                       url(r'^addmetatype/$', 'addmetatype',
                           name='gstudio_add_meatype'),
                       url(r'^addobjecttype/$', 'addobjecttype',
                           name='gstudio_add_objecttype'),

		       url(r'^addattributetype/$', 'addattributetype',
                           name='gstudio_add_attributetype'),
		       
                       url(r'^addrelationtype/$', 'addrelationtype',
                           name='gstudio_add_addrelationtype'),	
		       url(r'^addsystemtype/$', 'addsystemtype',
                           name='gstudio_add_addsystemtype'),
		       url(r'^addprocesstype/$', 'addprocesstype',
                           name='gstudio_add_addsystemtype'),	
                       )
