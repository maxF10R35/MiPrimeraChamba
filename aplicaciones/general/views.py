from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def login_usuario(request):
    # 1. Si ya estás dentro, no deberías ver el login. Te mando a tu casa.
    if request.user.is_authenticated:
        if hasattr(request.user, 'empresa'):
            return redirect('home')
        elif hasattr(request.user, 'trabajador'):
            return redirect('home_t')
        return redirect('home') # Fallback

    if request.method == 'POST':
        usuario_input = request.POST.get('username')
        password_input = request.POST.get('password')

        # Lógica para permitir login con Email o Usuario
        username_to_auth = usuario_input
        if '@' in usuario_input:
            try:
                user_obj = User.objects.get(email=usuario_input)
                username_to_auth = user_obj.username
            except User.DoesNotExist:
                pass # Dejar que authenticate falle después

        user = authenticate(request, username=username_to_auth, password=password_input)

        if user is not None:
            if user.is_active:
                login(request, user)
                
                # --- EL GRAN FILTRO DE REDIRECCIÓN ---
                
                # A. ¿Quería ir a un sitio específico? (ej: le dio clic a una vacante sin loguearse)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)

                # B. Si no, lo enviamos a su Dashboard correspondiente
                if hasattr(user, 'empresa'):
                    messages.success(request, f'¡Hola de nuevo, {user.empresa.nombre}!')
                    return redirect('home') # Dashboard Empresa
                
                elif hasattr(user, 'trabajador'):
                    messages.success(request, f'¡Bienvenido, {user.first_name}!')
                    return redirect('home_t') # Dashboard Trabajador
                
                else:
                    # Caso Admin o usuario sin perfil
                    return redirect('/')
            else:
                messages.warning(request, 'Tu cuenta está inactiva.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'login.html')

def logout_usuario(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('login')



def pagina_inicio(request):
    return render(request, 'plantilla_principal_TPC.html')