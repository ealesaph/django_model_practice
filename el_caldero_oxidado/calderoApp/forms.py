from django import forms
from .models import CalderoModels

class CalderooForms(forms.ModelForm):
    class Meta:
        model = CalderoModels
        fields='__all__'