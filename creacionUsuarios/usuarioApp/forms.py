from django import forms
from .models import EmpleadoModels

class EmpleadoForms(forms.ModelForm):
    class Meta:
        model = EmpleadoModels
        fields = '__all__'

class RegistroUsuarioForms(forms.Form):
    nombre=forms.CharField()
    Apellido=forms.CharField()
    sueldo= forms.IntegerField()
    