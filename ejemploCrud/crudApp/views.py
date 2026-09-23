from django.shortcuts import render
from .models import ProyectoModels as pM
from .forms import ProyectoForms as pF

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def listado_proyectos(request):
    lista_proyectos= pM.objects.all()
    data={
        'lista_proyectos':lista_proyectos
    }
    return render(request, 'listado_proyectos.html',data)