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

@api_view(['GET','PUT','DELETE'])
def estudiante_detallle(request, pk):
    try:
        estudiante=Estudiante.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        ser=EstudianteSerializers(estudiante)
        return Response(ser.data)

    if request.method=='PUT':
        ser=EstudianteSerializers(estudiante,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=='DELETE':
        estudiante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        