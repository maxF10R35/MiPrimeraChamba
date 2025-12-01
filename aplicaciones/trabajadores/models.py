from django.db import models
from django.contrib.auth.models import User
from aplicaciones.utils import encriptar, desencriptar

# Create your models here.
class Trabajador(models.Model):
    # Información personal
    _nombre_encriptado = models.CharField(db_column="nombre", max_length=500)
    _email_encriptado = models.CharField(db_column="email", max_length=500)
    _apellido_p_encriptado = models.CharField(db_column='apellido_p', max_length=500)
    _apellido_m_encriptado = models.CharField(db_column='apellido_m', max_length=500)
    genero = models.CharField(max_length=20, null=False, blank=False)#opciones: masculino, femenino, otro
    nacionalidad = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    _telefono_encriptado = models.CharField(db_column='telefono', max_length=500)
    _cp_encriptado = models.CharField(db_column='codigo_postal', max_length=200)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    movilidad_limitada = models.BooleanField(default=False)#indica si el trabajador tiene alguna discapacidad motriz
    #cod_post se usará para buscar ofertas cercanas al trabajador


    # Información profesional
    _biografia_encriptada = models.TextField(db_column="bio")
    #biografia = models.TextField(null=True, blank=True)#descripción personal
    estudios = models.CharField(max_length=50, null=False, blank=False)#opciones: en etiquetas.py seccion NIVEL_ESTUDIOS
    titulo = models.CharField(max_length=100, null=True, blank=True)
    ult_area_ocup = models.IntegerField(null=True, blank=True)#opciones: indice de SINCO
    ult_exp = models.CharField(max_length=50, null=True, blank=True)#opciones: tiempo de experiencia en etiquetas.py
    descripcion_exp = models.TextField(null=True, blank=True)#Los detalles de la experiencia laboral
    hard_skills = models.TextField(null=True, blank=True)#lista de habilidades duras separadas por comas derivadas de VACANTE_TAGS['2']
    soft_skills = models.TextField(null=True, blank=True)#lista de habilidades duras separadas por comas derivadas de VACANTE_TAGS['3']

    #Intereses

    area_interes = models.IntegerField(null=True, blank=True)#indice de SINCO
    intereses = models.TextField(null=True, blank=True)#lista de intereses separadas por comas derivadas de VACANTE_TAGS['1']


    # Setters y getters para campos encriptados
    @property
    def nombre(self):
        return desencriptar(self._nombre_encriptado)
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre_encriptado = encriptar(valor)

    @property
    def email(self):
        return desencriptar(self._email_encriptado)
    
    @email.setter
    def email(self, valor):
        self._email_encriptado = encriptar(valor)

    @property
    def apellido_p(self):
        return desencriptar(self._apellido_p_encriptado)
    
    @apellido_p.setter
    def apellido_p(self, valor):
        self._apellido_p_encriptado = encriptar(valor)


    @property
    def apellido_m(self):
        return desencriptar(self._apellido_m_encriptado)
    
    @apellido_m.setter
    def apellido_m(self, valor):
        self._apellido_m_encriptado = encriptar(valor)

    
    @property
    def telefono(self):
        return desencriptar(self._telefono_encriptado)
    
    @telefono.setter
    def telefono(self, valor):
        self._telefono_encriptado = encriptar(valor)

    
    @property
    def cod_post(self):
        # A. Recuperamos el texto encriptado
        texto = desencriptar(self._cp_encriptado)
        
        # B. Lo convertimos a ENTERO antes de entregártelo
        if texto and texto.isdigit():
            return int(texto)
        return None
    
    @cod_post.setter
    def cod_post(self, valor_numerico):
        # A. Aseguramos que sea string para poder encriptarlo
        texto = str(valor_numerico)
        
        # B. Encriptamos y guardamos
        self._cp_encriptado = encriptar(texto)


    @property
    def biografia(self):
        return desencriptar(self._biografia_encriptada)

    @biografia.setter
    def biografia(self, texto_largo):
        self._biografia_encriptada = encriptar(texto_largo)


    def __str__(self):
        return f"{self.nombre} {self.apellido_p}"