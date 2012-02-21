from objectapp.models import *
from django.forms import ModelForm

class GbobjectForm(ModelForm):

    class Meta:
        model = Gbobject

class ProcessForm(ModelForm):

    class Meta:
        model = Process

class SystemForm(ModelForm):

    class Meta:
        model = System

