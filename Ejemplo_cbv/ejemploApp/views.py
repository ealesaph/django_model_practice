from django.shortcuts import render
from .serializer import EstudianteSerializers
from .models import Estudiante
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class EstudianteLista(APIView):
    def get(self,request):
        estudiante=Estudiante.objects.all()
        ser=EstudianteSerializers(estudiante,many=True)
        return Response(ser.data)

    def post(self, request):
        ser=EstudianteSerializers(data=request.data)
        if ser.is_valid():
            ser.save
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class EstudianteDetalle(APIView):
    def get_object(self, pk):
        try:
            return Estudiante.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk ):
        estudiante=self.get_object(pk)
        ser=EstudianteSerializers(estudiante)
        return Response(ser.data)

    def put(self,request,pk):
        estudiante=self.get_object(pk)
        ser=EstudianteSerializers(estudiante,request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)