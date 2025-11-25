from django.shortcuts import render
from django.http import HttpResponse
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Trabajador
# Importamos todos tus diccionarios
from aplicaciones.etiquetas import SINCO, VACANTE_TAGS, GENERO_OPCIONES, NIVEL_ESTUDIOS, TIEMPO_EXPERIENCIA


# Administración de usuario

def registrar_trabajador(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password') # Nuevo

            # Validaciones básicas
            if password != confirm_password:
                messages.error(request, 'Las contraseñas no coinciden.')
                return render(request, 'registro_trabajador.html', get_context_trabajador())

            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya existe.')
                return render(request, 'registro_trabajador.html', get_context_trabajador())
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya está registrado.')
                return render(request, 'registro_trabajador.html', get_context_trabajador())

            # Crear Usuario
            user = User.objects.create_user(username=username, email=email, password=password)

            # Convertir checkbox a booleano (Si está en POST es True, si no es False)
            movilidad = True if request.POST.get('movilidad_limitada') else False

            # Crear Trabajador
            Trabajador.objects.create(
                usuario=user,
                nombre=request.POST.get('nombre'),
                apellido_p=request.POST.get('apellido_p'),
                apellido_m=request.POST.get('apellido_m'),
                genero=request.POST.get('genero'),
                nacionalidad=request.POST.get('nacionalidad'),
                email=email,
                telefono=request.POST.get('telefono'),
                cod_post=request.POST.get('cod_post'),
                movilidad_limitada=movilidad, # Guardamos booleano
                
                biografia=request.POST.get('biografia'),
                estudios=request.POST.get('estudios'),
                titulo=request.POST.get('titulo'),
                
                # Orden lógico corregido
                ult_area_ocup=request.POST.get('ult_area_ocup'), # ID numérico
                ult_exp=request.POST.get('ult_exp'), # Tiempo
                descripcion_exp=request.POST.get('descripcion_exp'),
                
                hard_skills=request.POST.get('hard_skills'),
                soft_skills=request.POST.get('soft_skills'),
                
                # Nuevo: Área de interés como índice SINCO
                area_interes=request.POST.get('area_interes'), 
                intereses=request.POST.get('intereses') # Tags adicionales
            )

            messages.success(request, "¡Cuenta creada! Bienvenido a Tu Primera Chamba.")
            return redirect('login')

        except Exception as e:
            messages.error(request, f"Error en el registro: {str(e)}")

    # GET
    return render(request, 'registro_trabajador.html', get_context_trabajador())


def get_context_trabajador():
    """Helper para empaquetar los diccionarios en JSON"""
    return {
        'sinco_json': json.dumps(SINCO),
        'generos_json': json.dumps(GENERO_OPCIONES),
        'estudios_json': json.dumps(NIVEL_ESTUDIOS),
        'experiencia_json': json.dumps(TIEMPO_EXPERIENCIA),
        # Dividimos VACANTE_TAGS por secciones para facilitar el frontend
        'tags_industria_json': json.dumps(VACANTE_TAGS['1']['etiquetas']), # Intereses
        'tags_hard_json': json.dumps(VACANTE_TAGS['2']['etiquetas']),      # Hard Skills
        'tags_soft_json': json.dumps(VACANTE_TAGS['3']['etiquetas']),      # Soft Skills
    }

def home_trabajador(request):#vista para explorar trabajos
    return render(request, 'home_t.html')

'''

def iniciar_sesion_trabajador(request):
    return render(request, 'iniciar_sesion_trabajador.html')

def logout_trabajador(request):
    return HttpResponse("Funcionalidad de inicio de sesión para trabajadores.")

# Vistas principales de la aplicación

def home_trabajador(request):#vista para explorar trabajos
    return render(request, 'home_trabajador.html')

def perfil_trabajador(request):#vista del perfil del trabajador
    return render(request, 'perfil_trabajador.html')

def mis_postulaciones(request):#vista de las postulaciones del trabajador
    return render(request, 'mis_postulaciones.html')

'''