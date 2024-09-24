from django.http import HttpResponse
from django.shortcuts import render
import datetime
from random import randint

def hola(request):
    texto = "Usuario"
    return render(request, "hola.html" ,{'clave': texto})

def fecha_actual(request):
    ahora = datetime.datetime.now()
    return render(request,  'fecha_actual.html',{'ahora': ahora})

def horas_adelante(request, offset):
    diferencia = int(offset)
    diferencia_de_tiempo = datetime.datetime.now() + datetime.timedelta(hours=diferencia)
    return render(request, 'horas_adelante.html' ,{'diferencia_de_tiempo':diferencia_de_tiempo})

def aleatorio(request):
    numero = randint(1, 100)
    resto = numero % 2
    return render(request, 'aleatorio.html' , {
        "numero": numero, 'resto' :resto ,
          })

def semana(request):
    semana = [
        'lunes',
        'martes',
        'miercoles',
        'jueves',
        'viernes',
        'sabado',
        'domingo',
    ]
    return render(request, 'semana.html' , {'semana': semana})