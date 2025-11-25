from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pagina_inicio(request):
    return render(request, 'pagina_inicio.html')