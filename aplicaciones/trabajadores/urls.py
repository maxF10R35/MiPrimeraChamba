from django.urls import path
from . import views

urlpatterns = [
    path('home_t/', views.home_trabajador, name='home_t'),
    path('registrar_trabajador/', views.registrar_trabajador, name='registrar_trabajador'),
    path('Base/', views.mostrar_base, name='base_trabajadores'),  # Nueva ruta para la base
]