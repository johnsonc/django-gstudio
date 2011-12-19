"""MetatypeAdmin for Gstudio"""
from django.contrib import admin
from django.core.urlresolvers import NoReverseMatch
from django.utils.translation import ugettext_lazy as _
from ajax_select import LookupChannel
from django.utils.html import escape
from gstudio.admin.forms import AttributeAdminForm
from gstudio.models import *
import reversion

class AttributeAdmin(reversion.VersionAdmin):
    class Media:
        js = ("gstudio/js/gstudio.js",)
    
    def save_model(self, request, attribute, form, change):
        attribute.title = attribute.composed_attribution
        attribute.save()

class PersonLookup(LookupChannel):

    model = Attribute

    def get_result(self,q,request):
        return NID.objects.filter(Q(title__icontains=q) )

        

    def get_result(self,obj):
        
        return obj.name

    def format_match(self,obj):
            """ (HTML) formatted item for display in the dropdown """
            return self.format_item_display(obj)

    def format_item_display(self,obj):
            """ (HTML) formatted item for displaying item in the selected deck area """
            return u"%s<div><i>%s</i></div>" % (escape(obj.name),escape(obj.email))




