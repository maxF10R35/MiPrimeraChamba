from django.urls import path
from . import views

urlpatterns = [
    path('home_t/', views.home_trabajador, name='home_t'),
    path('registrar_trabajador/', views.registrar_trabajador, name='registrar_trabajador'),
    path('Base/', views.mostrar_base, name='base_trabajadores'),  # Nueva ruta para la base
    path('detalle_vacante_trabajador/<int:vacante_id>/', views.ver_detalle_vacante, name='detail_vac_trab'),
    path('postular_vacante/<int:vacante_id>/', views.postularse, name='postular_vacante'),
    path('mis_postulaciones/', views.mis_postulaciones, name='mis_postulaciones'),
    path('perfil_trabajador/', views.perfil_trabajador, name='perfil_trabajador'),
    path('cancelar_postulacion/<int:postulacion_id>/', views.cancelar_postulacion, name='cancelar_postulacion'),
]