from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

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
            return HttpResponseRedirect('/application/')
    else:
        form = ApplicationForm()

    return render(request, 'scout/apply.html', {'form': form})

def ward(request, ward_id):
    child = get_object_or_404(Ward, pk=ward_id)
    return render(request, 'scout/ward.html', {'ward': child})

def update(request, ward_id):
    return HttpResponse("Update application for child %s." % ward_id)
