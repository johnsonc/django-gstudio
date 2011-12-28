"""Views for Gstudio nodetypes"""
from django.shortcuts import redirect 
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from gstudio.gnowql import *
#import networkx as nx
#import d3 
import json
import os
 
from gstudio.views.decorators import protect_nodetype
from gstudio.views.decorators import update_queryset

def graph_json(request, node_id): 

    if(node_id=='189087228'):
        jsonFile = open( os.path.join(os.path.dirname(__file__), 'egonet.json'), "r")
        #testjson = json.loads(jsonFile)

        return HttpResponse(str(jsonFile.read()), "application/json")

    try:
        node = NID.objects.get(id=node_id)
        node = node.ref        
    except:
        return HttpResponse("Node not found.", "text/html")

    return HttpResponse(str(node.get_graph_json()), "application/json")
    
def force_graph(request, node_id):
    return render_to_response('gstudio/graph1.html',{'node_id': node_id })

 
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
