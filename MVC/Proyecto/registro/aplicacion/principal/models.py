from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    idtipodocumento
    lugarresidencia
    fechanacimiento = models.DateField()
    email = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length = 30)
    password = models.CharField(min_length = 10, max_length = 30)

class TipoDocumento(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(unique = True)
    descripcion = models.CharField(max_length = 100)

class Ciudad(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(unique = True)
    descripcion = models.CharField(max_length = 100)