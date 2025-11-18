from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def SignUp(request):
    return render(request, 'signup.html')

def SignIn(request):
    return render(request, 'signin.html')

def agregar_vacante(request):
    return render(request, 'agregar-vacante.html')

def detalle_vacante(request, id):
    return render(request, 'detalle-vacante.html', {'vacante_id': id})

def editar_vacante(request, vacante_id):
   return render(request, 'editar-vacante.html', {'vacante_id': vacante_id})

def historial_vacantes(request):
    return render(request, 'historial.html')