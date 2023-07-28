from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulo
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

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


def contacto(request):
    if request.method=="POST":

        formulario_contacto = FormularioContacto(request.POST)

        if formulario_contacto.is_valid():

            info_formulario = formulario_contacto.cleaned_data

            destinatarios = [info_formulario['email']]

            send_mail(info_formulario['asunto'], info_formulario['mensaje'], info_formulario['email'], destinatarios)

            return render(request, "gracias.html")
    else:

        formulario_contacto = FormularioContacto()
    
    return render(request, "formulario_contacto.html", {"form":formulario_contacto})
      