"""
URL configuration for MPC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplicaciones.general import views as general_views # Importamos la vista nueva


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', general_views.pagina_inicio, name='inicio'), # Opcional: Raíz lleva al login
    path('login/', general_views.login_usuario, name='login'),       # <--- LA IMPORTANTE
    path('logout/', general_views.logout_usuario, name='logout'),
    path('empresas/', include('aplicaciones.empresas.urls')),
    path('trabajadores/', include('aplicaciones.trabajadores.urls')),
]
