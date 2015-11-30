from django import forms
from .models import Ward

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = ['first_names', 'surname', 'group', 'branch', 'sa_id_number', 'date_of_birth', 'email', 'residential_address', 'home_phone']
