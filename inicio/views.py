from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Template, Context

# Create your views here.
def inicio(request):
    return HttpResponse("Hola Bubucita")


def bienvenida(request):
    return HttpResponse("Bienvenida a mi sitio web")

def fecha(request):
    import datetime
    fecha_actual = datetime.datetime.now()
    return HttpResponse(f"La fecha y hora actual es: {fecha_actual}")

def template1(request):
    
    nom = "Cesar"
    apellido = "Samacoits"
    
    diccionario = {"nombre": nom, "apellido": apellido}
    
    miHTML = open("C:\\Users\\cesar\\Downloads\\Python\\djangogabyinventario\\template1\\template1.html")
    
    plantilla = Template(miHTML.read())
    miHTML.close()
    contexto = Context(diccionario)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)