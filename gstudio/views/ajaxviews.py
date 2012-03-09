from django.http import HttpResponse
import json
from gstudio.models import *
from objectapp.models import *

def AjaxAttribute(request):
    iden = request.GET["id"]
    attr = Attributetype.objects.get(id=iden)
    subjecttype = attr.subjecttype
    returndict = {}

    for each in Objecttype.objects.all():
        if attr.subjecttype.id == each.id:
            for member in each.get_members:
                returndict[member.id] = member.title
    jsonobject = json.dumps(returndict)
    return HttpResponse(jsonobject, "application/json")
    
                
                
                

            



	
	
	
	
