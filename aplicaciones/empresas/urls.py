from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('SignUp/', views.SignUp, name='signup'),
    path('SignIn/', views.SignIn, name='signin'),
    path('agregar-vacante/', views.agregar_vacante, name='add'),
    path('detalle-vacante/<int:id>', views.detalle_vacante, name='detail'),
    path('editar-vacante/<int:vacante_id>', views.editar_vacante, name='edit'),
    path('historial-vacantes/', views.historial_vacantes, name='history'),
]