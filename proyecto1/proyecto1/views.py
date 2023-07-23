from django.http import HttpResponse

def saludo(request): # Primera vista

    return HttpResponse("Hola WORLD")

def despedida(request):

    return HttpResponse("See you later")