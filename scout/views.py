import datetime

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.utils import timezone
from django.views.generic import DetailView
from django.core.urlresolvers import reverse

from .models import Parent, Group, Ward

def index(request):
    template = loader.get_template('scout/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        ]

class CreateParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = [
            'sa_id_number',
            'date_of_birth',
            'postal_address',
            'work_phone',
            'cell_phone',
            'sex',
            'marital_status',
            'occupation',
            'employer',
        ]

def add_parent(request):
    context = RequestContext(request)
    success = False
    if request.method == "POST":
        uform = CreateUserForm(data = request.POST)
        pform = CreateParentForm(data = request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            profile = pform.save(commit = False)
            profile.user = user
            profile.save()
            x = profile.id
    else:
        uform = CreateUserForm()
        pform = CreateParentForm()
    return render_to_response(
            'scout/parent_detail.html',
            {'uform': uform, 'pform': pform, 'success': success},
            context)

class CreateWardForm(ModelForm):
    class Meta:
        model = Ward
        fields = [
            'group',
            'branch',
            'application_date',
            'sa_id_number',
            'date_of_birth',
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

def add_ward(request):
    context = RequestContext(request)
    success = False
    if request.method == "POST":
        uform = CreateUserForm(data = request.POST)
        wform = CreateWardForm(data = request.POST)
        if uform.is_valid() and wform.is_valid():
            user = uform.save()
            profile = wform.save(commit = False)
            profile.user = user
            profile.save()
    else:
        uform = CreateUserForm()
        wform = CreateWardForm()
    return render_to_response(
            'scout/ward_detail.html',
            {'uform': uform, 'wform': wform, 'success': success},
            context)

class ParentDetail(DetailView):
    template_name="scout/parent_detail.html"
    context_object_name = 'parent'
    queryset = Parent.objects.all()

class WardDetail(DetailView):
    template_name="scout/ward_detail.html"
    context_object_name = 'ward'
    queryset = Ward.objects.all()
