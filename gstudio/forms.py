from gstudio.models import *
from django.forms import ModelForm

class MetatypeForm(ModelForm):

    class Meta:
        model = Metatype

class ObjecttypeForm(ModelForm):                 

    class Meta:
        model = Objecttype
        fields = ('title', 'altnames','plural','parent','slug','metatypes','tags',
                      'status','content','prior_nodes','posterior_nodes','password','login_required','sites')

class AttributetypeForm(ModelForm):

    class Meta:
         model = Attributetype
         fields =('title','altnames','subjecttype','applicable_nodetypes','dataType',
		  'slug','status','content','prior_nodes','posterior_nodes','password','login_required','sites')

class RelationtypeForm(ModelForm):

    class Meta:
         model = Relationtype
         fields =('title','altnames','slug','inverse','left_subjecttype','left_applicable_nodetypes','right_subjecttype',
		 'right_applicable_nodetypes','content','prior_nodes','posterior_nodes','sites')
class SystemtypeForm(ModelForm):

    class Meta:
         model =Systemtype
         fields =('title','altnames','content','parent','slug','status','nodetype_set','relationtype_set','attributetype_set','metatype_set','processtype_set',
		 'prior_nodes','posterior_nodes','sites')


class ProcesstypeForm(ModelForm):

    class Meta:
         model =Processtype
         fields =('title','altnames','content','parent','slug','status','changing_attributetype_set','changing_relationtype_set',
		 'prior_nodes','posterior_nodes','sites')

class AttributeForm(ModelForm):
    class Meta:
        model = Attribute


