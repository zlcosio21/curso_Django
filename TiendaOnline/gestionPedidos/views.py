from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulo

# Create your views here.
def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["producto"]:
       producto = request.GET["producto"]
       if len(producto) < 20:
          articulos = articulo.objects.filter(nombre__icontains = producto)
          return render(request, "resultado_busqueda.html", {"articulos":articulos, "query":producto,})
       else:
           mensaje = "El numero de caracteres es muy grande"
    else:
        mensaje = "No se ha introducido nada"
    return HttpResponse(mensaje)