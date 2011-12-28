"""Views for Gstudio forms"""
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from datetime import datetime
from gstudio.forms import *
from django.core.exceptions import ValidationError

def addmetatype(request):
    if request.method == 'POST':
        formset = MetatypeForm(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/gstudio/")
        
    else:
       
        formset = MetatypeForm()
        variables = RequestContext(request,{'formset':formset})
        template = "gstudioforms/gstudiometatypeform.html"
        return render_to_response(template, variables)

    
    
def addobjecttype(request):
        if request.method == 'POST':
            formset = ObjecttypeForm(request.POST)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect("/gstudio/")
            
                    
        else:

            formset = ObjecttypeForm()

            template = "gstudioforms/gstudioobjecttypeform.html"
            variables = RequestContext(request,{'formset':formset})
            return render_to_response(template, variables)

def addrelationtype(request):
        if request.method == 'POST':
            formset = RelationtypeForm(request.POST)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect("/gstudio/")
            
                    
        else:

            formset = RelationtypeForm()

            template = "gstudioforms/gstudiorelationtypeform.html"
            variables = RequestContext(request,{'formset':formset})
            return render_to_response(template, variables)


def addattributetype(request):
        if request.method == 'POST':
            formset = AttributetypeForm(request.POST)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect("/gstudio/")
            
                    
        else:

            formset = AttributetypeForm()

            template = "gstudioforms/gstudioattributetypeform.html"
            variables = RequestContext(request,{'formset':formset})
            return render_to_response(template, variables)


def addsystemtype(request):
        if request.method == 'POST':
            formset = SystemtypeForm(request.POST)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect("/gstudio/")
            
                    
        else:

            formset = SystemtypeForm()

            template = "gstudioforms/gstudioattributetypeform.html"
            variables = RequestContext(request,{'formset':formset})
            return render_to_response(template, variables)

def addprocesstype(request):
        if request.method == 'POST':
            formset = ProcesstypeForm(request.POST)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect("/gstudio/")
            
                    
        else:

            formset = ProcesstypeForm()

            template = "gstudioforms/gstudioprocesstypeform.html"
            variables = RequestContext(request,{'formset':formset})
            return render_to_response(template, variables)









