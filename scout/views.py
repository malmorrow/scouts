import datetime

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Group, Ward
from .forms import ApplicationForm

def index(request):
    group_list = Group.objects.order_by('name')
    context = {
        'group_list': group_list,
    }
    return render(request, 'scout/index.html', context)

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            ward = Ward()
            ward.group = form.cleaned_data['group']
            ward.first_names = form.cleaned_data['first_names']
            ward.surname = form.cleaned_data['surname']
            ward.branch = form.cleaned_data['branch']
            ward.application_date = form.cleaned_data['application_date']
            ward.sa_id_number = form.cleaned_data['sa_id_number']
            ward.date_of_birth = form.cleaned_data['date_of_birth']
            ward.email = form.cleaned_data['email']
            ward.residential_address = form.cleaned_data['residential_address']
            ward.home_phone = form.cleaned_data['home_phone']
            ward.save()
            return HttpResponseRedirect(reverse('scout:apply'))
    else:
        form = ApplicationForm()

    return render(request, 'scout/apply.html', {'form': form})

def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            ward = Ward()
            ward.group = form.cleaned_data['group']
            ward.first_names = form.cleaned_data['first_names']
            ward.surname = form.cleaned_data['surname']
            ward.branch = form.cleaned_data['branch']
            ward.application_date = form.cleaned_data['application_date']
            ward.sa_id_number = form.cleaned_data['sa_id_number']
            ward.date_of_birth = form.cleaned_data['date_of_birth']
            ward.email = form.cleaned_data['email']
            ward.residential_address = form.cleaned_data['residential_address']
            ward.home_phone = form.cleaned_data['home_phone']
            ward.save()
            #return HttpResponseRedirect(reverse('scout:apply'))
    return HttpResponse("Completed application.")

def ward(request, ward_id):
    child = get_object_or_404(Ward, pk=ward_id)
    return render(request, 'scout/ward.html', {'ward': child})

def update(request, ward_id):
    return HttpResponse("Update application for child %s." % ward_id)
