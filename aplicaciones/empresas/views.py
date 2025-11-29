import json
from aplicaciones.etiquetas import VACANTE_TAGS, SINCO
from django.contrib import messages
from django.contrib.auth.models import User
#from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from aplicaciones.general.decorators import empresa_required
from django.shortcuts import get_object_or_404
from aplicaciones.empresas.models import Empresa, Vacante, Postulacion
from aplicaciones.trabajadores.models import Trabajador
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from aplicaciones.etiquetas import SINCO, VACANTE_TAGS, GENERO_OPCIONES, NIVEL_ESTUDIOS, TIEMPO_EXPERIENCIA


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
            return redirect('login') # O a donde quieras mandarlo
        except Exception as e:
            messages.error(request, 'Ocurrió un error inesperado al guardar.')
            print(f"Error: {e}")

    # Si es GET o si hubo error, mostramos la página
    return render(request, 'signup.html', context)

#funciones de inicion de sesión, ahora se invocan desde aplicaciones/general/
'''
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

'''

'''
def logout_usuario(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('signin')
'''


#Funciones de administracion de vacantes

@empresa_required
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



@empresa_required
def historial_vacantes(request):
    try:
        empresa = request.user.empresa
        # Obtenemos las vacantes y le 'pegamos' el conteo de postulaciones
        vacantes = Vacante.objects.filter(empresa=empresa).order_by('-fecha_publicacion')
        
    except Empresa.DoesNotExist:
        vacantes = []

    return render(request, 'historial_v2.html', {'vacantes': vacantes})



@empresa_required
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


@empresa_required
def detalle_vacante(request, id):
    # 1. Obtener la vacante asegurando que sea de la empresa actual
    vacante = get_object_or_404(Vacante, id=id, empresa=request.user.empresa)
    
    # 2. Obtener postulaciones
    postulaciones = Postulacion.objects.filter(vacante=vacante).order_by('-compatibilidad')

    # --- PROCESAMIENTO DE DATOS PARA LA VISTA ---

    # A) SINCO: Buscar el nombre del subgrupo
    nombre_area = "No especificada"
    area_id = str(vacante.area_ocupacion) # Convertimos a string para buscar en el dict
    
    # Recorremos el diccionario SINCO para encontrar el ID
    found = False
    for div_id, div_data in SINCO.items():
        if found: break
        for grupo_id, grupo_data in div_data.get('grupos', {}).items():
            subgrupos = grupo_data.get('subgrupos', {})
            if area_id in subgrupos:
                nombre_area = subgrupos[area_id] # ¡Encontrado!
                found = True
                break

    # B) ETIQUETAS: Convertir IDs "11,36" a Nombres "Tecnología, Trabajo en equipo"
    nombres_etiquetas = []
    if vacante.etiquetas:
        ids_tags = vacante.etiquetas.split(',')
        # Recorremos VACANTE_TAGS para buscar cada ID
        for tag_id in ids_tags:
            for cat_id, cat_data in VACANTE_TAGS.items():
                mis_etiquetas = cat_data.get('etiquetas', {})
                if tag_id in mis_etiquetas:
                    nombres_etiquetas.append(mis_etiquetas[tag_id]['nombre'])
                    break # Pasamos al siguiente tag_id

    # C) REQUISITOS Y PRESTACIONES: Separar por '|||'
    # Creamos listas limpias para iterar fácil en el HTML
    lista_requisitos = vacante.requisitos.split('|||') if vacante.requisitos else []
    lista_prestaciones = vacante.prestaciones.split('|||') if vacante.prestaciones else []

    # D) COMPATIBILIDAD: Ajustar a porcentaje (0-100)
    # No guardamos en BD, solo modificamos los objetos en memoria para esta vista
    for post in postulaciones:
        if post.compatibilidad:
            post.porcentaje_fit = int(post.compatibilidad * 100)
        else:
            post.porcentaje_fit = 0

    context = {
        'vacante': vacante,
        'postulaciones': postulaciones,
        'nombre_area_sinco': nombre_area,     # Dato procesado A
        'lista_etiquetas': nombres_etiquetas, # Dato procesado B
        'lista_requisitos': lista_requisitos, # Dato procesado C
        'lista_prestaciones': lista_prestaciones # Dato procesado C
    }
    
    return render(request, 'detalle-vacante.html', context)


@empresa_required
def editar_vacante(request, vacante_id):
    # 1. Obtener vacante y validar propiedad
    vacante = get_object_or_404(Vacante, id=vacante_id, empresa=request.user.empresa)

    if request.method == 'POST':
        try:
            # 2. Actualizar campos básicos
            vacante.nombre_puesto = request.POST.get('nombre_puesto')
            vacante.salario = request.POST.get('salario')
            vacante.tipo_contrato = request.POST.get('tipo_contrato')
            vacante.horario = request.POST.get('horario')
            vacante.ubicacion = request.POST.get('ubicacion')
            vacante.descripcion = request.POST.get('descripcion')
            
            # 3. Actualizar campos complejos (Listas y Tags)
            vacante.requisitos = request.POST.get('requisitos') # Viene separado por |||
            vacante.prestaciones = request.POST.get('prestaciones') # Viene separado por |||
            vacante.etiquetas = request.POST.get('etiquetas') # Viene separado por comas
            
            # 4. Actualizar SINCO (Solo si el usuario seleccionó uno nuevo, si no, mantenemos el anterior)
            nuevo_sinco = request.POST.get('area_ocupacion')
            if nuevo_sinco:
                vacante.area_ocupacion = nuevo_sinco

            # 5. BORRADO DE POSTULACIONES (Regla de Negocio)
            # Al cambiar los requisitos, los candidatos actuales pierden validez.
            count_deleted, _ = vacante.postulacion_set.all().delete()
            
            # Resetear contador de postulaciones en el modelo Vacante (si lo usas desnormalizado)
            vacante.postulaciones_count = 0 
            
            vacante.save()

            if count_deleted > 0:
                messages.warning(request, f"Vacante actualizada. Se eliminaron {count_deleted} postulaciones antiguas debido a los cambios.")
            else:
                messages.success(request, "Vacante actualizada exitosamente.")
                
            return redirect(f'/empresas/detalle-vacante/{vacante.id}')

        except Exception as e:
            messages.error(request, f"Error al actualizar: {str(e)}")
    
    # GET: Preparamos datos para pre-llenar el formulario
    context = {
        'vacante': vacante,
        'sinco_json': json.dumps(SINCO),
        'tags_json': json.dumps(VACANTE_TAGS)
    }
    return render(request, 'editar-vacante.html', context)


@empresa_required
def cambio_estatus(request, vacante_id):
    #if request.method == 'POST':
    # Aseguramos que la vacante pertenezca a la empresa del usuario (Seguridad)
    vacante = get_object_or_404(Vacante, id=vacante_id, empresa=request.user.empresa)
        
    # Invertimos el valor (Si es True pasa a False, y viceversa)
    # NOTA: Esto asume que agregaste 'activa = models.BooleanField(default=True)' a tu modelo
    vacante.activa = not vacante.activa 
    vacante.save()
        
    status_msg = "activada" if vacante.activa else "desactivada"
    messages.success(request, f"La vacante ha sido {status_msg}.")
        
    return redirect('home') # Vuelve a la misma tabla


@empresa_required
def perfil_empresa(request):
    try:
        empresa = request.user.empresa
    except Empresa.DoesNotExist:
        return redirect('signup')

    # --- PROCESAMIENTO DE ETIQUETAS (SECTORES) ---
    # Convertimos los IDs guardados en la BD a nombres legibles
    nombres_sectores = []
    if empresa.categoria:
        ids_sectores = empresa.categoria.split(',')
        # Accedemos directamente a la sección 1 (Sectores) de VACANTE_TAGS
        sectores_data = VACANTE_TAGS.get('1', {}).get('etiquetas', {})
        
        for sec_id in ids_sectores:
            if sec_id in sectores_data:
                nombres_sectores.append(sectores_data[sec_id]['nombre'])

    context = {
        'empresa': empresa,
        'lista_sectores': nombres_sectores,
        # Opcional: Agregamos conteo de vacantes para mostrar actividad
        'total_vacantes': empresa.vacante_set.count(),
        'vacantes_activas': empresa.vacante_set.filter(activa=True).count()
    }
    
    return render(request, 'perfil-empresa.html', context)



@login_required
@empresa_required
def ver_perfil_candidato(request, postulacion_id): # Cambiamos el argumento recibido
    # 1. Obtener la postulación asegurando que sea de una vacante de la empresa actual
    # Esto es vital para la seguridad: evita que una empresa vea postulaciones de otra.
    postulacion = get_object_or_404(Postulacion, id=postulacion_id, vacante__empresa=request.user.empresa)
    
    # 2. Actualizar estado a "Visto" o "Revisado" automáticamente
    if postulacion.estado == 'En revisión':
        postulacion.estado = 'Visto' # O el texto que prefieras mostrar al candidato
        postulacion.save()

    # 3. Obtener el objeto trabajador desde la postulación
    candidato = postulacion.trabajador

    # --- HELPERS PARA TRADUCIR CÓDIGOS ---
    def get_sinco_name(code):
        if not code: return "No especificado"
        code_str = str(code)
        for div in SINCO.values():
            for grp in div['grupos'].values():
                if code_str in grp['subgrupos']:
                    return grp['subgrupos'][code_str]
        return "Área desconocida"

    def get_tag_names(ids_str, section_key):
        if not ids_str: return []
        names = []
        ids = ids_str.split(',')
        tags_dict = VACANTE_TAGS[section_key]['etiquetas']
        for tag_id in ids:
            if tag_id in tags_dict:
                names.append(tags_dict[tag_id]['nombre'])
        return names

    # --- PREPARAR CONTEXTO ---
    context = {
        'candidato': candidato,
        'postulacion': postulacion, # Pasamos también la postulación por si quieres mostrar la fecha o el estado
        # Datos traducidos
        'genero_texto': GENERO_OPCIONES.get(candidato.genero, 'No especificado'),
        'estudios_texto': NIVEL_ESTUDIOS.get(candidato.estudios, 'No especificado'),
        'experiencia_texto': TIEMPO_EXPERIENCIA.get(candidato.ult_exp, 'Sin experiencia'),
        'area_ocup_texto': get_sinco_name(candidato.ult_area_ocup),
        
        # Listas de Habilidades
        'hard_skills': get_tag_names(candidato.hard_skills, '2'),
        'soft_skills': get_tag_names(candidato.soft_skills, '3'),
    }

    return render(request, 'perfil_candidato.html', context)


#Funciones auxxiliares
def mostrar_marco(request):
    return render(request, 'marco.html')