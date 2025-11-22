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