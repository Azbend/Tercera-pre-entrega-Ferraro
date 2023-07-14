from django.shortcuts import render
from miapp.models import pais, cliente, dni

def index(request):
    return render(request, 'miapp/index.html')

def formulario(request):
    if request.method == 'POST':
        

    return render(request, 'miapp/formulario.html')


