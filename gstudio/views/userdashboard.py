from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

def userdashboard(request):
    variables = RequestContext(request)
    template = "gstudiodashboard/dashboard.html"
    return render_to_response(template, variables)
    


    
