from django.db import models
from django.contrib.auth.models import User
from aplicaciones.trabajadores.models import Trabajador

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False   , blank=False)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(null=False, blank=False, unique=True, default='email')
    biografia = models.TextField(null=False, blank=False, default='Biografía de la empresa.')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    categoria = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.nombre
    

class Vacante(models.Model):
    nombre_puesto = models.CharField(max_length=100, null=False, blank=False)
    area_ocupacion = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField(null=False, blank=False, default='Descripción del puesto.')
    requisitos = models.TextField(null=False, blank=False, default='Requisitos del puesto.')
    prestaciones = models.TextField(null=False, blank=False, default='Prestaciones del puesto.')
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=True)
    ubicacion = models.CharField(max_length=200)
    horario = models.CharField(max_length=100)
    tipo_contrato = models.CharField(max_length=100)
    etiquetas = models.TextField(null=True, blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    activa = models.BooleanField(default=True)
    postulaciones_count = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_puesto


class Postulacion(models.Model):
    
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha_postulacion = models.DateField(null=False, auto_now_add=True)
    estado = models.CharField(max_length=50, null=False, blank=False, default='En revisión')
    D_A_fit = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    N_S_fit = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    P_O_fit = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    compatibilidad = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.trabajador} - {self.vacante}"
