from django import forms
from .models import ProyectoModels

class ProyectoForms(forms.ModelForm):
    class Meta:
        model=ProyectoModels
        fields='__all__'