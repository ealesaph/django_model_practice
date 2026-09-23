from django import forms as fr
from .models import ProyectoModels

class ProyectoForms(fr.ModelForm):
    class Meta:
        model=ProyectoModels
        fields='__all__'