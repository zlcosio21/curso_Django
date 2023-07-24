from django.http import HttpResponse
import datetime
from django.template import Template, Context 
from django.template.loader import get_template

class Persona:
    def __init__(self, nombre, apellido, agno_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.agno_nacimiento = 2023 - agno_nacimiento

def saludo(request): # Primera vista

    persona1 = Persona("Sebastian Andres", "Gomez Sobrino", 2006)

    lista_temas_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegues"]

    hora_actual = datetime.datetime.now()

    doc_externo = get_template("plantilla1.html")

    documento = doc_externo.render({
        "nombre_persona":persona1.nombre,
        "apellido_persona":persona1.apellido,
        "fecha_actual":hora_actual,
        "edad":persona1.agno_nacimiento,
        "temas":lista_temas_curso
        })

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