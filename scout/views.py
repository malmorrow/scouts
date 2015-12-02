import datetime

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import Parent, Group, Ward

def index(request):
    template = loader.get_template('scout/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

class CreateParent(CreateView):
    model = Parent
    # template_name can be set as a parameter to .as_view() in urls.py, same syntax.  Not yet clear to me which arrangement would be better.
    template_name = 'scout/parent_create.html'
    fields = [
        'first_names',
        'surname',
        'sa_id_number',
        'date_of_birth',
        'postal_address',
        'work_phone',
        'cell_phone',
        'email',
        'sex',
        'marital_status',
        'occupation',
        'employer',
    ]

class CreateWard(CreateView):
    model = Ward
    template_name="scout/ward_create.html"
    fields = [
        'group',
        'first_names',
        'surname',
        'branch',
        'application_date',
        'sa_id_number',
        'date_of_birth',
        'email',
        'sex',
        'residential_address',
        'home_phone',
        'cell_phone',
        'religious_denomination',
        'special_conditions',
        'doctor',
        'medical_aid_scheme',
        'medical_aid_number',
        'medical_aid_principal_member',
        'parent1',
        'parent2',
    ]

class ParentDetail(DetailView):
    template_name="scout/parent_detail.html"
    context_object_name = 'parent'
    queryset = Parent.objects.all()

class WardDetail(DetailView):
    template_name="scout/ward_detail.html"
    context_object_name = 'ward'
    queryset = Ward.objects.all()
