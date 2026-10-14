from django.db import models

# Create your models here.
class EmpleadoModels(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    sueldo= models.IntegerField()