from django.urls import path
from miapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    path('datos/', views.datos, name='datos'),
]