from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=30)

class articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=15)
    precio = models.IntegerField()

class pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()