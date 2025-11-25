from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pag_inicio'),
    path('login/', views.pagina_login, name='login'),
]