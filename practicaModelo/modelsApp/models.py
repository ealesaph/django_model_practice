from django.db import models

# Create your models here.
class EstudianteModels(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    edad=models.IntegerField()