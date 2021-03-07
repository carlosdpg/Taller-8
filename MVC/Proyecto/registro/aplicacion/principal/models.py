from django.db import models

# Create your models here.

class TipoDocumento(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(unique = True, max_length = 30)
    descripcion = models.CharField(max_length = 100)

class Ciudad(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(unique = True, max_length = 30)
    descripcion = models.CharField(max_length = 100)

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    idtipodocumento = models.ForeignKey(TipoDocumento, on_delete = models.CASCADE)
    documento = models.IntegerField(unique = True)
    lugarresidencia = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    fechanacimiento = models.DateField()
    email = models.EmailField(max_length = 50)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)