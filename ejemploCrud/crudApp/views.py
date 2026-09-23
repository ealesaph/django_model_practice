from django.shortcuts import render, redirect
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

def agregar_proyecto(request):
    formulario=pF()
    if request.method=='POST':
        formulario=pF(request.POST)
        if formulario.is_valid():
            formulario.save()
            print('ok')
        return index(request)
    data={
        'titulo':'Agregar nuevo proyecto',
        'formulario':formulario
    }
    return render(request, 'agregar_proyecto.html',data)

def eliminar_proyecto(request,id):
    proyecto=pM.objects.get(id=id)
    proyecto.delete()
    return redirect('/listado_proyectos')

def modificar_proyecto(request, id):
    proyecto=pM.objects.get(id=id)
    formulario = pF(instance=proyecto)
    if request.method=='POST':
        formulario=pF(request.POST, instance=proyecto)
        if formulario.is_valid():
            formulario.save()
        return redirect('/listado_proyectos')
    data = {
        'titulo': 'Modificar nuevo proyecto',
        'formulario': formulario
    }
    return render(request, 'agregar_proyecto.html', data)