import json
from aplicaciones.etiquetas import VACANTE_TAGS
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from aplicaciones.empresas.models import Empresa, Vacante, Postulacion
from aplicaciones.trabajadores.models import Trabajador
from django.shortcuts import render, redirect
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def SignUp(request):
    # Contexto base (se usa tanto en GET como en POST si falla)
    sectores_data = VACANTE_TAGS['1']['etiquetas']
    context = {
        'sectores_json': json.dumps(sectores_data)
    }

    if request.method == 'POST':
        # OBTENCIÓN DE DATOS
        print(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        biografia = request.POST.get('biografia')
        categoria = request.POST.get('categoria')
        

        # VERIFICACIÓN: ¿Existe el usuario?
        if User.objects.filter(username=username).exists():
            # CASO DE ERROR: El usuario ya existe
            messages.error(request, f'El usuario "{username}" ya está registrado. Por favor elige otro.')
            print(f"El usuario {username} ya existe.")
            # Retornamos render (no redirect) para que el usuario no pierda lo que escribió (opcionalmente)
            # y vea el mensaje de error en la misma página.
            return render(request, 'signup.html', context)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Ese correo electrónico ya está registrado.')
            return render(request, 'signup.html', context)

        # 3. Si pasa los filtros, guardas el usuario
        try:
            # Aquí iría tu lógica real de creación (User.objects.create_user...)
            print(f"Creando usuario: {username}, email: {email}")
            user = User.objects.create_user(username, email, password)
            empresa = Empresa.objects.create(usuario=user, nombre=nombre, telefono=telefono,
                                             direccion=direccion, biografia=biografia,
                                             categoria=categoria, email=email)
            messages.success(request, '¡Cuenta creada exitosamente! Por favor inicia sesión.')
            print(f"Empresa {nombre} creado con éxito.")
            return redirect('signin') # O a donde quieras mandarlo
        except Exception as e:
            messages.error(request, 'Ocurrió un error inesperado al guardar.')
            print(f"Error: {e}")

    # Si es GET o si hubo error, mostramos la página
    return render(request, 'signup.html', context)

def SignIn(request):
    if request.method == 'POST':
        usuario_input = request.POST.get('username') # El HTML manda 'username' aunque sea email
        password_input = request.POST.get('password')

        username_to_auth = usuario_input

        # 1. Lógica para permitir acceso con Email
        if '@' in usuario_input:
            try:
                # Buscamos al usuario que tenga este email
                user_obj = User.objects.get(email=usuario_input)
                # Si existe, usamos su username real para autenticar
                username_to_auth = user_obj.username
            except User.DoesNotExist:
                # Si el email no existe, dejamos que authenticate falle abajo
                pass

        # 2. Autenticación estándar de Django
        user = authenticate(request, username=username_to_auth, password=password_input)

        if user is not None:
            # Credenciales correctas
            if user.is_active:
                login(request, user) # Crea la sesión
                messages.success(request, f'¡Bienvenido de nuevo, {user.username}!')
                
                # Redirección: Si intentó entrar a una url protegida, lo mandamos ahí (next), si no al home
                #next_url = request.GET.get('next', 'home') 
                return redirect('home') 
            else:
                messages.warning(request, 'Tu cuenta está inactiva. Contacta a soporte.')
        else:
            # Credenciales incorrectas
            messages.error(request, 'Usuario, correo o contraseña incorrectos.')
    
    # Si es GET o falló el login, mostramos la página
    return render(request, 'signin.html')

def agregar_vacante(request):
    return render(request, 'agregar-vacante.html')

def detalle_vacante(request, id):
    return render(request, 'detalle-vacante.html', {'vacante_id': id})

def editar_vacante(request, vacante_id):
   return render(request, 'editar-vacante.html', {'vacante_id': vacante_id})

def historial_vacantes(request):
    return render(request, 'historial.html')

def logout_usuario(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('signin')