"""Urls for the Gstudio nodetypes"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from gstudio.models import Nodetype
from gstudio.settings import PAGINATION
from gstudio.settings import ALLOW_EMPTY
from gstudio.settings import ALLOW_FUTURE

urlpatterns = patterns(
    'gstudio.views.graphs',
    url(r'^rgraph$','graph_json', name='radial_graph'), 
    url(r'^graph$','force_graph', name='force_graph'), 
    )
