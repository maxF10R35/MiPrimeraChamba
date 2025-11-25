import json
from aplicaciones.etiquetas import VACANTE_TAGS, SINCO
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from aplicaciones.empresas.models import Empresa, Vacante, Postulacion
from aplicaciones.trabajadores.models import Trabajador
from django.shortcuts import render, redirect
#from django.http import HttpResponse

# Create your views here.


#funciones para el control del usuario empresa

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



def logout_usuario(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('signin')



#Funciones de administracion de vacantes

@login_required
def home(request):
    if request.user.is_anonymous == False:
        empresa = Empresa.objects.get(usuario_id= request.user.id)
        vacantes = Vacante.objects.filter(empresa_id = empresa.id)
        vacantes_activas = vacantes.filter(activa=True)
        context = {
            'vacantes': vacantes,
            'vacantes_a': vacantes_activas,
            'empresa' : empresa
        }

        print(request.user.id)
        print(vacantes)
        return render(request, 'home.html', context)
    else:
        print('Debes iniciar sesion primero')
        messages.error(request, 'Debes iniciar sesión primero para ver tus vacantes.')
        return redirect('signin')



@login_required
def historial_vacantes(request):
    try:
        empresa = request.user.empresa
        # Obtenemos las vacantes y le 'pegamos' el conteo de postulaciones
        vacantes = Vacante.objects.filter(empresa=empresa).order_by('-fecha_publicacion')
        
    except Empresa.DoesNotExist:
        vacantes = []

    return render(request, 'historial.html', {'vacantes': vacantes})



@login_required
def agregar_vacante(request):
    '''
    # Obtener la empresa del usuario actual
    try:
        empresa = request.user.empresa
    except Empresa.DoesNotExist:
        messages.error(request, "Necesitas tener un perfil de empresa para publicar vacantes.")
        return redirect('registro_empresa')
    '''
    #obtener la empresa del usuario actual
    empresa = Empresa.objects.get(usuario_id=request.user.id)

    if request.method == 'POST':
        # Aquí iría la lógica para procesar el formulario y guardar la vacante
        print(request.POST)
        print(F'EMPRESA: {empresa.nombre} con id: {empresa.id}')
        try:
            vacante = Vacante.objects.create(
                nombre_puesto=request.POST.get('nombre_puesto'),
                area_ocupacion=request.POST.get('area_ocupacion'),
                descripcion=request.POST.get('descripcion'),
                requisitos=request.POST.get('requisitos'),
                prestaciones=request.POST.get('prestaciones'),
                salario=request.POST.get('salario'),
                ubicacion=request.POST.get('ubicacion'),
                horario=request.POST.get('horario'),
                tipo_contrato=request.POST.get('tipo_contrato'),
                etiquetas=request.POST.get('etiquetas'),
                empresa=empresa
            )
            vacante.save()
            print(f'Vacante {vacante.nombre_puesto} creada para la empresa {empresa.nombre}.')
            # Después de guardar, redirigir o mostrar un mensaje
            #print('requisitos: ')
            #print(request.POST.get('requisitos'))
            messages.success(request, 'Vacante agregada exitosamente.')
            return redirect('home')  # O a donde quieras redirigir después de agregar
        except Exception as e:
            messages.error(request, 'Ocurrió un error al agregar la vacante.')
            print(f'Error al crear vacante: {e}')
    
    context = {
        'sinco_json': json.dumps(SINCO),
        'tags_json': json.dumps(VACANTE_TAGS)
    }
    return render(request, 'agregar-vacante.html', context)



@login_required
def detalle_vacante(request, id):
    return render(request, 'detalle-vacante.html', {'vacante_id': id})



@login_required
def editar_vacante(request, vacante_id):
   return render(request, 'editar-vacante.html', {'vacante_id': vacante_id})



@login_required
def cambio_estatus(request, vacante_id):
    if request.method == 'POST':
        # Aseguramos que la vacante pertenezca a la empresa del usuario (Seguridad)
        vacante = get_object_or_404(Vacante, id=vacante_id, empresa=request.user.empresa)
        
        # Invertimos el valor (Si es True pasa a False, y viceversa)
        # NOTA: Esto asume que agregaste 'activa = models.BooleanField(default=True)' a tu modelo
        vacante.activa = not vacante.activa 
        vacante.save()
        
        status_msg = "activada" if vacante.activa else "desactivada"
        messages.success(request, f"La vacante ha sido {status_msg}.")
        
    return redirect('historial') # Vuelve a la misma tabla



def mostrar_marco(request):
    return render(request, 'marco.html')