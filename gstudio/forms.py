from gstudio.models import *
from django.forms import ModelForm
from django.contrib.admin import widgets  

class MetatypeForm(ModelForm):


	class Meta:
		model = Metatype
		fields = ('title', 'altnames','plural','parent','slug','creation_date','last_update','description','parent')


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
		fields =('title','altnames','slug','inverse','left_subjecttype','left_applicable_nodetypes','right_subjecttype', 'right_applicable_nodetypes','content','prior_nodes','posterior_nodes','sites')
class SystemtypeForm(ModelForm):

	class Meta:
		model =Systemtype
		fields =('title','altnames','content','parent','slug','status','nodetype_set','relationtype_set','attributetype_set','metatype_set','processtype_set',
		 'prior_nodes','posterior_nodes','sites')


class ProcesstypeForm(ModelForm):

	class Meta:
		model =Processtype
		fields =('title','altnames','content','parent','slug','status','changing_attributetype_set','changing_relationtype_set','prior_nodes','posterior_nodes','sites')


class RelationForm(ModelForm):
    class Meta:
        model = Relation

class AttributeForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(AttributeForm, self).__init__(*args, **kwargs)
		self.fields['last_update'].widget = widgets.AdminSplitDateTime()
		self.fields['creation_date'].widget = widgets.AdminSplitDateTime()

	class Meta:
		model = Attribute


class ComplementForm(ModelForm):
    class Meta:
        model = Complement

class UnionForm(ModelForm):
    class Meta:
        model = Union

class IntersectionForm(ModelForm):
    class Meta:
        model = Intersection


