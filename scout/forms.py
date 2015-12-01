from django import forms
from .models import Parent, Ward

class ParentForm(forms.ModelForm):
    class Meta:
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

class WardForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = [
            'first_names',
            'surname',
            'application_date',
            'group',
            'branch',
            'sa_id_number',
            'date_of_birth',
            'email',
            'sex',
            'residential_address',
            'home_phone',
            'cell_phone',
            'religious_denomination',
            'special_conditions',
        ]
