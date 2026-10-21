from django.db import models

# Create your models here.
class EmpleadoModels(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    sueldo= models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellido', 'nombre']