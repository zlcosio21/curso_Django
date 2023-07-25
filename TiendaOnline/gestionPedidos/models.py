from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    correo = models.EmailField(blank=True, null=True, verbose_name="Correo")
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return "%s, %s, %s, %s" % (self.nombre, self.direccion, self.correo, self.telefono)

class articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=15)
    precio = models.IntegerField()

    def __str__(self):
        return "%s, %s, %s" % (self.nombre, self.seccion, self.precio)

class pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()