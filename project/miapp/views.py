from django.shortcuts import render
from miapp.models import pais, cliente, dni

def index(request):
    return render(request, 'miapp/index.html')

def formulario(request):
    if request.method == 'POST':
        # Lógica para procesar el formulario y guardar los datos en las clases de modelos

    return render(request, 'miapp/formulario.html')


# Create your views here.
