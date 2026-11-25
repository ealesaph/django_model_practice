from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    promedio=models.DecimalField(max_digits=3,decimal_places=1)

