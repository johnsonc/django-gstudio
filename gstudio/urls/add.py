"""Urls for Gstudio forms"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('gstudio.views.add',
                       url(r'^metatype/$', 'addmetatype',
                           name='gstudio_add_meatype'),
                       url(r'^objecttype/$', 'addobjecttype',
                           name='gstudio_add_objecttype'),

		       url(r'^attributetype/$', 'addattributetype',
                           name='gstudio_add_attributetype'),
		       
                       url(r'^relationtype/$', 'addrelationtype',
                           name='gstudio_add_relationtype'),	
		       url(r'^systemtype/$', 'addsystemtype',
                           name='gstudio_add_systemtype'),
		       url(r'^processtype/$', 'addprocesstype',
                           name='gstudio_add_systemtype'),	
		       url(r'^attribute/$', 'addattribute',
                           name='gstudio_add_attribute'),	
		       url(r'^relation/$', 'addrelation',
                           name='gstudio_add_relation'),	
		       url(r'^complement/$', 'addcomplement',
                           name='gstudio_add_complement'),
		       url(r'^intersection/$', 'addintersection',
                           name='gstudio_add_intersection'),	
		       url(r'^union/$', 'addunion',
                           name='gstudio_add_union'),	

	



                       )
