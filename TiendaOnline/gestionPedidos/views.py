from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulo
from django.core.mail import send_mail
from django.conf import settings

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
    if request.method == "POST":

        asunto = request.POST["asunto"]
        mensaje = request.POST["mensaje"] + " " + request.POST["email"]
        email = settings.EMAIL_HOST_USER
        recibir_mails = [""]
        send_mail(asunto, mensaje, email, recibir_mails)

        return render(request, "gracias.html")
    
    return render(request, "contacto.html")
      