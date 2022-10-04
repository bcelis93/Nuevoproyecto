from http.client import HTTPResponse
from django.shortcuts import render

from django.http import HttpResponse

def mostrar_inicio(request):
   return HttpResponse("Hola crack!")