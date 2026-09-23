from django.db import models

# Create your models here.
class ProyectoModels(models.Model):
    fecha_inicio=models.DateField()
    fecha_termino=models.DateField()
    nombre=models.CharField(max_length=30)
    responsable=models.CharField(max_length=50)
    prioridad=models.IntegerField()