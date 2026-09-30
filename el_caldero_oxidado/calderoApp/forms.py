from django import forms
from .models import CalderoPostre , CalderoSandwich

class CalderoPostreForms(forms.ModelForm):
    class Meta:
        model = CalderoPostre
        fields = '__all__'
        
class CalderoSandwichForms(forms.ModelForm):
    class Meta:
        model = CalderoSandwich
        fields = '__all__'