from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): # Primera vista

    doc_externo = open(r"C:/Users/User/Desktop/curso_django/proyecto1/proyecto1/plantillas/plantilla1.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("See you later")

def fechaActual(request):

    fecha_hora = datetime.datetime.now()

    return HttpResponse(fecha_hora)

def calculaEdad(request, edad, agno):
    
    periodo = agno - 2023
    edad_futura = edad + periodo
    documento = "<html><body><h2>En en el agno %s tendras %s agnos" %(agno, edad_futura)

    return HttpResponse(documento)