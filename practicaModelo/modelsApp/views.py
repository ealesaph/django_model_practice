from django.shortcuts import render
from .models import EstudianteModels
# Create your views here.
def estudiante_datos(request):
    lista_estudiante=EstudianteModels.objects.all()
    data={
        'lista_estudiante':lista_estudiante
    }
    return render(request,'estudianteDatos.html', data)