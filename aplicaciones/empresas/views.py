from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Enterprises Home Page")

def SignUp(request):
    return HttpResponse("REgistra tu empresa")

def SignIn(request):
    return HttpResponse("Inicia sesión en tu cuenta")

def agregar_vacante(request):
    return HttpResponse("Agregar una nueva vacante")

def detalle_vacante(request, id):
    return HttpResponse(f"Detalle de la vacante con ID: {id}")

def editar_vacante(request, vacante_id):
    return HttpResponse(f"Editar la vacante con ID: {vacante_id}")

def historial_vacantes(request):
    return HttpResponse("Historial de vacantes publicadas")