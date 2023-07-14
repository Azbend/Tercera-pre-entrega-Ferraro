from django.shortcuts import render, redirect
from miapp.models import pais, cliente, dni

def index(request):
    return render(request, 'miapp/index.html')

def formulario(request):
    if request.method == 'POST':
        return redirect('datos')

    return render(request, 'miapp/formulario.html')

def datos(request):
    if request.method == 'POST':
        pais_de_origen = request.POST['pais_de_origen']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        dni = request.POST['dni']
        
        datos = {
            'pais_de_origen': pais_de_origen,
            'nombre': nombre,
            'apellido': apellido,
            'dni': dni
        }

        return render(request, 'miapp/datos.html', datos)

    return redirect('index')