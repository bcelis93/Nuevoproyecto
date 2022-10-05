from http.client import HTTPResponse
from django.shortcuts import render


from AppCoder.models import Estudiante

def mostrar_inicio(request):
    familia = Estudiante(nombre="Daniela", apellido="Celis", email="dani@gmail.com")
    contexto = {"familia_1" : familia}
    return render(request, "AppCoder/inicio.html", contexto)