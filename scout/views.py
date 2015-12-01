import datetime

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Group, Ward
from .forms import ParentForm, WardForm

def index(request):
    group_list = Group.objects.order_by('name')
    context = {
        'group_list': group_list,
    }
    return render(request, 'scout/index.html', context)

def apply(request):
    return render(request, 'scout/apply.html', {
        'ward_form': WardForm(),
        'parent1_form': ParentForm(),
        'parent2_form': ParentForm(),
    })

def application(request):
    if request.method == 'POST':
        ward_form = WardForm(request.POST)
        if ward_form.is_valid():
            ward = Ward()
            ward.group = ward_form.cleaned_data['group']
            ward.first_names = ward_form.cleaned_data['first_names']
            ward.surname = ward_form.cleaned_data['surname']
            ward.branch = ward_form.cleaned_data['branch']
            ward.application_date = ward_form.cleaned_data['application_date']
            ward.sa_id_number = ward_form.cleaned_data['sa_id_number']
            ward.date_of_birth = ward_form.cleaned_data['date_of_birth']
            ward.email = ward_form.cleaned_data['email']
            ward.residential_address = ward_form.cleaned_data['residential_address']
            ward.home_phone = ward_form.cleaned_data['home_phone']
            ward.save()
            return HttpResponse("Completed application.")
        else:
            return HttpResponse("Invalid application.")

def ward(request, ward_id):
    child = get_object_or_404(Ward, pk=ward_id)
    return render(request, 'scout/ward.html', {'ward': child})

def update(request, ward_id):
    return HttpResponse("Update application for child %s." % ward_id)
