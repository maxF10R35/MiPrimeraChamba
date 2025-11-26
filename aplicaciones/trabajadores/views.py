from django.shortcuts import render
from django.http import HttpResponse
import json
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from aplicaciones.general.decorators import trabajador_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Trabajador
from aplicaciones.empresas.models import Vacante, Postulacion
from django.shortcuts import get_object_or_404
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





@login_required
@trabajador_required
def home_trabajador(request):
    # 1. Obtener todas las vacantes activas, ordenadas por las más recientes
    # Usamos select_related para traer los datos de la empresa en la misma consulta (eficiencia)
    vacantes = Vacante.objects.filter(activa=True).select_related('empresa').order_by('-fecha_publicacion')

    # 2. Procesamiento de datos para la vista (Tags y Logos)
    # Como no podemos modificar el objeto guardado en BD, modificamos la instancia en memoria
    for vacante in vacantes:
        # A. Procesar Etiquetas (IDs -> Nombres)
        lista_tags = []
        if vacante.etiquetas:
            ids = vacante.etiquetas.split(',')
            # Buscamos en todas las categorías de VACANTE_TAGS
            for tag_id in ids:
                found = False
                for cat_key, cat_val in VACANTE_TAGS.items():
                    if tag_id in cat_val['etiquetas']:
                        lista_tags.append(cat_val['etiquetas'][tag_id]['nombre'])
                        found = True
                        break
                if len(lista_tags) >= 3: # Limitamos a 3 tags para no saturar la tarjeta
                    break
        vacante.tag_nombres = lista_tags

        # B. Inicial de la Empresa (para el logo placeholder)
        if vacante.empresa and vacante.empresa.nombre:
            vacante.empresa_inicial = vacante.empresa.nombre[0].upper()
        else:
            vacante.empresa_inicial = "?"

    context = {
        'vacantes': vacantes
    }
    
    return render(request, 'home_t.html', context)


@login_required
@trabajador_required
def ver_detalle_vacante(request, vacante_id):
    # 1. Obtener vacante activa
    vacante = get_object_or_404(Vacante, id=vacante_id, activa=True)
    
    # 2. Verificar si ya se postuló (Para deshabilitar el botón)
    ya_postulado = Postulacion.objects.filter(
        vacante=vacante, 
        trabajador=request.user.trabajador
    ).exists()

    # 3. Procesar Etiquetas (IDs -> Nombres)
    lista_tags = []
    if vacante.etiquetas:
        ids = vacante.etiquetas.split(',')
        for tag_id in ids:
            for cat_val in VACANTE_TAGS.values():
                if tag_id in cat_val['etiquetas']:
                    lista_tags.append(cat_val['etiquetas'][tag_id]['nombre'])
                    break
    
    # 4. Procesar Listas (Requisitos/Prestaciones con |||)
    requisitos_list = vacante.requisitos.split('|||') if vacante.requisitos else []
    prestaciones_list = vacante.prestaciones.split('|||') if vacante.prestaciones else []

    # 5. Inicial Empresa
    inicial_empresa = vacante.empresa.nombre[0].upper() if vacante.empresa else "?"

    context = {
        'vacante': vacante,
        'lista_tags': lista_tags,
        'requisitos_list': requisitos_list, # Lista limpia
        'prestaciones_list': prestaciones_list, # Lista limpia
        'inicial_empresa': inicial_empresa,
        'ya_postulado': ya_postulado
    }
    return render(request, 'detalle_vacante_trabajador.html', context)




@login_required
@trabajador_required
def postularse(request, vacante_id):
    vacante = get_object_or_404(Vacante, id=vacante_id)
    trabajador = request.user.trabajador
    
    # Verificar si ya existe postulación
    if Postulacion.objects.filter(vacante=vacante, trabajador=trabajador).exists():
        messages.warning(request, "Ya te has postulado a esta vacante.")
        return redirect('home_t')

    # --- MANEJO DEL POST (Procesar Formulario) ---
    if request.method == 'POST':
        try:
            # === 1. OBTENCIÓN DE DATOS ===
            es_rapida = request.POST.get('es_rapida') == 'true'
            # A. Datos del Usuario (Depende si es rápida o normal)
            if es_rapida:
                # Tomar del perfil
                u_exp = int(trabajador.ult_exp) if trabajador.ult_exp and trabajador.ult_exp.isdigit() else 0
                u_hard = trabajador.hard_skills.split(',') if trabajador.hard_skills else []
                u_soft = trabajador.soft_skills.split(',') if trabajador.soft_skills else []
                # En rápida, asumimos satisfacción máxima (el usuario quiere el trabajo)
                satisfaccion_avg = 5
            else:
                # Tomar del formulario
                # Experiencia: Si marcó el check de experiencia específica, usamos esa, si no, la del perfil o 0
                if request.POST.get('tiene_experiencia_area'):
                    u_exp = int(request.POST.get('tiempo_experiencia', 0))
                else:
                    u_exp = 0 # O podrías usar trabajador.ult_exp como fallback
                
                u_hard = request.POST.getlist('hard_skills_selected')
                u_soft = request.POST.getlist('soft_skills_selected')
                
                # Calcular promedio de satisfacción (1-5)
                s1 = int(request.POST.get('sat_sueldo', 0))
                s2 = int(request.POST.get('sat_horario', 0))
                s3 = int(request.POST.get('sat_requisitos', 0))
                s4 = int(request.POST.get('sat_prestaciones', 0))
                satisfaccion_avg = (s1 + s2 + s3 + s4) / 4 if (s1+s2+s3+s4) > 0 else 0                
            
            # B. Datos de la Vacante (Requeridos)
            # Nota: Asumimos que agregaste estos campos al modelo Vacante como mencionaste.
            # Si no tienen valor, usamos defaults para evitar división por cero.
            
            # Escolaridad requerida (Asumimos un valor medio '22' Bachillerato si no existe campo)
            v_esc = int(vacante.escolaridad_minima) 
            #v_esc = 22 # Placeholder, ajusta según tu modelo real
            u_esc = int(trabajador.estudios) if trabajador.estudios and trabajador.estudios.isdigit() else 0
            
            v_exp = int(vacante.tiempo_experiencia) if hasattr(vacante, 'tiempo_experiencia') and vacante.tiempo_experiencia else 0
            
            # Obtener etiquetas requeridas de la vacante (Hard vs Soft)
            v_tags = vacante.etiquetas.split(',') if vacante.etiquetas else []
            v_hard_req = []
            v_soft_req = []

            # Clasificar tags de la vacante usando el diccionario global
            for tag_id in v_tags:
                if tag_id in VACANTE_TAGS['2']['etiquetas']: # Sección 2 = Hard
                    v_hard_req.append(tag_id)
                elif tag_id in VACANTE_TAGS['3']['etiquetas']: # Sección 3 = Soft
                    v_soft_req.append(tag_id)

            # === 2. CÁLCULO DE ÍNDICES (Fórmulas PDF) ===

            # --- A. D-A Fit (Demanda - Habilidades) ---
            # Alpha: Escolaridad (1 - |Req - User| / 61) -> Rango [10, 71], max dif = 61
            dif_esc = abs(v_esc - u_esc)
            alpha = 1 - (dif_esc / 61)
            alpha = max(0, alpha) # Evitar negativos

            # Beta: Experiencia (1 - |Req - User| / 7) -> Rango [0, 7]
            dif_exp = abs(v_exp - u_exp)
            beta = 1 - (dif_exp / 7)
            beta = max(0, beta)

            # Sigma: Hard Skills (Coincidencias / Requeridas)
            # Intersección de sets para contar coincidencias únicas
            matches_hard = len(set(u_hard) & set(v_hard_req))
            total_hard_req = len(v_hard_req)
            sigma = (matches_hard / total_hard_req) if total_hard_req > 0 else 1 # Si no pide nada, tienes 100%

            # Promedio D-A Fit
            da_fit = (alpha + beta + sigma) / 3

            # --- B. N-S Fit (Necesidades - Suministros) ---
            # Promedio de satisfacción / 5
            ns_fit = satisfaccion_avg / 5

            # --- C. P-O Fit (Persona - Organización) ---
            # Soft Skills (Coincidencias / Requeridas)
            matches_soft = len(set(u_soft) & set(v_soft_req))
            total_soft_req = len(v_soft_req)
            po_fit = (matches_soft / total_soft_req) if total_soft_req > 0 else 1

            # === 3. CÁLCULO FINAL ===
            # Compatibilidad Promedio (Por ahora, luego será MLP)
            compatibilidad_final = (da_fit + ns_fit + po_fit) / 3

            # === 4. GUARDAR ===
            Postulacion.objects.create(
                vacante=vacante,
                trabajador=trabajador,
                estado='En revisión',
                # Guardamos los índices calculados para futuro entrenamiento de la IA
                D_A_fit=Decimal(da_fit),
                N_S_fit=Decimal(ns_fit),
                P_O_fit=Decimal(po_fit),
                compatibilidad=Decimal(compatibilidad_final)
            )

            # Actualizar contador de la vacante
            vacante.postulaciones_count += 1
            vacante.save()

            messages.success(request, f"¡Postulación enviada! Tu compatibilidad inicial es del {int(compatibilidad_final * 100)}%")
            return redirect('home_t')
        
        except Exception as e:
            messages.error(request, f"Ocurrió un error al procesar tu postulación: {str(e)}")
            return redirect('detail_vac_trab', vacante_id=vacante_id)

    # --- MANEJO DEL GET (Mostrar Formulario) ---
    
    # Preparamos los diccionarios para el template
    context = {
        'vacante': vacante,
        # Diccionarios directos para iterar en el template
        'hard_skills_dict': VACANTE_TAGS['2']['etiquetas'],
        'soft_skills_dict': VACANTE_TAGS['3']['etiquetas'],
        'tiempo_experiencia_dict': TIEMPO_EXPERIENCIA,
        
        # Diccionario simple para iterar los campos de estrellas
        'satisfaccion_fields': {
            'sat_sueldo': 'Sueldo Ofrecido',
            'sat_horario': 'Horario de Trabajo',
            'sat_requisitos': 'Requisitos Solicitados',
            'sat_prestaciones': 'Prestaciones y Beneficios'
        },
        
        # Datos procesados para mostrar info útil en el panel derecho
        'nombre_area_sinco': "Tecnología (Ejemplo)", # Aquí deberías buscar el nombre real en SINCO usando vacante.area_ocupacion
        'requisitos_list': vacante.requisitos.split('|||') if vacante.requisitos else [],
        'prestaciones_list': vacante.prestaciones.split('|||') if vacante.prestaciones else [],
    }
    
    return render(request, 'postulacion_form.html', context)

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

def mostrar_base(request):
    return render(request, 'base_trabajadores.html')