from django.shortcuts import render, redirect
from.models import EmpleadoModels
from .forms import EmpleadoForms, RegistroUsuarioForms

# Create your views here.
def index (request):
    
    return render(request, 'index.html', {})

def crear_usuario(request):
    formulario = RegistroUsuarioForms()
    if request.method=='POST':
        formulario=RegistroUsuarioForms(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            print('Usuario Creado')
            return redirect('/usuarios')
    data = {
        'titulo':'Agregar Nuevo Usuario',
        'formulario':formulario
    }
    return render(request, 'insertar.html', data)

def vista_usuario(request):
    lista_usuarios = EmpleadoModels.objects.all() #Pone en lista los usuarios
    data = {
        'titulo':'Usuarios',
        'lista_usuarios':lista_usuarios
    }
    return render (request, 'usuarios.html', data)
    

def modificar_usuario(request, id):
    empleado=EmpleadoModels.objects.get(id=id)
    formulario=EmpleadoForms(instance=empleado)
    if request.method=='POST':
        formulario=EmpleadoForms(request.POST, request.FILES, instance=empleado)
        if formulario.is_valid():
            formulario.save()
        return redirect('/usuarios')
    data ={
        'titulo': 'Modificar Usuario',
        'formulario': formulario
    }
    return render(request, 'insertar.html', data)

def eliminar_usuario(request, id):
    usuario = EmpleadoModels.objects.get(id=id)
    usuario.delete()
    return redirect('/usuarios')
    