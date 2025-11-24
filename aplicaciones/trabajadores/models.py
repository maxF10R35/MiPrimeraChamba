from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trabajador(models.Model):
    # Información personal
    nombre = models.CharField(max_length=20, null=False, blank=False)
    apellido_p = models.CharField(max_length=20, null=False, blank=False)
    apellido_m = models.CharField(max_length=20, null=False, blank=False)
    genero = models.CharField(max_length=20, null=False, blank=False)
    nacionalidad = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    cod_post = models.IntegerField(null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # Información profesional
    
    estudios = models.CharField(max_length=50, null=False, blank=False)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    ult_area_ocup = models.IntegerField(null=True, blank=True)
    ult_exp = models.CharField(max_length=50, null=True, blank=True)
    hard_skills = models.TextField(null=True, blank=True)
    soft_skills = models.TextField(null=True, blank=True)

    #Intereses

    area_interes = models.IntegerField(null=True, blank=True)
    intereses = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_p}"