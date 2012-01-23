"""Urls for the Gstudio nodetypes"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from gstudio.models import Nodetype
from gstudio.settings import PAGINATION
from gstudio.settings import ALLOW_EMPTY
from gstudio.settings import ALLOW_FUTURE

urlpatterns = patterns(
    'gstudio.views.graphs',
    url(r'^graph_json/(?P<node_id>\d+)$','graph_json', name='graph_json_d3'), 
    url(r'^graph/(?P<node_id>\d+)$','force_graph', name='force_graph_d3'), 
    )
