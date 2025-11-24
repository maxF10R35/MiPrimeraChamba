from django.db import models
from django.contrib.auth.models import User

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
    nombre_puesto = models.CharField(max_length=100, unique=True, null=False   , blank=False)
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

    def __str__(self):
        return self.nombre_puesto


