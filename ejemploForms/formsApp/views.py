from django.shortcuts import render
from .forms import RegistroUsuarioForms

# Create your views here.
def index(request):
    formulario = RegistroUsuarioForms()
    data = {
        'formulario':formulario
    }
    return render(request, 'index.html', data)