from django.shortcuts import redirect
from django.contrib import messages

# Decorador para vistas exclusivas de EMPRESAS
def empresa_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        # 1. Si no está logueado, al login
        if not request.user.is_authenticated:
            return redirect('login')
        
        # 2. Si es una Empresa, pase usted
        if hasattr(request.user, 'empresa'):
            return view_func(request, *args, **kwargs)
        else:
            # 3. Si es Trabajador (o admin sin perfil empresa), fuera de aquí
            messages.warning(request, "Esta sección es solo para reclutadores.")
            return redirect('home_trabajador') # Redirigir a SU zona
            
    return wrapper_func

# Decorador para vistas exclusivas de TRABAJADORES
def trabajador_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
            
        if hasattr(request.user, 'trabajador'):
            return view_func(request, *args, **kwargs)
        else:
            messages.info(request, "Estás logueado como empresa. Cierra sesión para buscar empleo.")
            return redirect('home') # Redirigir a zona empresa
            
    return wrapper_func