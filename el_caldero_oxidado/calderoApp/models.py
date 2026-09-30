from django.db import models

# Create your models here.
class CalderoSandwich(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=250)
    pan = models.CharField(max_length=75)
    proteina = models.CharField(max_length=150)
    extra = models.CharField(max_length=250)
    precio = models.IntegerField()

class CalderoPostre(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=250)
    porcion = models.CharField(max_length=50)
    extra = models.CharField(max_length=250)
    precio = models.IntegerField()