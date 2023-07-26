from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulo

# Create your views here.
def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["producto"]:
       
       #mensaje = "Articulo buscado: %r" %request.GET["producto"]
       producto = request.GET["producto"]
       articulos = articulo.objects.filter(nombre__icontains = producto)
       return render(request, "resultado_busqueda.html", {"articulos":articulos, "query":producto,})
    else:
        mensaje = "No se ha encontrado nada"
    return HttpResponse(mensaje)