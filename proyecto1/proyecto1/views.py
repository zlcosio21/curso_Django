from django.http import HttpResponse
import datetime

def saludo(request): # Primera vista

    return HttpResponse("Hola WORLD")

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