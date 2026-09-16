from django import forms

class RegistroUsuarioForms(forms.Form):
    nombre=forms.CharField()
    email=forms.CharField(widget=forms.EmailInput)
    edad=forms.IntegerField()