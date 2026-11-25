from django.shortcuts import render
from  rest_framework import viewsets
from .models import Estudiante
from .serializers import EstudianteSerializers

# Create your views here.
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all()
    serializer_class=EstudianteSerializers