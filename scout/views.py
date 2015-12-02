import datetime

from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import Parent, Group, Ward

class CreateParent(CreateView):
    model = Parent
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
    model = Parent
    def get_context_data(self, **kwargs):
        context = super(ParentDetail, self).get_context_data(**kwargs)

        context['book_list'] = Book.objects.all()
        return context

