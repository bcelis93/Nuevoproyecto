from http.client import HTTPResponse
from django.shortcuts import render


from AppCoder.models import Familia

def mostrar_inicio(request):
    familia = Familia(nombre="Daniela", apellido="Celis", edad="21", nacimiento="1999-10-10")
    familia_2 = Familia(nombre="Javier", apellido="Celis", edad="58", nacimiento="1964-05-08")
    familia_3 = Familia(nombre="Luana", apellido="Celis", edad="33", nacimiento="1989-07-12")
    contexto = {"familia_1" : familia, "familia_2" : familia_2}
    return render(request, "AppCoder/inicio.html", contexto)