from django.contrib import admin
from gestionPedidos.models import cliente, articulo, pedido

class cliente_admin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "correo", "correo")
    search_fields = ("nombre", "telefono")

class articulo_admin(admin.ModelAdmin):
    list_display = ("nombre", "seccion", "precio")
    search_fields = ("seccion", "nombre")

# Register your models here.
admin.site.register(cliente, cliente_admin)
admin.site.register(articulo, articulo_admin)
admin.site.register(pedido)