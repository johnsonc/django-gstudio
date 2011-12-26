"""Views for Gstudio nodetypes"""
from django.shortcuts import redirect 
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from gstudio.gnowql import *
import networkx as nx
import d3 
import json
from os.path import join
 
from gstudio.views.decorators import protect_nodetype
from gstudio.views.decorators import update_queryset

jsonFile = open("/home/johnson/Desktop/v_env_gstudio/django-gstudio/gstudio/views/egonet.json", "r")

def graph_json(request): 
    #testjson = json.loads(jsonFile)

    return HttpResponse(jsonFile.read(), "application/json")
    
def force_graph(request):
    return render_to_response('gstudio/graph1.html',{'time': 'now'})

 
#node = get_node(str(object_id))
#ot = Objecttype.objects.get(title='place')
#G = ot.get_radial_graph_json()
#    
#    G = nx.DiGraph()
#    
#    G.add_node(node)
#    
#    for key in node.get_nbh.keys():
#        # is null
#        if isinstance(node[key],list):
#           G.add_nodes_from(node[key])
#
#            for item in node[key]:
#                G.add_edge()                
#    


#    return ast(nodetype, permanent=True)
