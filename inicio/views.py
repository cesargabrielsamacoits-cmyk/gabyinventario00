from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Hola Bubucita")


def bienvenida(request):
    return HttpResponse("Bienvenida a mi sitio web")

def fecha(request):
    import datetime
    fecha_actual = datetime.datetime.now()
    return HttpResponse(f"La fecha y hora actual es: {fecha_actual}")