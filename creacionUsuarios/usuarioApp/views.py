from django.shortcuts import render, redirect
from.models import EmpleadoModels
from .forms import EmpleadoForms

# Create your views here.
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

def es_administrador(user):
    return(
        user.is_authenticated
        and (
            user.is_superuser
            or user.group.filter(
                name='Administrador'
            ).exists()
        )
    )

def es_usuario_autorizado(user):
    return(
        user.is_authenticated
        and (
            user.is_superuser
            or user.groups.filter(
                name__in=['Administrador','Invitado']
            ).exists()
        )    
    )

def administrador_requerido(view_func):
    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):
        if not es_administrador(request.user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

# Listar Empleados
@login_required
def lista_empleados(request):
    if not es_usuario_autorizado(request.user):
        raise PermissionDenied
    
    empleados = EmpleadoModels.objects.all()

    contexto = {
        'empleados': empleados,
        'es_administrador': es_administrador(
            request.user
        ),
    }
    return render(request, 'empleados/lista.html', contexto)

#Ver detalle
@administrador_requerido
def detalle_empleado(request, pk):
    empleado = get_object_or_404(EmpleadoModels, pk=pk)
    return render (request, 'empleados/detalle.html', {'empleado':empleado})

#Crear Empleado
@administrador_requerido
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
        else:
            form = EmpleadoForms()
        return render(request, 'empleados/crear.html', {'form': form})

#Editar Empleado
@administrador_requerido
def editar_empleado(request, pk):
    empleado = get_object_or_404(EmpleadoModels, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForms(
            request.POST,
            instance=empleado
        )
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForms(instance=empleado)
    return render(request, 'empleados/editar.html', {'form':form, 'empleado':empleado,})

#Eliminar empleado
@administrador_requerido
def eliminar_empleado(request,pk):
    empleado = get_object_or_404(EmpleadoModels, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')
    return render(request, 'empleados/eliminar.html', {'empleado':empleado})

