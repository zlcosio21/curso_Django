from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona:
    def __init__(self, nombre, apellido, agno_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.agno_nacimiento = 2023 - agno_nacimiento

def saludo(request): # Primera vista
    doc_externo = open(r"C:/Users/User/Desktop/curso_django/proyecto1/proyecto1/plantillas/plantilla1.html")

    persona1 = Persona("Sebastian Andres", "Gomez Sobrino", 2006)

    hora_actual = datetime.datetime.now()

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({
        "nombre_persona":persona1.nombre,
        "apellido_persona":persona1.apellido,
        "fecha_actual":hora_actual,
        "edad":persona1.agno_nacimiento
        })

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