from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from datetime import datetime
from objectapp.forms import *


def addgbobject(request):
    if request.method == 'POST':
        formset = GbobjectForm(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/objects/")
 
 
        
    else:
       
        formset = GbobjectForm()


    variables = RequestContext(request,{'formset':formset})
    template = "objectappforms/gbobjectform.html"
    return render_to_response(template, variables)


def addprocess(request):
    if request.method == 'POST':
        formset = ProcessForm(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/objects/")
 
 
        
    else:
       
        formset = ProcessForm()


    variables = RequestContext(request,{'formset':formset})
    template = "objectappforms/processform.html"
    return render_to_response(template, variables)

def addsystem(request):
    if request.method == 'POST':
        formset = ProcessForm(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/objects/")
 
 
        
    else:
       
        formset = SystemForm()


    variables = RequestContext(request,{'formset':formset})
    template = "objectappforms/systemform.html"
    return render_to_response(template, variables)
