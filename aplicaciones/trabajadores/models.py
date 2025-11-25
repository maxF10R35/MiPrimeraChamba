from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trabajador(models.Model):
    # Información personal
    nombre = models.CharField(max_length=20, null=False, blank=False)
    apellido_p = models.CharField(max_length=20, null=False, blank=False)
    apellido_m = models.CharField(max_length=20, null=False, blank=False)
    genero = models.CharField(max_length=20, null=False, blank=False)#opciones: masculino, femenino, otro
    nacionalidad = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    cod_post = models.IntegerField(null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    movilidad_limitada = models.BooleanField(default=False)#indica si el trabajador tiene alguna discapacidad motriz

    # Información profesional
    biografia = models.TextField(null=True, blank=True)#descripción personal
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

    def __str__(self):
        return f"{self.nombre} {self.apellido_p}"