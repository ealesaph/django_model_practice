from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Estudiante
from .serializers import EstudianteSerializers

# Create your views here.
@api_view(['GET','POST'])
def estudiante_lista(request):
    if request.method=='GET':
        estudiante=Estudiante.objects.all()
        ser=EstudianteSerializers(estudiante, many=True)
        return Response(ser.data)

    if request.method=='POST':
        ser=EstudianteSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

