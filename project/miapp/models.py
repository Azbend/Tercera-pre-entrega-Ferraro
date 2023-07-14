from django.db import models

# Create your models here.
from django.db import models

class pais(models.Model):
    pais_de_origen = models.CharField(max_length=50)
    
    def __str__(self):
        return self.pais_de_origen

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.nombre} {self.apellido}")

class dni(models.Model):
    dni = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dni
