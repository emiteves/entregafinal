from django.db import models

# Create your models here.
class Selecciones(models.Model):

    pais = models.CharField(max_length=30)
    grupo = models.CharField(max_length=1)

class Futbolistas(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dorsal = models.IntegerField()
    pais = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre+ " " +str(self.apellido)

class Tecnicos(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)